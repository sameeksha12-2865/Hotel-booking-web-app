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

