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