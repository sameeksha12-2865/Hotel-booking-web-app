from tkinter import *
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