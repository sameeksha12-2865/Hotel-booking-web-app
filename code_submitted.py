from tkinter import *
def on_close():
	root.destroy()
root=Tk()
root.title("Sancastle bookings")
root.maxsize(800,400)

img = PhotoImage(file="hotel.png")
canvas = Canvas(root, width=img.width(), height=img.height())
canvas.pack()

canvas.create_image(0, 0, anchor=NW, image=img)

pic=Label(root,image=img)
pic.pack(pady=20)

l1=Label(root,text="Welcome to Sandcastle bookings!",bg="light blue",fg="black",font=("georgia",30,))
l1.window=canvas.create_window(70,40,anchor=NW,window=l1)

def open_next():
    root.destroy()
    import win2

b1=Button(root,text="Next page",bg="light blue",fg="black",font=("georgia",12,"bold"),command=open_next)
b1.window=canvas.create_window(300,250,anchor=NW,window=b1)

root.mainloop()
from tkinter import *

win2 = Tk()
win2.geometry("800x800")
win2.maxsize(800,600)
win2.title("Start booking")

def open():
    win2.destroy()
    import win3

def open1():
    win2.destroy()
    import win4

def open2():
    win2.destroy()
    import win10
    

img = PhotoImage(file="rec.png")
canvas = Canvas(win2, width=img.width(), height=img.height())
canvas.pack()

canvas.create_image(0, 0, anchor=NW, image=img)

pic=Label(win2,image=img)
pic.pack(pady=20)


b1=Button(win2,text="Sign Up",bg="beige",fg="black",font=("georgia",12),height=2,width=6,command=open)
b2=Button(win2,text="Book Your Hotel",bg="beige",fg="black",font=("georgia",12),height=2,width=14,command=open1)
b3=Button(win2,text="Exit",bg="beige",fg="black",font=("georgia",12),height=2,width=5,command=open2)
b1.window=canvas.create_window(10,55,anchor=NW,window=b1)
b2.window = canvas.create_window(10, 115, anchor=NW, window=b2)
b3.window = canvas.create_window(10, 175, anchor=NW, window=b3)
win2.mainloop()

from tkinter import *

root = Tk()
root.geometry("900x900")
root.title("sign in")
root.maxsize(700,400)


img = PhotoImage(file="signin.png")
canvas = Canvas(root, width=img.width(), height=img.height())
canvas.pack()

canvas.create_image(0, 0, anchor=NW, image=img)

pic=Label(root,image=img)
pic.pack(pady=20)

l1=Label(root,text="Name:",font=("Algerian",14),bg="orange",fg="black")
l1.window = canvas.create_window(200, 50, anchor=NW, window=l1)

username_entry = Entry(root,bg="black",fg="white")
username_entry.window = canvas.create_window(380, 50, anchor=NW, window=username_entry)

l2 = Label(root, text="Phone number:",font=("Algerian",14),bg="orange",fg="black")
l2.window = canvas.create_window(200, 100, anchor=NW, window=l2)

phonenumber_entry = Entry(root,bg="black",fg="white")  
phonenumber_entry.window = canvas.create_window(380, 100, anchor=NW, window=phonenumber_entry,)

l3=Label(root,text="Email:",font=("Algerian",14),bg="orange",fg="black")
l3.window = canvas.create_window(200, 150, anchor=NW, window=l3)
email_entry=Entry(root,bg="black",fg="white")
email_entry.window = canvas.create_window(380, 150, anchor=NW, window=email_entry)

def open():
    root.destroy()
    import win4

btn1 = Button(root, text="Next page",bg="orange",fg="black",font=("algerian",12),command=open)
btn1.window = canvas.create_window(350, 220, anchor=NW, window=btn1)


root.mainloop()


from tkinter import *

root = Tk()
root.geometry("900x900")


root.maxsize(700,550)

