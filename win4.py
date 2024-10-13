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
