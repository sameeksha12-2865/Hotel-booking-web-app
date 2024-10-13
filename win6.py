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