root.title("Location")
img = PhotoImage(file="img4.png")
canvas = Canvas(root, width=img.width(), height=img.height())
canvas.pack()

canvas.create_image(0, 0, anchor=NW, image=img)

pic=Label(root,image=img)
pic.pack(pady=20)

l1=Label(root,text="CHOOSE YOUR DESTINATION",font=("Georgia",12),bg="white",fg="black")
l1.window = canvas.create_window(100, 50, anchor=NW, window=l1)
Checkbutton1 = IntVar() 
Checkbutton2 = IntVar()
Checkbutton3 = IntVar()
cb1=Checkbutton(root, text="Paris",variable = Checkbutton1,onvalue = 1,offvalue = 0,height = 2,width = 10,bg="light blue",fg="black")
cb2=Checkbutton(root, text = "New York", variable = Checkbutton2,onvalue = 1,offvalue = 0,height = 2,width = 10,bg="light blue",fg="black") 
cb3=Checkbutton(root, text="Maldives",variable = Checkbutton3,onvalue = 1,offvalue = 0,height = 2,width = 10,bg="light blue",fg="black")
cb1.window = canvas.create_window(150, 100, anchor=NW, window=cb1)
cb2.window = canvas.create_window(150, 150, anchor=NW, window=cb2)
cb3.window = canvas.create_window(150,200, anchor=NW, window=cb3)
l2=Label(root,text="CHOOSE YOUR CHOICE OF PROPERTY",font=("Georgia",12),bg="white",fg="black")
l2.window = canvas.create_window(70, 250, anchor=NW, window=l2)
Checkbutton4 = IntVar() 
Checkbutton5 = IntVar()
Checkbutton6 = IntVar()
cb4=Checkbutton(root, text="Happy Mornings",variable = Checkbutton4,onvalue = 1,offvalue = 0,height = 2,width = 12,bg="light blue",fg="black")
cb5=Checkbutton(root, text = "Holiday Breeze", variable = Checkbutton5,onvalue = 1,offvalue = 0,height = 2,width = 12,bg="light blue",fg="black") 
cb6=Checkbutton(root, text="Hotel Inn",variable = Checkbutton6,onvalue = 1,offvalue = 0,height = 2,width = 12,bg="light blue",fg="black")
cb4.window = canvas.create_window(150, 300, anchor=NW, window=cb4)
cb5.window = canvas.create_window(150, 350, anchor=NW, window=cb5)
cb6.window = canvas.create_window(150, 400, anchor=NW, window=cb6)

def open():
    root.destroy()
    import win5

b1=Button(root,text="Submit",activebackground="white",activeforeground="black",command=open)
b1.window = canvas.create_window(170, 450, anchor=NW, window=b1)

root.mainloop()
from tkinter import *
from datetime import datetime
root = Tk()
root.title("Room Booking")
root.geometry("900x900")
root.maxsize(650,400)

img = PhotoImage(file="r1.png")
canvas = Canvas(root, width=img.width(), height=img.height())
canvas.pack()

canvas.create_image(0, 0, anchor=NW, image=img)

pic=Label(root,image=img)
pic.pack(pady=20)





def total_days():
    checkin_date = checkin_var.get()
    checkout_date = checkout_var.get()

    try:
        checkin_date = datetime.strptime(checkin_date, "%Y-%m-%d")
        checkout_date = datetime.strptime(checkout_date, "%Y-%m-%d")

        total = checkout_date - checkin_date
        total_days = total.days

        result_label.config(text=f"Total Days of Stay: {total_days} days")
    except ValueError:
        result_label.config(text="Invalid date format. Use YYYY-MM-DD")




checkin_label = Label(root, text="Check-In Date:",font=("Algerian", 12,"bold"),bg="beige",fg="black")
checkin_label.window = canvas.create_window(10, 10, anchor=NW, window=checkin_label)


checkin_var = StringVar()
checkin_entry = Entry(root, textvariable=checkin_var)
checkin_entry.window = canvas.create_window(150, 10, anchor=NW, window=checkin_entry)


