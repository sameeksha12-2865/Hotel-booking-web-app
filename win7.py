
from tkinter import *
import random


def apply_discount():
    try:
        base_price = float(base_price_var.get())

        lucky_number = random.randint(1, 10)
        if lucky_number == 7:
            discount = 0.2 
            message="CONGRATS! you received a discount of 20%"
        elif lucky_number == 3:
            discount = 0.15
            message="CONGRATS! you received a discount of 15%"
        elif lucky_number == 9:
            discount = 0.25
            message="CONGRATS! you received a discount of 25%"
        elif lucky_number == 2:
            discount = 0.10
            message="CONGRATS! you received a discount of 10%"
        else:
            discount = 0  # No discount for other numbers
            message="BETTER LUCK NEXT TIME!"
        
        discounted_price = base_price - (base_price * discount)
        result_label.config(text=f"Lucky Number: {lucky_number}\n{message}\nDiscounted Price: ₹{discounted_price:.2f}")
    except ValueError:
        result_label.config(text="Invalid input for base price")
# GUI setup
root = Tk()
root.geometry("900x900")
root.maxsize(700,500)
root.title("Discount (lucky draw)")

img = PhotoImage(file="ld.png")
canvas = Canvas(root, width=img.width(), height=img.height())
canvas.pack()

canvas.create_image(0, 0, anchor=NW, image=img)

pic=Label(root,image=img)
pic.pack(pady=20)

# Create and place widgets
base_price_label =Label(root, text="Base Price:",font=("georgia",12,"bold"),bg="red",fg="white")
base_price_label.window = canvas.create_window(10, 10, anchor=NW, window=base_price_label)

base_price_var = StringVar()
base_price_entry = Entry(root, textvariable=base_price_var,font=("georgia",12),bg="red",fg="white")
base_price_entry.window = canvas.create_window(150, 10, anchor=NW, window=base_price_entry)

calculate_button = Button(root, text="Generate Discount",font=("georgia",12,"bold"),bg="red",fg="white", command=apply_discount)
calculate_button.window = canvas.create_window(10, 140, anchor=NW, window=calculate_button)

result_label =Label(root, text="",background="white",foreground="black",font=("georgia",8,"bold"))
result_label.window = canvas.create_window(100, 70, anchor=NW, window=result_label)

def open():
    root.destroy()
    import win8

b1=Button(root,text="Proceed to payment page:",font=("georgia",10,"bold"),bg="red",fg="white",command=open)
b1.place(x=210,y=230)
root.mainloop()