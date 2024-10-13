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
