import tkinter as tk
from tkinter import messagebox

def make_payment():
    payment_method = payment_method_var.get()

    if payment_method == "Credit/Debit Card":
        card_number = card_number_entry.get()
        card_holder_name = card_holder_name_entry.get()
        expiry_date = expiry_date_entry.get()
        cvv = cvv_entry.get()

        # Perform credit/debit card payment processing logic here
        # For simplicity, just display a thank you message
        message = f"Thank you for making a credit/debit card payment!\n\nCard Number: {card_number}\nCard Holder: {card_holder_name}\nExpiry Date: {expiry_date}\nCVV: {cvv}"
        messagebox.showinfo("Payment Successful", message)

    elif payment_method == "UPI":
        upi_id = upi_id_entry.get()
        amount = amount_entry.get()
        name = name_entry.get()

        # Perform UPI payment processing logic here
        # For simplicity, just display a thank you message
        message = f"Thank you for making a UPI payment!\n\nUPI ID: {upi_id}\nAmount: {amount}\nName: {name}"
        messagebox.showinfo("Payment Successful", message)

# Create the main window
root = tk.Tk()
root.title("Payment Details")
root.minsize(600,400)

# Set a background image
background_image = tk.PhotoImage(file="pay.png")
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)

# Create and place widgets
tk.Label(root, text="Payment Method:", bg="white").grid(row=0, column=0, padx=10, pady=10, sticky="w")
payment_methods = ["Credit/Debit Card", "UPI"]
payment_method_var = tk.StringVar(root)
payment_method_var.set(payment_methods[0])
payment_menu = tk.OptionMenu(root, payment_method_var, *payment_methods)
payment_menu.config(bg="white")
payment_menu.grid(row=0, column=1, padx=10, pady=10, sticky="w")


tk.Label(root, text="Card Number:", bg="white").grid(row=1, column=0, padx=10, pady=10, sticky="w")
card_number_entry = tk.Entry(root)
card_number_entry.grid(row=1, column=1, padx=10, pady=10, sticky="w")

tk.Label(root, text="Card Holder Name:", bg="white").grid(row=2, column=0, padx=10, pady=10, sticky="w")
card_holder_name_entry = tk.Entry(root)
card_holder_name_entry.grid(row=2, column=1, padx=10, pady=10, sticky="w")

tk.Label(root, text="Expiry Date (mm/yy):", bg="white").grid(row=3, column=0, padx=10, pady=10, sticky="w")
expiry_date_entry = tk.Entry(root)
expiry_date_entry.grid(row=3, column=1, padx=10, pady=10, sticky="w")

tk.Label(root, text="CVV:", bg="white").grid(row=4, column=0, padx=10, pady=10, sticky="w")
cvv_entry = tk.Entry(root)
cvv_entry.grid(row=4, column=1, padx=10, pady=10, sticky="w")


tk.Label(root, text="UPI ID:", bg="white").grid(row=5, column=0, padx=10, pady=10, sticky="w")
upi_id_entry = tk.Entry(root)
upi_id_entry.grid(row=5, column=1, padx=10, pady=10, sticky="w")


tk.Label(root, text="Amount:", bg="white").grid(row=6, column=0, padx=10, pady=10, sticky="w")
amount_entry = tk.Entry(root)
amount_entry.grid(row=6, column=1, padx=10, pady=10, sticky="w")

tk.Label(root, text="Name:", bg="white").grid(row=7, column=0, padx=10, pady=10, sticky="w")
name_entry = tk.Entry(root)
name_entry.grid(row=7, column=1, padx=10, pady=10, sticky="w")

payment_button = tk.Button(root, text="Make Payment", command=make_payment, bg="green", fg="white")
payment_button.grid(row=8, column=0, columnspan=2, pady=20)

def open():
    root.destroy()
    import win9

Next_button=tk.Button(root, text="Next Page", command=open, bg="green", fg="white")
Next_button.grid(row=8, column=2, columnspan=2, pady=20)

root.mainloop()