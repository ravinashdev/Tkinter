import tkinter
# from tkinter import * (using this we can remove tkinter method)
# Functions
def my_button_1_clicked():
    my_label_1.config(text="Pressed")
    print("Pressed")
def my_button_2_clicked():
    user_input = input.get()
    my_label_2.config(text=user_input)
    print(f"{user_input}")
# Initialize the window
window = tkinter.Tk()
window.title("Tkinter")
window.minsize(width=500, height=500)
# Padding to the window
window.config(padx=20, pady=20)

# Labels
my_label_1 = tkinter.Label(text="my_button_1_text", font=("Arial", 25, "bold"))
my_label_2 = tkinter.Label(text="my_button_2_text", font=("Arial", 25, "bold"))
# Method to automatically place label in the screen and center it
# my_label_1.pack(side="right",expand=True)
# my_label_2.pack(side="left",expand=True)
# Place label on the screen given x,y coordinates as arguments very specific
# my_label_1.place(x=10,y=10)
# my_label_2.place(x=10,y=20)
# Grid allows you to create a grid of rows and columns with intuitive placements
# CANNOT use grid and pack at the same time
my_label_1.grid(column=0,row=0)
my_label_2.grid(column=0,row=1)

# Button
# command is the name of the function or using lambda to write a blank function
# my_button_1 = tkinter.Button(text="my_button_1", command=lambda: print("Clicked"))
my_button_1 = tkinter.Button(text="my_button_1", command= my_button_1_clicked)
# When button clicked label text= "Pressed" via config change
my_button_2 = tkinter.Button(text="my_button_2", command=my_button_2_clicked)
# my_button_1.pack(side="top",expand=True)
# my_button_2.pack(side="bottom",expand=True)

# Entry
input = tkinter.Entry()
# input.pack(side="top",expand=True)

# Keep window object open so it doesn't close
window.mainloop()