checkout_label = Label(root, text="Check-Out Date:",font=("Algerian", 12,"bold"),bg="beige",fg="black")
checkout_label.window = canvas.create_window(10, 70, anchor=NW, window=checkout_label)


checkout_var = StringVar()
checkout_entry = Entry(root, textvariable=checkout_var)
checkout_entry.window = canvas.create_window(150, 70, anchor=NW, window=checkout_entry)


calculate_button = Button(root, text="Calculate",font=("Algerian", 12,"bold"),bg="beige",fg="black", command=total_days)
calculate_button.window = canvas.create_window(150, 180, anchor=NW, window=calculate_button)


result_label =Label(root, text="",font=("Algerian", 12,"bold"),bg="beige",fg="black",height=1)
result_label.window = canvas.create_window(250, 180, anchor=NW, window=result_label)


def open():
    root.destroy()
    import win6 
    
b1=Button(root,text="Next page",font=("Algerian", 12,"bold"),bg="beige",fg="black",command=open)
b1.window = canvas.create_window(150, 230, anchor=NW, window=b1)


root.mainloop()


from tkinter import*
import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Hotel Booking with Amenities")
root.geometry("700x610")


def calculate_price():
    room_type = room_type_var.get()
    nights = nights_var.get()
    spa = spa_var.get()
    laundry = laundry_var.get()
    gym = gym_var.get()
    pool = pool_var.get()
    minibar=minibar_var.get()
    pickup=pickup_var.get()

    try:
        nights = int(nights)

        if room_type == "2 bed AC":
            room_price = 3500  
        elif room_type == "2 bed Non-AC":
            room_price = 4000 
        elif room_type == "3 bed Non-AC":
            room_price = 5000  
        elif room_type == "3 bed AC":
            room_price = 5500 
        else:
            result_label.config(text="Invalid room type")
            return

        spa_price = spa * 500  
        laundry_price = laundry * 100  # per wash
        gym_price = gym * 400  
        pool_price=pool * 200
        minibar_price=minibar * 500 #per drink
        pickup_price=pickup*100
        total_price = (nights * room_price) + spa_price + laundry_price + gym_price + pool_price + minibar_price + pickup_price
        result_label.config(text=f"Total Price:₹ {total_price}",font=("georgia",10,"bold"),background="light blue",foreground="black")
    except ValueError:
        result_label.config(text="Invalid input for nights, spa, laundry,pool,minibar,pickup or gym",background="light blue",foreground="black")



img = PhotoImage(file="pool.png")
canvas = Canvas(root, width=img.width(), height=img.height())
canvas.pack()

canvas.create_image(0, 0, anchor=NW, image=img)

pic=Label(root,image=img)
pic.pack(pady=20)

room_type_label = tk.Label(root, text="Room Type:",font=("georgia",10,"bold"),background="light blue",foreground="black")
room_type_label.window = canvas.create_window(10, 10, anchor=NW, window=room_type_label)

room_type_var = tk.StringVar()
room_type_combobox = ttk.Combobox(root, textvariable=room_type_var, values=["3 bed AC", "3 bed Non-AC","2 bed AC","2 bed Non-Ac"])
room_type_combobox.window = canvas.create_window(250, 10, anchor=NW, window=room_type_combobox)
room_type_combobox.set("CHOOSE")  # Default room type



nights_label = tk.Label(root, text="Number of Nights:",font=("georgia",10,"bold"),background="light blue",foreground="black")
nights_label.window = canvas.create_window(10, 60, anchor=NW, window=nights_label)

nights_var = tk.StringVar()
nights_entry = ttk.Entry(root, textvariable=nights_var)
nights_entry.window = canvas.create_window(250,60, anchor=NW, window=nights_entry)

