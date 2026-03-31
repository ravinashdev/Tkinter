import tkinter

# Initialize the window
window = tkinter.Tk()
window.title("Tkinter")
window.minsize(width=500, height=500)

# Labels
my_label = tkinter.Label(text="Hello World", font=("Arial", 25, "bold"))
# Method to automatically place label in the screen and center it
my_label.pack(side="right",expand=True)







# Keep window object open so it doesn't close
window.mainloop()