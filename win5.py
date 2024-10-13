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


