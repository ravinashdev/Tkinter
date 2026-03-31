from tkinter import *
# FUNCTIONS
def miles_to_kilometers(miles):
    kilometers = miles*1.609344
    return kilometers
def miles_to_kilometers_label_changer():
    miles = int(entry_box.get())
    # print(entry_box.get())
    kilometers = miles_to_kilometers(miles)
    label_to_display_kilometers.config(text=f"is equal to {kilometers} kilometers ")

# Initialize the window
window = Tk()
window.title("Miles to Kilometers Converter")
window.minsize(width=500, height=500)
# Padding to the window
window.config(padx=150, pady=150)

# User enter miles
entry_box = Entry(width=10)
#Add some text to begin with
entry_box.insert(END,0)
entry_box.grid(row=0, column=4)

# Label to display miles after conversion & for just miles
kilometers =  0
label_to_display_kilometers = Label(text=f"is equal to {kilometers} kilometers ")
label_to_display_kilometers.grid(row=1, column=4)
miles_label = Label(text="Miles")
miles_label.grid(row=0, column=5)

#Button to click and initiate conversion
convert_button = Button(text="Convert", command=lambda: miles_to_kilometers_label_changer())
convert_button.grid(row=2, column=4)

# Keep window object open so it doesn't close
window.mainloop()