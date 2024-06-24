import tkinter as tk
from tkinter import ttk, messagebox
from promptpay import qrcode
from PIL import ImageTk, Image
import io
import sqlite3
import os
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import pandas as pd
from tkcalendar import Calendar

class CoffeeShopPOS(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Coffee Shop POS")
        self.geometry("1225x900")
        self.configure(bg="#f8f8f8")

        self.create_styles()
        self.create_item_buttons_frame()
        self.create_order_summary_frame()

        self.order = {}
        self.total_price = 0.0

        # Initialize database
        self.conn = self.create_db_connection()
        self.create_db_table()
        
        self.customer_count = self.get_customer_count()
        self.update_customer_count_label()

        self.cash_payment_window = None
        self.cash_amount_var = tk.DoubleVar()

    def create_styles(self):
        style = ttk.Style()
        style.theme_use("clam")
        style.configure("TFrame", background="#f8f8f8")
        style.configure("TButton", font=("Consolas", 12), padding=10, background="#ffffff", foreground="#333333")
        style.configure("TLabel", font=("Consolas", 14), background="#f8f8f8", foreground="#333333")
        style.configure("Order.TLabel", font=("Consolas", 12), background="#ffffff", padding=10)
        style.configure("Treeview", font=("Consolas", 12), background="#ffffff", foreground="#333333", rowheight=25)
        style.configure("Treeview.Heading", font=("Consolas", 14, "bold"), background="#ffffff", foreground="#333333")
        style.configure("TCombobox", font=("Consolas", 12), padding=10)

    def create_db_connection(self):
        db_exists = os.path.exists("orders.db")
        conn = sqlite3.connect("orders.db")
        if db_exists:
            print("Connected to existing database.")
        else:
            print("Created a new database.")
        return conn

    def create_db_table(self):
        cursor = self.conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS orders (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                customer_id INTEGER,
                item_name TEXT,
                quantity INTEGER,
                price REAL,
                order_date TEXT,
                order_time TEXT
            )
        """)
        self.conn.commit()
        print("Database table checked/created.")  # Debug statement

    def get_customer_count(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT MAX(customer_id) FROM orders WHERE order_date = ?", (datetime.now().strftime("%d-%m-%Y"),))
        result = cursor.fetchone()
        return result[0] + 1 if result[0] else 1

    def create_item_buttons_frame(self):
        items_frame = ttk.Frame(self, style="TFrame")
        items_frame.grid(row=0, column=0, padx=20, pady=20, sticky="nw")

        items = [
            ("Latte", 15), ("Espresso", 10), ("Froid", 12), ("Flat White", 15),
            ("Caramel Latte", 18), ("Cappuccino", 13), ("Americano", 12), 
            ("Hazelnut", 17), ("Ice Tea", 10), ("Iced Coffee", 14), ("Hot Chocolate", 16),
            ("Chai Black", 15), ("Chai Plain", 13), ("Tea Colored", 10), ("Inner Elegant", 22),
            ("Truffle Cupcakes", 20), ("Rainbow Cakes", 25), ("Truffle Floss", 18), ("Waffles", 12)
        ]

        for index, (name, price) in enumerate(items):
            btn = ttk.Button(items_frame, text=f"{name}\n฿{price:.2f}", command=lambda name=name, price=price: self.add_to_order(name, price))
            btn.grid(row=index // 4, column=index % 4, padx=10, pady=10, ipadx=10, ipady=10)

    def create_order_summary_frame(self):
        summary_frame = ttk.Frame(self, style="TFrame")
        summary_frame.grid(row=0, column=1, padx=20, pady=20, sticky="ne")

        tk.Label(summary_frame, text="Current Order", font=("Consolas", 16, "bold"), bg="#f8f8f8", fg="#333333").grid(row=0, column=0, pady=10)

        self.order_tree = ttk.Treeview(summary_frame, columns=("Item", "Quantity", "Price"), show='headings', style="Treeview")
        self.order_tree.heading("Item", text="Item")
        self.order_tree.heading("Quantity", text="Quantity")
        self.order_tree.heading("Price", text="Price")

        self.order_tree.column("Item", width=150)
        self.order_tree.column("Quantity", width=100)
        self.order_tree.column("Price", width=100)

        self.order_tree.grid(row=1, column=0, padx=10, pady=10)

        self.total_label = ttk.Label(summary_frame, text="Total: ฿0.00", font=("Consolas", 14, "bold"), style="TLabel")
        self.total_label.grid(row=2, column=0, padx=10, pady=10)

        self.delete_button = tk.Button(summary_frame, text="Delete Selected Item", command=self.delete_selected_item, bg="#e74c3c", fg="#ffffff", font=("Consolas", 12, "bold"), bd=0, relief="flat")
        self.delete_button.grid(row=3, column=0, padx=10, pady=10, ipadx=10, ipady=5)

        self.payment_method_label = ttk.Label(summary_frame, text="Select Payment Method:", style="TLabel")
        self.payment_method_label.grid(row=4, column=0, padx=10, pady=5)

        self.payment_method = ttk.Combobox(summary_frame, values=["Cash", "QR Code", "True Money Wallet"], style="TCombobox")
        self.payment_method.grid(row=5, column=0, padx=10, pady=5)
        self.payment_method.current(0)  # Set default to "Cash"

        self.pay_button = tk.Button(summary_frame, text="Pay", command=self.pay, bg="#27ae60", fg="#ffffff", font=("Consolas", 12, "bold"), bd=0, relief="flat")
        self.pay_button.grid(row=6, column=0, padx=10, pady=10, ipadx=10, ipady=5)

        self.customer_count_label = ttk.Label(summary_frame, text="Customer Count: 0", font=("Consolas", 14, "bold"), style="TLabel")
        self.customer_count_label.grid(row=7, column=0, padx=10, pady=10)

        self.past_orders_button = tk.Button(summary_frame, text="Check Orders", command=self.show_past_orders, bg="#3498db", fg="#ffffff", font=("Consolas", 12, "bold"), bd=0, relief="flat")
        self.past_orders_button.grid(row=8, column=0, padx=10, pady=10, ipadx=10, ipady=5)

        self.report_button = tk.Button(summary_frame, text="Show Sales Report", command=self.show_report_calendar, bg="#8e44ad", fg="#ffffff", font=("Consolas", 12, "bold"), bd=0, relief="flat")
        self.report_button.grid(row=9, column=0, padx=10, pady=10, ipadx=10, ipady=5)

    def update_customer_count_label(self):
        self.customer_count_label.config(text=f"Customer Count: {self.customer_count}")

    def add_to_order(self, name, price):
        if name in self.order:
            self.order[name]["quantity"] += 1
            self.order[name]["total_price"] += price
        else:
            self.order[name] = {"price": price, "quantity": 1, "total_price": price}

        self.update_order_tree()
        self.update_total(price)

    def update_order_tree(self):
        for row in self.order_tree.get_children():
            self.order_tree.delete(row)

        for item, details in self.order.items():
            self.order_tree.insert("", tk.END, values=(item, details["quantity"], f"฿{details['total_price']:.2f}"))

    def update_total(self, price):
        self.total_price += price
        self.total_label.config(text=f"Total: ฿{self.total_price:.2f}")

    def delete_selected_item(self):
        selected_item = self.order_tree.selection()
        if selected_item:
            item_values = self.order_tree.item(selected_item, "values")
            item_name = item_values[0]
            item_quantity = int(item_values[1])
            item_total_price = float(item_values[2][1:])  # Remove the dollar sign and convert to float

            # Update the total price
            self.total_price -= item_total_price
            self.total_label.config(text=f"Total: ฿{self.total_price:.2f}")

            # Remove the item from the order dictionary
            del self.order[item_name]

            # Remove the item from the treeview
            self.order_tree.delete(selected_item)

    def pay(self):
        payment_method = self.payment_method.get()
        if self.order:
            self.save_order_to_db()
            self.customer_count += 1
            self.update_customer_count_label()
            if payment_method == "QR Code":
                self.generate_qr_code()
            elif payment_method == "Cash":
                self.ask_cash_payment()
            else:
                self.complete_payment(payment_method)
        else:
            messagebox.showwarning("Payment", "No items in the order to pay for.")

    def ask_cash_payment(self):
        try:
            cash_payment_window = tk.Toplevel(self)
            cash_payment_window.title("Cash Payment")
            cash_payment_window.geometry("300x300")
            cash_payment_window.configure(bg="#f8f8f8")

            tk.Label(cash_payment_window, text="Enter amount paid:", font=("Consolas", 18), bg="#f8f8f8", fg="#333333").pack(pady=10)

            cash_amount_var = tk.DoubleVar()
            cash_entry = tk.Entry(cash_payment_window, textvariable=cash_amount_var, font=("Consolas", 18), justify="center")
            cash_entry.pack(pady=10)
            cash_entry.focus()

            def process_cash_payment():
                try:
                    amount_paid = cash_amount_var.get()
                    if amount_paid < self.total_price:
                        self.show_custom_messagebox("Insufficient Amount", "The amount paid is less than the total price.", "warning")
                    else:
                        change = amount_paid - self.total_price
                        self.show_custom_messagebox("Change", f"Total: ฿{self.total_price:.2f}\nPaid: ฿{amount_paid:.2f}\nChange: ฿{change:.2f}", "info")
                        self.complete_payment("Cash")
                        cash_payment_window.destroy()
                    
                except ValueError:
                    self.show_custom_messagebox("Invalid Input", "Please enter a valid amount.", "error")

            pay_button = tk.Button(cash_payment_window, text="Pay", command=process_cash_payment, bg="#27ae60", fg="#ffffff", font=("Consolas", 16, "bold"), bd=0, relief="flat")
            pay_button.pack(pady=10, ipadx=10, ipady=5)

        except Exception as e:
            self.show_custom_messagebox("Payment Error", f"Error processing cash payment: {e}", "error")


    def show_custom_messagebox(self, title, message, type):
        custom_window = tk.Toplevel(self)
        custom_window.title(title)
        custom_window.geometry("300x200")
        custom_window.configure(bg="#f8f8f8")

        font_style = ("Consolas", 12)

        tk.Label(custom_window, text=title, font=("Consolas", 14, "bold"), bg="#f8f8f8", fg="#333333").pack(pady=10)
        tk.Label(custom_window, text=message, font=font_style, bg="#f8f8f8", fg="#333333").pack(pady=10)

        button_text = "OK"
        if type == "info":
            button_color = "#27ae60"
        elif type == "warning":
            button_color = "#e74c3c"
            button_text = "OK"
        elif type == "error":
            button_color = "#e74c3c"
            button_text = "OK"

        tk.Button(custom_window, text=button_text, command=custom_window.destroy, bg=button_color, fg="#ffffff", font=("Consolas", 12, "bold"), bd=0, relief="flat").pack(pady=10, ipadx=10, ipady=5)



    def generate_qr_code(self):
        try:
            id_or_phone_number = "0951847769"
            payload_with_amount = qrcode.generate_payload(id_or_phone_number, self.total_price)
            img = qrcode.to_image(payload_with_amount)

            img_byte_arr = io.BytesIO()
            img.save(img_byte_arr, format='PNG')
            img_byte_arr = img_byte_arr.getvalue()

            self.qr_img = ImageTk.PhotoImage(Image.open(io.BytesIO(img_byte_arr)))

            qr_window = tk.Toplevel(self)
            qr_window.title("QR Code Payment")
            qr_window.geometry("400x700")
            qr_window.configure(bg="#2c3e50")

            qr_label = tk.Label(qr_window, image=self.qr_img, bg="#2c3e50")
            qr_label.pack(pady=20)

            tk.Label(qr_window, text=f"Scan to Pay ฿{self.total_price:.2f}", font=("Consolas", 14), bg="#2c3e50", fg="#ecf0f1").pack(pady=10)

            close_button = tk.Button(qr_window, text="Close", command=qr_window.destroy, bg="#e74c3c", fg="#ffffff", font=("Consolas", 12, "bold"), bd=0, relief="flat")
            close_button.pack(pady=10, ipadx=10, ipady=5)

            self.reset_order()
        except Exception as e:
            messagebox.showerror("QR Code Error", f"Error generating QR code: {e}")


    def complete_payment(self, payment_method):
        self.reset_order()
        messagebox.showinfo("Payment", f"Payment successful using {payment_method}!")

    def reset_order(self):
        for row in self.order_tree.get_children():
            self.order_tree.delete(row)
        self.total_label.config(text="Total: ฿0.00")
        self.order = {}
        self.total_price = 0.0

    def save_order_to_db(self):
        cursor = self.conn.cursor()
        current_date = datetime.now().strftime("%d-%m-%Y")
        current_time = datetime.now().strftime("%H:%M:%S")
        for item, details in self.order.items():
            cursor.execute("""
                INSERT INTO orders (customer_id, item_name, quantity, price, order_date, order_time) 
                VALUES (?, ?, ?, ?, ?, ?)
            """, (self.customer_count, item, details["quantity"], details["total_price"], current_date, current_time))
            print(f"Saved order to DB: {self.customer_count}, {item}, {details['quantity']}, {details['total_price']}, {current_date}, {current_time}")
        self.conn.commit()

    def show_past_orders(self):
        past_orders_window = tk.Toplevel(self)
        past_orders_window.title("Past Orders")
        past_orders_window.geometry("700x500")
        past_orders_window.configure(bg="#f8f8f8")

        # Create combobox to select past customers
        tk.Label(past_orders_window, text="Select Customer ID:", font=("Consolas", 12), bg="#f8f8f8", fg="#333333").pack(pady=10)
        self.customer_select = ttk.Combobox(past_orders_window, style="TCombobox")
        self.customer_select.pack(pady=10)

        # Create calendar to select date
        tk.Label(past_orders_window, text="Select Date:", font=("Consolas", 12), bg="#f8f8f8", fg="#333333").pack(pady=10)
        self.calendar = Calendar(past_orders_window, date_pattern="dd-mm-yyyy")
        self.calendar.pack(pady=10)

        # Create Treeview to display past orders
        tree = ttk.Treeview(past_orders_window, columns=("Customer ID", "Item", "Quantity", "Price", "Date", "Time"), show='headings', style="Treeview")
        tree.heading("Customer ID", text="Customer ID")
        tree.heading("Item", text="Item")
        tree.heading("Quantity", text="Quantity")
        tree.heading("Price", text="Price")
        tree.heading("Date", text="Date")
        tree.heading("Time", text="Time")

        tree.column("Customer ID", width=100)
        tree.column("Item", width=150)
        tree.column("Quantity", width=100)
        tree.column("Price", width=100)
        tree.column("Date", width=100)
        tree.column("Time", width=100)

        tree.pack(fill=tk.BOTH, expand=True)

        # Populate the combobox with distinct customer IDs
        cursor = self.conn.cursor()
        cursor.execute("SELECT DISTINCT customer_id FROM orders")
        customer_ids = [row[0] for row in cursor.fetchall()]
        self.customer_select['values'] = customer_ids

        # Bind combobox and calendar selection to a method that updates the Treeview
        self.customer_select.bind("<<ComboboxSelected>>", lambda event: self.update_past_orders(tree))
        self.calendar.bind("<<CalendarSelected>>", lambda event: self.update_past_orders(tree))

    def update_past_orders(self, tree):
        selected_customer = self.customer_select.get()
        selected_date = self.calendar.get_date()

        query = "SELECT customer_id, item_name, quantity, price, order_date, order_time FROM orders WHERE 1=1"
        params = []

        if selected_customer:
            query += " AND customer_id = ?"
            params.append(selected_customer)

        if selected_date:
            query += " AND order_date = ?"
            params.append(selected_date)

        cursor = self.conn.cursor()
        cursor.execute(query, tuple(params))
        rows = cursor.fetchall()
        print(f"Fetched rows for customer {selected_customer} and date {selected_date}: {rows}")  # Debug statement

        # Clear the Treeview
        for row in tree.get_children():
            tree.delete(row)

        # Insert new rows
        for row in rows:
            tree.insert("", tk.END, values=row)

    def show_report_calendar(self):
        report_calendar_window = tk.Toplevel(self)
        report_calendar_window.title("Select Date for Report")
        report_calendar_window.geometry("400x400")
        report_calendar_window.configure(bg="#f8f8f8")

        tk.Label(report_calendar_window, text="Select Date:", font=("Consolas", 12), bg="#f8f8f8", fg="#333333").pack(pady=10)
        self.report_calendar = Calendar(report_calendar_window, date_pattern="dd-mm-yyyy")
        self.report_calendar.pack(pady=10)

        tk.Button(report_calendar_window, text="Generate Report", command=self.generate_sales_report, bg="#8e44ad", fg="#ffffff", font=("Consolas", 12, "bold"), bd=0, relief="flat").pack(pady=10)

    def create_order_summary_frame(self):
        summary_frame = ttk.Frame(self, style="TFrame")
        summary_frame.grid(row=0, column=1, padx=20, pady=20, sticky="ne")

        tk.Label(summary_frame, text="Current Order", font=("Consolas", 16, "bold"), bg="#f8f8f8", fg="#333333").grid(row=0, column=0, pady=10)

        self.order_tree = ttk.Treeview(summary_frame, columns=("Item", "Quantity", "Price"), show='headings', style="Treeview")
        self.order_tree.heading("Item", text="Item")
        self.order_tree.heading("Quantity", text="Quantity")
        self.order_tree.heading("Price", text="Price")

        self.order_tree.column("Item", width=150)
        self.order_tree.column("Quantity", width=100)
        self.order_tree.column("Price", width=100)

        self.order_tree.grid(row=1, column=0, padx=10, pady=10)

        self.total_label = ttk.Label(summary_frame, text="Total: ฿0.00", font=("Consolas", 14, "bold"), style="TLabel")
        self.total_label.grid(row=2, column=0, padx=10, pady=10)

        self.delete_button = tk.Button(summary_frame, text="Delete Selected Item", command=self.delete_selected_item, bg="#e74c3c", fg="#ffffff", font=("Consolas", 12, "bold"), bd=0, relief="flat")
        self.delete_button.grid(row=3, column=0, padx=10, pady=10, ipadx=10, ipady=5)

        self.payment_method_label = ttk.Label(summary_frame, text="Select Payment Method:", style="TLabel")
        self.payment_method_label.grid(row=4, column=0, padx=10, pady=5)

        self.payment_method = ttk.Combobox(summary_frame, values=["Cash", "QR Code", "True Money Wallet"], style="TCombobox")
        self.payment_method.grid(row=5, column=0, padx=10, pady=5)
        self.payment_method.current(0)  # Set default to "Cash"

        self.pay_button = tk.Button(summary_frame, text="Pay", command=self.pay, bg="#27ae60", fg="#ffffff", font=("Consolas", 12, "bold"), bd=0, relief="flat")
        self.pay_button.grid(row=6, column=0, padx=10, pady=10, ipadx=10, ipady=5)

        self.customer_count_label = ttk.Label(summary_frame, text="Customer Count: 0", font=("Consolas", 14, "bold"), style="TLabel")
        self.customer_count_label.grid(row=7, column=0, padx=10, pady=10)

        self.past_orders_button = tk.Button(summary_frame, text="Check Orders", command=self.show_past_orders, bg="#3498db", fg="#ffffff", font=("Consolas", 12, "bold"), bd=0, relief="flat")
        self.past_orders_button.grid(row=8, column=0, padx=10, pady=10, ipadx=10, ipady=5)

        self.report_button = tk.Button(summary_frame, text="Show Sales Report", command=self.show_report_calendar, bg="#8e44ad", fg="#ffffff", font=("Consolas", 12, "bold"), bd=0, relief="flat")
        self.report_button.grid(row=9, column=0, padx=10, pady=10, ipadx=10, ipady=5)

        self.weekly_report_button = tk.Button(summary_frame, text="Show Weekly Sales Report", command=self.generate_weekly_sales_report, bg="#8e44ad", fg="#ffffff", font=("Consolas", 12, "bold"), bd=0, relief="flat")
        self.weekly_report_button.grid(row=10, column=0, padx=10, pady=10, ipadx=10, ipady=5)


    def generate_sales_report(self):
        selected_date = self.report_calendar.get_date()
        try:
            cursor = self.conn.cursor()

            # Total sales for the selected day
            cursor.execute("SELECT SUM(price) FROM orders WHERE order_date = ?", (selected_date,))
            total_sales = cursor.fetchone()[0] or 0

            # Popular products for the selected day
            cursor.execute("SELECT item_name, SUM(quantity) FROM orders WHERE order_date = ? GROUP BY item_name ORDER BY SUM(quantity) DESC", (selected_date,))
            popular_products = cursor.fetchall()

            # Sales over time for the selected day
            cursor.execute("SELECT order_time, SUM(price) FROM orders WHERE order_date = ? GROUP BY order_time ORDER BY order_time", (selected_date,))
            sales_over_time = cursor.fetchall()

            report_window = tk.Toplevel(self)
            report_window.title("Sales Report")
            report_window.geometry("1240x1050")
            report_window.configure(bg="#f8f8f8")

            tk.Label(report_window, text=f"Total Sales on {selected_date}: ฿{total_sales:.2f}", font=("Consolas", 18, "bold"), bg="#f8f8f8", fg="#333333").pack(pady=10)

            popular_products_frame = ttk.Frame(report_window, style="TFrame")
            popular_products_frame.pack(pady=10)

            # Create Treeview for popular products
            popular_products_tree = ttk.Treeview(popular_products_frame, columns=("Item", "Quantity"), show='headings', style="Treeview")
            popular_products_tree.heading("Item", text="Item")
            popular_products_tree.heading("Quantity", text="Quantity Sold")

            popular_products_tree.column("Item", width=200)
            popular_products_tree.column("Quantity", width=150)

            for product in popular_products:
                popular_products_tree.insert("", tk.END, values=(product[0], product[1]))

            popular_products_tree.pack()

            # Sales Over Time Chart
            try:
                if sales_over_time:
                    times = [datetime.strptime(f"{selected_date} {time}", "%d-%m-%Y %H:%M:%S") for time, _ in sales_over_time]
                    times = mdates.date2num(times)
                    sales = [sale for _, sale in sales_over_time]

                    fig_daily, ax_daily = plt.subplots(figsize=(12, 6))
                    bar_width = 0.03

                    norm = plt.Normalize(min(sales), max(sales))
                    colors = plt.cm.Reds(norm(sales))

                    bars = ax_daily.bar(times, sales, width=bar_width, color=colors, edgecolor='black')

                    ax_daily.set_title(f'Sales Over Time on {selected_date}', fontsize=20, fontweight='bold')
                    ax_daily.set_xlabel('Time', fontsize=16)
                    ax_daily.set_ylabel('Total Sales (฿)', fontsize=16)
                    ax_daily.xaxis.set_major_formatter(mdates.DateFormatter('%H:%M'))
                    ax_daily.xaxis.set_major_locator(mdates.HourLocator(interval=1))
                    fig_daily.autofmt_xdate()

                    for bar, sale in zip(bars, sales):
                        height = bar.get_height()
                        ax_daily.annotate(f'{sale:.2f}', xy=(bar.get_x() + bar.get_width() / 2, height),
                                        xytext=(0, 3), textcoords="offset points", ha='center', va='bottom', fontsize=10, color='black')

                    fig_daily.tight_layout()
                    canvas_daily = plt.gcf().canvas
                    canvas_daily.draw()

                    buf_daily = canvas_daily.buffer_rgba()
                    graph_image_daily = Image.frombuffer('RGBA', canvas_daily.get_width_height(), buf_daily, 'raw', 'RGBA', 0, 1)
                    graph_image_tk_daily = ImageTk.PhotoImage(graph_image_daily)

                    graph_label_daily = tk.Label(report_window, image=graph_image_tk_daily)
                    graph_label_daily.image = graph_image_tk_daily
                    graph_label_daily.pack(pady=10)
                else:
                    tk.Label(report_window, text="No sales data available for the selected day.", font=("Consolas", 14), bg="#f8f8f8", fg="#333333").pack(pady=10)

            except Exception as e:
                messagebox.showerror("Plotting Error", f"Error generating graph: {e}")

            report_window.mainloop()
        except sqlite3.Error as e:
            messagebox.showerror("Database Error", f"Error generating sales report: {e}")
        except Exception as e:
            messagebox.showerror("Report Error", f"Error generating report: {e}")

    def generate_weekly_sales_report(self):
        try:
            cursor = self.conn.cursor()

            # Get the current date
            today = datetime.today()
            # Calculate the start of the week (Monday)
            start_of_week = today - timedelta(days=today.weekday())
            end_of_week = start_of_week + timedelta(days=6)

            # Convert dates to string format for querying
            start_of_week_str = start_of_week.strftime("%d-%m-%Y")
            end_of_week_str = end_of_week.strftime("%d-%m-%Y")

            # Get sales data for the week
            cursor.execute("""
                SELECT order_date, SUM(price)
                FROM orders
                WHERE order_date BETWEEN ? AND ?
                GROUP BY order_date
                ORDER BY order_date
            """, (start_of_week_str, end_of_week_str))
            weekly_sales = cursor.fetchall()

            if not weekly_sales:
                messagebox.showinfo("No Data", "No sales data available for the current week.")
                return

            # Prepare data for plotting
            days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
            sales_by_day = {day: 0 for day in days}

            for date_str, sales in weekly_sales:
                date_obj = datetime.strptime(date_str, "%d-%m-%Y")
                day_name = date_obj.strftime('%a')
                sales_by_day[day_name] = sales

            report_window = tk.Toplevel(self)
            report_window.title("Weekly Sales Report")
            report_window.geometry("1212x710")
            report_window.configure(bg="#f8f8f8")

            tk.Label(report_window, text=f"Total Sales for the Week Starting {start_of_week_str}", font=("Consolas", 18, "bold"), bg="#f8f8f8", fg="#333333").pack(pady=10)

            # Weekly Sales Line Chart
            try:
                fig_weekly, ax_weekly = plt.subplots(figsize=(12, 6))

                ax_weekly.plot(days, list(sales_by_day.values()), marker='o', linestyle='-', color='b')

                ax_weekly.set_title('Total Sales for the Week', fontsize=20, fontweight='bold')
                ax_weekly.set_xlabel('Day', fontsize=16)
                ax_weekly.set_ylabel('Total Sales (฿)', fontsize=16)
                ax_weekly.grid(True)

                for i, sale in enumerate(sales_by_day.values()):
                    ax_weekly.text(i, sale, f'{sale:.2f}', ha='center', va='bottom', fontsize=10)

                fig_weekly.tight_layout()
                canvas_weekly = plt.gcf().canvas
                canvas_weekly.draw()

                buf_weekly = canvas_weekly.buffer_rgba()
                graph_image_weekly = Image.frombuffer('RGBA', canvas_weekly.get_width_height(), buf_weekly, 'raw', 'RGBA', 0, 1)
                graph_image_tk_weekly = ImageTk.PhotoImage(graph_image_weekly)

                graph_label_weekly = tk.Label(report_window, image=graph_image_tk_weekly)
                graph_label_weekly.image = graph_image_tk_weekly
                graph_label_weekly.pack(pady=10)

            except Exception as e:
                messagebox.showerror("Plotting Error", f"Error generating weekly sales graph: {e}")

            report_window.mainloop()
        except sqlite3.Error as e:
            messagebox.showerror("Database Error", f"Error generating weekly sales report: {e}")
        except Exception as e:
            messagebox.showerror("Report Error", f"Error generating report: {e}")




if __name__ == "__main__":
    app = CoffeeShopPOS()
    app.mainloop()
