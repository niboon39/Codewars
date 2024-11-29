import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from PIL import Image, ImageOps, ImageEnhance, ImageTk
import pytesseract
import re

# Set path to Tesseract executable if necessary (update for your system)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'

def update_image():
    """Update the image based on the user-adjusted parameters, display it, and update the split calculation."""
    try:
        if not current_image:
            return

        # Retrieve slider values
        contrast_factor = contrast_slider.get()
        threshold_value = threshold_slider.get()
        resize_factor = resize_slider.get() / 100

        # Convert to grayscale
        grayscale_image = ImageOps.grayscale(current_image)

        # Enhance contrast
        enhancer = ImageEnhance.Contrast(grayscale_image)
        enhanced_image = enhancer.enhance(contrast_factor)

        # Apply thresholding
        threshold_image = enhanced_image.point(lambda x: 0 if x < threshold_value else 255, '1')

        # Resize the image
        width, height = threshold_image.size
        new_width = int(width * resize_factor)
        new_height = int(height * resize_factor)
        resized_image = threshold_image.resize((new_width, new_height), Image.Resampling.LANCZOS)

        # Update the displayed image
        tk_image = ImageTk.PhotoImage(resized_image)
        image_label.config(image=tk_image)
        image_label.image = tk_image

        # Save processed image for OCR use
        global processed_image
        processed_image = resized_image

        # Extract and display items in real-time
        process_receipt()

    except Exception as e:
        messagebox.showerror("Error", f"Failed to update image: {str(e)}")

def open_file():
    """Open file dialog to upload a receipt image."""
    filepath = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])
    if filepath:
        try:
            global current_image
            current_image = Image.open(filepath)
            update_image()
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load image: {str(e)}")

def process_receipt():
    """Process the receipt and display items."""
    try:
        if processed_image is None:
            messagebox.showwarning("Warning", "No processed image available.")
            return

        # Perform OCR using Tesseract
        receipt_text = pytesseract.image_to_string(processed_image)

        # Extract items and calculate subtotal
        items, subtotal = extract_items_and_prices(receipt_text)
        if not items:
            messagebox.showwarning("Warning", "No valid items found in receipt.")
            return

        # Display extracted items in the GUI
        for widget in item_frame.winfo_children():
            widget.destroy()  # Clear previous items

        global item_vars
        item_vars = []
        for item in items:
            var = tk.StringVar()
            item_vars.append(var)
            item_label = tk.Label(item_frame, text=f"{item['item']} - ${item['price']:.2f}", font=("Arial", 10))
            item_label.pack(anchor="w", pady=2)
            entry = tk.Entry(item_frame, textvariable=var, width=40)
            entry.pack(anchor="w", pady=2)
            set_placeholder(entry, "Enter names separated by commas")

        subtotal_label.config(text=f"Subtotal: ${subtotal:.2f}")
        calculate_button.config(state="normal")
        global items_list
        items_list = items  # Save items for later use

        # Automatically calculate the split after processing
        calculate_split()

    except Exception as e:
        messagebox.showerror("Error", f"Failed to process receipt: {str(e)}")

def extract_items_and_prices(receipt_text):
    """Extract food items and their prices from receipt text."""
    lines = receipt_text.split('\n')
    items = []
    subtotal = 0

    for line in lines:
        # Skip separators and empty lines
        if re.match(r'-+', line) or not line.strip():
            continue
        
        match = re.search(r'(.*?)(\d+\.\d{2})$', line)  # Match description and price at end
        if match:
            item = match.group(1).strip()
            price = float(match.group(2).strip())
            items.append({'item': item, 'price': price})
            subtotal += price

    return items, subtotal

def set_placeholder(entry, placeholder_text):
    """Set placeholder text in a Tkinter entry widget."""
    entry.insert(0, placeholder_text)
    entry.bind("<FocusIn>", lambda event: clear_placeholder(entry, placeholder_text))
    entry.bind("<FocusOut>", lambda event: restore_placeholder(entry, placeholder_text))

def clear_placeholder(entry, placeholder_text):
    """Clear placeholder text on focus if it matches the placeholder."""
    if entry.get() == placeholder_text:
        entry.delete(0, tk.END)

def restore_placeholder(entry, placeholder_text):
    """Restore placeholder text if the entry is empty on focus out."""
    if not entry.get():
        entry.insert(0, placeholder_text)