spa_label = tk.Label(root, text="Number of Spa Sessions:",font=("georgia",10,"bold"),background="light blue",foreground="black")
spa_label.window = canvas.create_window(10, 130, anchor=NW, window=spa_label)
spa_var = tk.IntVar()
spa_entry = ttk.Entry(root, textvariable=spa_var)
spa_entry.window = canvas.create_window(250, 130, anchor=NW, window=spa_entry)

laundry_label = tk.Label(root, text="Number of Laundry Services:",font=("georgia",10,"bold"),background="light blue",foreground="black")
laundry_label.window = canvas.create_window(10, 200, anchor=NW, window=laundry_label)

laundry_var = tk.IntVar()
laundry_entry = ttk.Entry(root, textvariable=laundry_var)
laundry_entry.window = canvas.create_window(250, 200, anchor=NW, window=laundry_entry)

gym_label = tk.Label(root, text="Number of Gym Sessions:",font=("georgia",10,"bold"),background="light blue",foreground="black")
gym_label.window = canvas.create_window(10, 270, anchor=NW, window=gym_label)

gym_var = tk.IntVar()
gym_entry = ttk.Entry(root, textvariable=gym_var)
gym_entry.window = canvas.create_window(250, 270, anchor=NW, window=gym_entry)

pool_label = tk.Label(root, text="Number of Pool Sessions:",font=("georgia",10,"bold"),background="light blue",foreground="black")
pool_label.window = canvas.create_window(10, 340, anchor=NW, window=pool_label)

pool_var = tk.IntVar()
pool_entry = ttk.Entry(root, textvariable=pool_var)
pool_entry.window = canvas.create_window(250, 340, anchor=NW, window=pool_entry)


minibar_label = tk.Label(root, text="Drinks per day:",font=("georgia",10,"bold"),background="light blue",foreground="black")
minibar_label.window = canvas.create_window(10, 410, anchor=NW, window=minibar_label)

minibar_var = tk.IntVar()
minibar_entry = ttk.Entry(root, textvariable=minibar_var)
minibar_entry.window = canvas.create_window(250, 410, anchor=NW, window=minibar_entry)

pickup_label = tk.Label(root, text="Pick or Drop service:",font=("georgia",10,"bold"),background="light blue",foreground="black")
pickup_label.window = canvas.create_window(10, 480, anchor=NW, window=pickup_label)

pickup_var = tk.IntVar()
pickup_entry = ttk.Entry(root, textvariable=pickup_var)
pickup_entry.window = canvas.create_window(250, 480, anchor=NW, window=pickup_entry)
 
result_label = tk.Label(root, text="")
result_label.window = canvas.create_window(200, 520, anchor=NW, window=result_label)

calculate_button = tk.Button(root, text="Calculate:" ,command=calculate_price,font=("georgia",10,"bold"),background="light blue",foreground="black")
calculate_button.window = canvas.create_window(10, 520, anchor=NW, window=calculate_button)

def open_next():
    root.destroy()
    import win7

b1=tk.Button(root, text="Next page",command=open_next,font=("georgia",10,"bold"),background="light blue",foreground="black")
b1.window = canvas.create_window(450, 550, anchor=NW, window=b1)

root.mainloop()

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
from tkinter import *

def generate_acknowledgment():
    name = name_entry.get()
    destination = destination_entry.get()
    days_of_stay = days_of_stay_entry.get()
    total_bill = total_bill_entry.get()

    acknowledgment_text = (
        f"Name: {name}\n"
        f"Destination: {destination}\n"
        f"Days of Stay: {days_of_stay}\n"
        f"Total Bill: {total_bill}\n"
        "Thank you for booking with us!"
    )

    acknowledgment_label.config(text=acknowledgment_text)


root = Tk()
root.title("Booking Acknowledgment")
root.maxsize(650,400)


img = PhotoImage(file="ack.png")
canvas = Canvas(root, width=img.width(), height=img.height())
canvas.pack()

