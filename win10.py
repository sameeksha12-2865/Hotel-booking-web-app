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

root.mainloop()