def calculate_split():
    """Calculate the split bill based on assigned items, discount, and surcharge."""
    try:
        discount_percentage = float(discount_entry.get())
        discount_multiplier = (100 - discount_percentage) / 100

        surcharge_amount = 0.0
        if surcharge_var.get():
            surcharge_amount = float(surcharge_entry.get().strip())

        person_expenses = {}
        for i, item in enumerate(items_list):
            names = [name.strip() for name in item_vars[i].get().split(',') if name.strip()]
            if not names:
                continue
            split_cost = item['price'] / len(names)
            for name in names:
                person_expenses[name] = person_expenses.get(name, 0) + split_cost

        result_str = ""
        subtotal = sum(person_expenses.values())
        total = (subtotal + surcharge_amount) * discount_multiplier
        for person, expense in person_expenses.items():
            result_str += f"{person}: ${(expense * discount_multiplier):.2f}\n"
        result_str += f"\nSurcharge: ${surcharge_amount:.2f}\nTotal After Discount: ${total:.2f}"

        result_text.set(result_str)
    except ValueError:
        messagebox.showerror("Input Error", "Please provide valid numeric discount, surcharge, and assignment information.")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to calculate split: {str(e)}")

def add_item():
    """Add a manually entered item to the items list."""
    try:
        item_name = manual_item_entry.get().strip()
        item_price = float(manual_price_entry.get().strip())
        if item_name and item_price >= 0:
            items_list.append({'item': item_name, 'price': item_price})
            var = tk.StringVar()
            item_vars.append(var)
            item_label = tk.Label(item_frame, text=f"{item_name} - ${item_price:.2f}", font=("Arial", 10))
            item_label.pack(anchor="w", pady=2)
            entry = tk.Entry(item_frame, textvariable=var, width=40)
            entry.pack(anchor="w", pady=2)
            set_placeholder(entry, "Enter names separated by commas")

            # Update subtotal
            subtotal = sum(item['price'] for item in items_list)
            subtotal_label.config(text=f"Subtotal: ${subtotal:.2f}")
            calculate_split()  # Update the split calculation
        else:
            messagebox.showwarning("Input Error", "Please enter a valid item name and price.")
    except ValueError:
        messagebox.showwarning("Input Error", "Please enter a valid numeric value for the price.")

# GUI Setup
root = tk.Tk()
root.title("Receipt Analyzer & Splitter")

style = ttk.Style(root)
root.configure(bg="#f2f2f2")

# Upload Button Frame
upload_frame = tk.Frame(root, bg="#f2f2f2")
upload_frame.pack(pady=10)

upload_button = tk.Button(upload_frame, text="Upload Receipt Image", command=open_file, font=("Arial", 12, "bold"), bg="#4CAF50", fg="white")
upload_button.pack(side="left", padx=10)

# Image Display Frame
image_frame = tk.LabelFrame(root, text="Processed Receipt Image", font=("Arial", 12, "bold"), bg="#f9f9f9", padx=10, pady=10)
image_frame.pack(fill="both", expand=True, padx=15, pady=5)

image_label = tk.Label(image_frame)
image_label.pack()

# Sliders Frame
slider_frame = tk.LabelFrame(root, text="Image Processing Adjustments", font=("Arial", 12, "bold"), bg="#f9f9f9", padx=10, pady=10)
slider_frame.pack(fill="x", padx=15, pady=5)

# Contrast Slider
tk.Label(slider_frame, text="Contrast Level", bg="#f9f9f9", font=("Arial", 10)).grid(row=0, column=0, padx=5)
contrast_slider = tk.Scale(slider_frame, from_=0.5, to=3.0, resolution=0.1, orient="horizontal", command=lambda x: update_image(), bg="#f9f9f9")
contrast_slider.set(2.0)
contrast_slider.grid(row=0, column=1, padx=5, pady=5)

# Threshold Slider
tk.Label(slider_frame, text="Threshold Level", bg="#f9f9f9", font=("Arial", 10)).grid(row=1, column=0, padx=5)
threshold_slider = tk.Scale(slider_frame, from_=50, to=200, orient="horizontal", command=lambda x: update_image(), bg="#f9f9f9")
threshold_slider.set(140)
threshold_slider.grid(row=1, column=1, padx=5, pady=5)