canvas.create_image(0, 0, anchor=NW, image=img)

pic=Label(root,image=img)
pic.pack(pady=20)

def open():
    root.destroy()
    import win10

name_label = Label(root, text="Name:",font="bold")
name_label.window = canvas.create_window(10, 10, anchor=NW, window=name_label)
name_entry = Entry(root)
name_entry.window = canvas.create_window(110, 10, anchor=NW, window=name_entry)

destination_label = Label(root, text="Destination:",font="bold")
destination_label.window = canvas.create_window(10, 70, anchor=NW, window=destination_label)
destination_entry = Entry(root)
destination_entry.window = canvas.create_window(110, 70, anchor=NW, window=destination_entry)

days_of_stay_label = Label(root, text="Days of Stay:",font="bold")
days_of_stay_label.window = canvas.create_window(10, 130, anchor=NW, window=days_of_stay_label)
days_of_stay_entry = Entry(root)
days_of_stay_entry.window = canvas.create_window(110, 130, anchor=NW, window=days_of_stay_entry)

total_bill_label = Label(root, text="Total Bill:",font="bold")
total_bill_label.window = canvas.create_window(10, 200, anchor=NW, window=total_bill_label)
total_bill_entry = Entry(root)
total_bill_entry.window = canvas.create_window(110, 200, anchor=NW, window=total_bill_entry)


generate_button = Button(root, text="Generate Acknowledgment",font="bold", command=generate_acknowledgment)
generate_button.window = canvas.create_window(10, 250, anchor=NW, window=generate_button)

b1=Button(root, text="Leave a review",font="bold", command=open)
b1.window=canvas.create_window(470,250,anchor=NW,window=b1)

acknowledgment_label = Label(root, text="", font=("georgia", 10,"bold"), wraplength=400, justify="center")
acknowledgment_label.window = canvas.create_window(220, 250, anchor=NW, window=acknowledgment_label)

root.mainloop()

from tkinter import *

def submit_review():
    review_text = review_entry.get("1.0", END).strip()
    rating_value = rating_var.get()

    acknowledgment_text = (
        f"Review: {review_text}\n"
        f"Rating: {rating_value}\n\n"
        "Thank you for booking with us!"
    )

    acknowledgment_label.config(text=acknowledgment_text)

# Create the main window
root = Tk()
root.title("Review Page")
root.maxsize(600,400)
img = PhotoImage(file="review.png")
canvas = Canvas(root, width=img.width(), height=img.height())
canvas.pack()

canvas.create_image(0, 0, anchor=NW, image=img)

pic=Label(root,image=img)
pic.pack(pady=20)



review_label = Label(root, text="Enter your review:",background="light blue",foreground="black",font=("georgia",10))
review_label.window=canvas.create_window(10,20,anchor=NW,window=review_label)
review_entry = Text(root, height=5, width=40)
review_entry.window=canvas.create_window(200,20,anchor=NW,window=review_entry)

rating_label = Label(root, text="Choose your rating (1 to 5):",background="light blue",foreground="black",font=("georgia",10))
rating_label.window=canvas.create_window(10,120,anchor=NW,window=rating_label)
rating_var = IntVar()

for i in range(1, 6):
    Radiobutton(root, text=str(i), variable=rating_var, value=i,background="light blue",foreground="black", font=("Arial", 12)).place(x=150 + i * 50, y=120)


submit_button = Button(root, text="Submit Review", command=submit_review,background="light blue",foreground="black",font=("georgia",10))
submit_button.window=canvas.create_window(10,200,anchor=NW,window=submit_button)

acknowledgment_label = Label(root, text="", wraplength=400, justify="center",background="light blue",foreground="black",font=("georgia",10))
acknowledgment_label.window=canvas.create_window(200,200,anchor=NW,window=acknowledgment_label)


root.protocol("WM_DELETE_WINDOW",on_close)
root.mainloop()
root.destroy()







