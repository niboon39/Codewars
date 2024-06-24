import tkinter as tk
from tkinter import messagebox, ttk
from tkcalendar import DateEntry
import sqlite3
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import datetime

class BankAccountApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Bank Account Manager")
        self.root.geometry("1000x800")
        self.root.configure(bg="#f0f0f0")

        # Connect to SQLite database
        self.conn = sqlite3.connect('bank_account.db')
        self.create_tables()

        # Account Balance
        self.balance_label = tk.Label(root, text="Account Balance: ฿0.00", font=("Arial", 18), bg="#f0f0f0")
        self.balance_label.grid(row=0, column=0, columnspan=4, pady=10)

        # Deposit Section
        self.deposit_frame = tk.LabelFrame(root, text="Deposit", padx=10, pady=10, bg="#f0f0f0")
        self.deposit_frame.grid(row=1, column=0, padx=10, pady=10, sticky="ew")

        self.deposit_label = tk.Label(self.deposit_frame, text="Deposit Amount:", bg="#f0f0f0")
        self.deposit_label.grid(row=0, column=0, padx=5, pady=5, sticky="e")

        self.deposit_entry = tk.Entry(self.deposit_frame)
        self.deposit_entry.grid(row=0, column=1, padx=5, pady=5, sticky="w")

        self.deposit_button = tk.Button(self.deposit_frame, text="Deposit", command=self.deposit_money, bg="#4caf50", fg="white")
        self.deposit_button.grid(row=1, column=0, columnspan=2, pady=5)

        # Withdraw Section
        self.withdraw_frame = tk.LabelFrame(root, text="Withdraw", padx=10, pady=10, bg="#f0f0f0")
        self.withdraw_frame.grid(row=1, column=1, padx=10, pady=10, sticky="ew")

        self.withdraw_label = tk.Label(self.withdraw_frame, text="Withdraw Amount:", bg="#f0f0f0")
        self.withdraw_label.grid(row=0, column=0, padx=5, pady=5, sticky="e")

        self.withdraw_entry = tk.Entry(self.withdraw_frame)
        self.withdraw_entry.grid(row=0, column=1, padx=5, pady=5, sticky="w")

        self.withdraw_button = tk.Button(self.withdraw_frame, text="Withdraw", command=self.withdraw_money, bg="#f44336", fg="white")
        self.withdraw_button.grid(row=1, column=0, columnspan=2, pady=5)

        # Upcoming Bills Section
        self.upcoming_bills_frame = tk.LabelFrame(root, text="Upcoming Bills", padx=10, pady=10, bg="#f0f0f0")
        self.upcoming_bills_frame.grid(row=2, column=0, columnspan=2, padx=10, pady=10, sticky="ew")

        self.bill_name_label = tk.Label(self.upcoming_bills_frame, text="Bill Name:", bg="#f0f0f0")
        self.bill_name_label.grid(row=0, column=0, padx=5, pady=5, sticky="e")

        self.bill_name_entry = tk.Entry(self.upcoming_bills_frame)
        self.bill_name_entry.grid(row=0, column=1, padx=5, pady=5, sticky="w")

        self.bill_amount_label = tk.Label(self.upcoming_bills_frame, text="Bill Amount:", bg="#f0f0f0")
        self.bill_amount_label.grid(row=1, column=0, padx=5, pady=5, sticky="e")

        self.bill_amount_entry = tk.Entry(self.upcoming_bills_frame)
        self.bill_amount_entry.grid(row=1, column=1, padx=5, pady=5, sticky="w")

        self.due_date_label = tk.Label(self.upcoming_bills_frame, text="Due Date:", bg="#f0f0f0")
        self.due_date_label.grid(row=2, column=0, padx=5, pady=5, sticky="e")

        self.due_date_entry = DateEntry(self.upcoming_bills_frame, date_pattern='yyyy-mm-dd')
        self.due_date_entry.grid(row=2, column=1, padx=5, pady=5, sticky="w")

        self.add_bill_button = tk.Button(self.upcoming_bills_frame, text="Add Bill", command=self.add_upcoming_bill, bg="#2196f3", fg="white")
        self.add_bill_button.grid(row=3, column=0, columnspan=2, pady=5)

        self.upcoming_bills_listbox = tk.Listbox(self.upcoming_bills_frame, height=10, width=70)
        self.upcoming_bills_listbox.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

        self.pay_bill_button = tk.Button(self.upcoming_bills_frame, text="Pay Bill", command=self.pay_bill, bg="#ff9800", fg="white")
        self.pay_bill_button.grid(row=5, column=0, columnspan=2, pady=5)

        self.total_upcoming_label = tk.Label(self.upcoming_bills_frame, text="Total Upcoming Bills: ฿0.00", bg="#f0f0f0")
        self.total_upcoming_label.grid(row=6, column=0, columnspan=2, pady=5)

        # Transaction History Section
        self.history_frame = tk.LabelFrame(root, text="Transaction History", padx=10, pady=10, bg="#f0f0f0")
        self.history_frame.grid(row=3, column=0, columnspan=3, padx=10, pady=10, sticky="ew")

        self.day_var_hist = tk.StringVar()
        self.day_combobox_hist = ttk.Combobox(self.history_frame, textvariable=self.day_var_hist, width=5)
        self.day_combobox_hist['values'] = [f"{day:02d}" for day in range(1, 32)]
        self.day_combobox_hist.grid(row=0, column=0, padx=5, pady=5)
        self.day_combobox_hist.bind('<<ComboboxSelected>>', self.update_history)

        self.month_var_hist = tk.StringVar()
        self.month_combobox_hist = ttk.Combobox(self.history_frame, textvariable=self.month_var_hist, width=10)
        self.month_combobox_hist['values'] = [
            "January", "February", "March", "April", "May", "June",
            "July", "August", "September", "October", "November", "December"
        ]
        self.month_combobox_hist.grid(row=0, column=1, padx=5, pady=5)
        self.month_combobox_hist.bind('<<ComboboxSelected>>', self.update_history)

        self.year_var_hist = tk.StringVar()
        self.year_combobox_hist = ttk.Combobox(self.history_frame, textvariable=self.year_var_hist, width=7)
        self.year_combobox_hist['values'] = [str(year) for year in range(2000, datetime.datetime.now().year + 1)]
        self.year_combobox_hist.grid(row=0, column=2, padx=5, pady=5)
        self.year_combobox_hist.bind('<<ComboboxSelected>>', self.update_history)

        self.history_listbox = tk.Listbox(self.history_frame, height=15, width=100)
        self.history_listbox.grid(row=1, column=0, columnspan=3, padx=5, pady=5)

        # Overview Section
        self.overview_frame = tk.LabelFrame(root, text="Overview", padx=10, pady=10, bg="#f0f0f0")
        self.overview_frame.grid(row=1, column=2, rowspan=2, padx=10, pady=10, sticky="nsew")

        self.total_income_label = tk.Label(self.overview_frame, text="Total Income (Baht): 0.00", font=("Arial", 12), bg="#f0f0f0")
        self.total_income_label.grid(row=0, column=0, pady=5, sticky="w")

        self.total_expenses_label = tk.Label(self.overview_frame, text="Total Expenses (Baht): 0.00", font=("Arial", 12), bg="#f0f0f0")
        self.total_expenses_label.grid(row=1, column=0, pady=5, sticky="w")

        self.income_transactions_label = tk.Label(self.overview_frame, text="Transactions (Income): 0", font=("Arial", 12), bg="#f0f0f0")
        self.income_transactions_label.grid(row=2, column=0, pady=5, sticky="w")

        self.expense_transactions_label = tk.Label(self.overview_frame, text="Transactions (Expenses): 0", font=("Arial", 12), bg="#f0f0f0")
        self.expense_transactions_label.grid(row=3, column=0, pady=5, sticky="w")

        self.average_income_label = tk.Label(self.overview_frame, text="Average Income/Month: 0.00", font=("Arial", 12), bg="#f0f0f0")
        self.average_income_label.grid(row=4, column=0, pady=5, sticky="w")

        self.average_expenses_label = tk.Label(self.overview_frame, text="Average Expenses/Month: 0.00", font=("Arial", 12), bg="#f0f0f0")
        self.average_expenses_label.grid(row=5, column=0, pady=5, sticky="w")

        # Graph inside Overview Frame
        self.figure_overview = plt.Figure(figsize=(5.5, 2.5), dpi=100)
        self.ax_overview = self.figure_overview.add_subplot(111)
        self.canvas_overview = FigureCanvasTkAgg(self.figure_overview, self.overview_frame)
        self.canvas_overview.get_tk_widget().grid(row=6, column=0, padx=5, pady=5)

        self.update_balance()

        # Check for upcoming due dates
        self.check_due_dates()

    def create_tables(self):
        cursor = self.conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS transactions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                type TEXT,
                amount REAL,
                balance REAL,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS upcoming_bills (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                amount REAL,
                due_date DATE DEFAULT CURRENT_DATE
            )
        ''')
        self.conn.commit()

    def update_balance(self):
        cursor = self.conn.cursor()
        cursor.execute('SELECT balance FROM transactions ORDER BY id DESC LIMIT 1')
        result = cursor.fetchone()
        balance = result[0] if result else 0.00
        self.balance_label.config(text=f"Account Balance: ฿{balance:.2f}")
        self.update_history()
        self.update_upcoming_bills()
        self.update_overview()

    def update_history(self, event=None):
        self.history_listbox.delete(0, tk.END)
        cursor = self.conn.cursor()

        query = 'SELECT type, amount, balance, timestamp FROM transactions WHERE 1=1'
        params = []

        day = self.day_var_hist.get()
        if day:
            query += ' AND strftime("%d", timestamp) = ?'
            params.append(day)

        month = self.month_var_hist.get()
        if month:
            month_number = self.get_month_number(month)
            query += ' AND strftime("%m", timestamp) = ?'
            params.append(month_number)

        year = self.year_var_hist.get()
        if year:
            query += ' AND strftime("%Y", timestamp) = ?'
            params.append(year)

        query += ' ORDER BY id DESC'
        cursor.execute(query, params)
        transactions = cursor.fetchall()

        for transaction in transactions:
            self.history_listbox.insert(tk.END, f"{transaction[3]} - {transaction[0]}: ฿{transaction[1]:.2f} (Balance: ฿{transaction[2]:.2f})")

        self.update_overview()  # Update the overview based on the filtered transactions

    def get_month_number(self, month_name):
        datetime_object = datetime.datetime.strptime(month_name, "%B")
        month_number = datetime_object.month
        return f"{month_number:02d}"

    def update_upcoming_bills(self):
        self.upcoming_bills_listbox.delete(0, tk.END)
        cursor = self.conn.cursor()
        cursor.execute('SELECT id, name, amount, due_date FROM upcoming_bills ORDER BY due_date')
        bills = cursor.fetchall()
        total_upcoming = 0.0
        for bill in bills:
            due_date = datetime.datetime.strptime(bill[3], "%Y-%m-%d").date()
            if due_date < datetime.date.today():
                self.upcoming_bills_listbox.insert(tk.END, f"{bill[0]} - {bill[3]} - {bill[1]}: ฿{bill[2]:.2f}")
                self.upcoming_bills_listbox.itemconfig(tk.END, {'bg':'#ffcccc'})
            else:
                self.upcoming_bills_listbox.insert(tk.END, f"{bill[0]} - {bill[3]} - {bill[1]}: ฿{bill[2]:.2f}")
            total_upcoming += bill[2]
        self.total_upcoming_label.config(text=f"Total Upcoming Bills: ฿{total_upcoming:.2f}")

    def deposit_money(self):
        amount = float(self.deposit_entry.get())
        self.record_transaction("Deposit", amount)
        self.deposit_entry.delete(0, tk.END)
        self.update_balance()

    def withdraw_money(self):
        amount = float(self.withdraw_entry.get())
        self.record_transaction("Withdraw", -amount)
        self.withdraw_entry.delete(0, tk.END)
        self.update_balance()

    def record_transaction(self, transaction_type, amount):
        cursor = self.conn.cursor()
        cursor.execute('SELECT balance FROM transactions ORDER BY id DESC LIMIT 1')
        result = cursor.fetchone()
        balance = result[0] if result else 0.00
        new_balance = balance + amount
        cursor.execute('INSERT INTO transactions (type, amount, balance) VALUES (?, ?, ?)', (transaction_type, amount, new_balance))
        self.conn.commit()

    def add_upcoming_bill(self):
        name = self.bill_name_entry.get()
        amount = float(self.bill_amount_entry.get())
        due_date = self.due_date_entry.get()
        cursor = self.conn.cursor()
        cursor.execute('INSERT INTO upcoming_bills (name, amount, due_date) VALUES (?, ?, ?)', (name, amount, due_date))
        self.conn.commit()
        self.bill_name_entry.delete(0, tk.END)
        self.bill_amount_entry.delete(0, tk.END)
        self.due_date_entry.set_date(datetime.datetime.now())
        self.update_upcoming_bills()

    def pay_bill(self):
        selected_bill_index = self.upcoming_bills_listbox.curselection()
        if not selected_bill_index:
            messagebox.showwarning("Select Bill", "Please select a bill to pay.")
            return
        bill_text = self.upcoming_bills_listbox.get(selected_bill_index)
        bill_id = int(bill_text.split()[0])
        cursor = self.conn.cursor()
        cursor.execute('SELECT amount FROM upcoming_bills WHERE id = ?', (bill_id,))
        amount = cursor.fetchone()[0]
        
        # Check if balance is sufficient
        cursor.execute('SELECT balance FROM transactions ORDER BY id DESC LIMIT 1')
        result = cursor.fetchone()
        balance = result[0] if result else 0.00
        if balance < amount:
            messagebox.showerror("Payment Declined", "Insufficient balance to pay the bill.")
            return

        # Process payment if balance is sufficient
        cursor.execute('DELETE FROM upcoming_bills WHERE id = ?', (bill_id,))
        self.conn.commit()
        self.record_transaction("Bill Payment", -amount)
        self.update_balance()

    def predict_income(self):
        cursor = self.conn.cursor()
        cursor.execute('SELECT amount FROM transactions WHERE type = "Deposit"')
        deposits = cursor.fetchall()
        if deposits:
            dates = range(1, len(deposits) + 1)
            amounts = [d[0] for d in deposits]
            average_income = sum(amounts) / len(amounts)
            self.show_graph(dates, amounts, "Income Prediction", "Income", average_income)
        else:
            messagebox.showinfo("Predicted Income", "No income data available to predict.")

    def predict_disbursement(self):
        cursor = self.conn.cursor()
        cursor.execute('SELECT amount FROM transactions WHERE type = "Withdraw" OR type = "Bill Payment"')
        disbursements = cursor.fetchall()
        if disbursements:
            dates = range(1, len(disbursements) + 1)
            amounts = [d[0] for d in disbursements]
            average_disbursement = sum(amounts) / len(amounts)
            self.show_graph(dates, amounts, "Disbursement Prediction", "Disbursement", average_disbursement)
        else:
            messagebox.showinfo("Predicted Disbursement", "No disbursement data available to predict.")

    def show_graph(self, dates, amounts, title, ylabel, average):
        self.ax.clear()
        self.ax.plot(dates, amounts, label='Actual', marker='o')
        self.ax.axhline(y=average, color='r', linestyle='--', label=f'Average: {average:.2f}')
        self.ax.set_title(title)
        self.ax.set_xlabel('Transactions')
        self.ax.set_ylabel(ylabel)
        self.ax.grid(True)
        self.ax.legend()
        self.canvas.draw()

    def update_overview(self):
        cursor = self.conn.cursor()

        # Calculate total income, total expenses, number of transactions, and averages
        query = 'SELECT SUM(amount), COUNT(*) FROM transactions WHERE type = "Deposit"'
        params = []

        day = self.day_var_hist.get()
        if day:
            query += ' AND strftime("%d", timestamp) = ?'
            params.append(day)

        month = self.month_var_hist.get()
        if month:
            month_number = self.get_month_number(month)
            query += ' AND strftime("%m", timestamp) = ?'
            params.append(month_number)

        year = self.year_var_hist.get()
        if year:
            query += ' AND strftime("%Y", timestamp) = ?'
            params.append(year)

        cursor.execute(query, params)
        total_income, income_transactions = cursor.fetchone()
        total_income = total_income or 0.00
        income_transactions = income_transactions or 0

        query = 'SELECT SUM(amount), COUNT(*) FROM transactions WHERE type IN ("Withdraw", "Bill Payment")'
        params = []

        if day:
            query += ' AND strftime("%d", timestamp) = ?'
            params.append(day)

        if month:
            month_number = self.get_month_number(month)
            query += ' AND strftime("%m", timestamp) = ?'
            params.append(month_number)

        if year:
            query += ' AND strftime("%Y", timestamp) = ?'
            params.append(year)

        cursor.execute(query, params)
        total_expenses, expense_transactions = cursor.fetchone()
        total_expenses = total_expenses or 0.00
        expense_transactions = expense_transactions or 0

        current_year = datetime.datetime.now().year
        cursor.execute('SELECT COUNT(DISTINCT strftime("%m", timestamp)) FROM transactions WHERE type = "Deposit" AND strftime("%Y", timestamp) = ?', (current_year,))
        months_with_income = cursor.fetchone()[0] or 1  # Avoid division by zero

        cursor.execute('SELECT COUNT(DISTINCT strftime("%m", timestamp)) FROM transactions WHERE type IN ("Withdraw", "Bill Payment") AND strftime("%Y", timestamp) = ?', (current_year,))
        months_with_expenses = cursor.fetchone()[0] or 1  # Avoid division by zero

        average_income = total_income / months_with_income
        average_expenses = total_expenses / months_with_expenses

        # Update overview labels
        self.total_income_label.config(text=f"Total Income (Baht): {total_income:.2f}")
        self.total_expenses_label.config(text=f"Total Expenses (Baht): {total_expenses:.2f}")
        self.income_transactions_label.config(text=f"Transactions (Income): {income_transactions}")
        self.expense_transactions_label.config(text=f"Transactions (Expenses): {expense_transactions}")
        self.average_income_label.config(text=f"Average Income/Month: {average_income:.2f}")
        self.average_expenses_label.config(text=f"Average Expenses/Month: {average_expenses:.2f}")

        # Update bar chart
        self.update_bar_chart()

    def update_bar_chart(self):
        cursor = self.conn.cursor()

        query = '''
            SELECT strftime("%Y-%m", timestamp) AS month, 
            SUM(CASE WHEN type = "Deposit" THEN amount ELSE 0 END) AS income,
            SUM(CASE WHEN type IN ("Withdraw", "Bill Payment") THEN amount ELSE 0 END) AS expenses
            FROM transactions
            WHERE 1=1
        '''
        params = []

        day = self.day_var_hist.get()
        if day:
            query += ' AND strftime("%d", timestamp) = ?'
            params.append(day)

        month = self.month_var_hist.get()
        if month:
            month_number = self.get_month_number(month)
            query += ' AND strftime("%m", timestamp) = ?'
            params.append(month_number)

        year = self.year_var_hist.get()
        if year:
            query += ' AND strftime("%Y", timestamp) = ?'
            params.append(year)

        query += ' GROUP BY month ORDER BY month'
        cursor.execute(query, params)

        data = cursor.fetchall()

        months = [datetime.datetime.strptime(d[0], "%Y-%m").strftime("%b %y") for d in data]
        income = [d[1] for d in data]
        expenses = [d[2] for d in data]

        self.ax_overview.clear()
        bar_width = 0.35
        index = range(len(months))

        self.ax_overview.bar(index, income, bar_width, label='Income', color='#4caf50')
        self.ax_overview.bar([i + bar_width for i in index], expenses, bar_width, label='Expenses', color='#f44336')

        self.ax_overview.set_title('Monthly Income and Expenses')
        self.ax_overview.set_xlabel('Month')
        self.ax_overview.set_ylabel('Amount (Baht)')
        self.ax_overview.set_xticks([i + bar_width / 2 for i in index])
        self.ax_overview.set_xticklabels(months)
        self.ax_overview.legend()
        self.ax_overview.grid(True)
        self.canvas_overview.draw()

    def check_due_dates(self):
        cursor = self.conn.cursor()
        cursor.execute('SELECT name, due_date FROM upcoming_bills')
        bills = cursor.fetchall()
        today = datetime.date.today()
        alert_days = 3  # Number of days before the due date to alert
        for bill in bills:
            due_date = datetime.datetime.strptime(bill[1], "%Y-%m-%d").date()
            days_left = (due_date - today).days
            if days_left <= alert_days:
                messagebox.showwarning("Upcoming Bill Due", f"The bill '{bill[0]}' is due in {days_left} days.")
        # Schedule the next check
        self.root.after(86400000, self.check_due_dates)  # Check every 24 hours (86400000 milliseconds)

# Create main window
root = tk.Tk()
app = BankAccountApp(root)

# Start the GUI event loop
root.mainloop()