# Resize Slider
tk.Label(slider_frame, text="Resize Factor (%)", bg="#f9f9f9", font=("Arial", 10)).grid(row=2, column=0, padx=5)
resize_slider = tk.Scale(slider_frame, from_=100, to=300, orient="horizontal", command=lambda x: update_image(), bg="#f9f9f9")
resize_slider.set(150)
resize_slider.grid(row=2, column=1, padx=5, pady=5)

# Manual Entry Frame
manual_entry_frame = tk.LabelFrame(root, text="Manually Add Items", font=("Arial", 12, "bold"), bg="#f9f9f9", padx=10, pady=10)
manual_entry_frame.pack(fill="x", padx=15, pady=5)

tk.Label(manual_entry_frame, text="Item Name:", bg="#f9f9f9", font=("Arial", 10)).grid(row=0, column=0, padx=5, sticky="w")
manual_item_entry = tk.Entry(manual_entry_frame, width=30)
manual_item_entry.grid(row=0, column=1, padx=5, pady=5)

tk.Label(manual_entry_frame, text="Item Price:", bg="#f9f9f9", font=("Arial", 10)).grid(row=0, column=2, padx=5, sticky="w")
manual_price_entry = tk.Entry(manual_entry_frame, width=10)
manual_price_entry.grid(row=0, column=3, padx=5, pady=5)

add_item_button = tk.Button(manual_entry_frame, text="Add Item", command=add_item, font=("Arial", 10), bg="#2196F3", fg="white")
add_item_button.grid(row=0, column=4, padx=10, pady=5)

# Item Frame
item_frame = tk.LabelFrame(root, text="Extracted Items", font=("Arial", 12, "bold"), bg="#f9f9f9", padx=10, pady=10)
item_frame.pack(fill="both", expand=True, padx=15, pady=5)

# Discount and Surcharge
discount_frame = tk.LabelFrame(root, text="Discount & Surcharge", font=("Arial", 12, "bold"), bg="#f9f9f9", padx=10, pady=10)
discount_frame.pack(fill="x", padx=15, pady=5)

tk.Label(discount_frame, text="Discount Percentage:", bg="#f9f9f9", font=("Arial", 10)).grid(row=0, column=0, padx=5, sticky="w")
discount_entry = tk.Entry(discount_frame, width=5)
discount_entry.insert(0, "5")  # Default discount
discount_entry.grid(row=0, column=1, padx=5, pady=5)

surcharge_var = tk.BooleanVar()
surcharge_checkbox = tk.Checkbutton(discount_frame, text="Surcharge?", variable=surcharge_var, bg="#f9f9f9", font=("Arial", 10))
surcharge_checkbox.grid(row=1, column=0, padx=5, pady=5, sticky="w")

tk.Label(discount_frame, text="Surcharge Amount:", bg="#f9f9f9", font=("Arial", 10)).grid(row=1, column=1, padx=5, sticky="w")
surcharge_entry = tk.Entry(discount_frame, width=10)
surcharge_entry.grid(row=1, column=2, padx=5, pady=5)
surcharge_entry.config(state="disabled")
surcharge_checkbox.config(command=lambda: surcharge_entry.config(state="normal" if surcharge_var.get() else "disabled"))

# Subtotal and Calculate Button
bottom_frame = tk.Frame(root, bg="#f2f2f2")
bottom_frame.pack(pady=10)

subtotal_label = tk.Label(bottom_frame, text="Subtotal: $0.00", font=("Arial", 12, "bold"), bg="#f2f2f2")
subtotal_label.grid(row=0, column=0, padx=10)

calculate_button = tk.Button(bottom_frame, text="Calculate Split", state="disabled", command=calculate_split, font=("Arial", 12, "bold"), bg="#FF5722", fg="white")
calculate_button.grid(row=0, column=1, padx=10)

# Result Frame
result_text = tk.StringVar()
result_text.set("")
result_label_frame = tk.LabelFrame(root, text="Result", font=("Arial", 12, "bold"), bg="#f9f9f9", padx=10, pady=10)
result_label_frame.pack(fill="both", expand=True, padx=15, pady=5)

result_label = tk.Label(result_label_frame, textvariable=result_text, font=("Arial", 12), justify="left", bg="#f9f9f9")
result_label.pack(pady=10)

# Global Variables
current_image = None
processed_image = None

# Run GUI Loop
root.mainloop()
