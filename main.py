import tkinter

# Initialize the window
window = tkinter.Tk()
window.title("Tkinter")
window.minsize(width=500, height=500)

# Labels
my_label = tkinter.Label(text="Hello World", font=("Arial", 25, "bold"))
# Method to automatically place label in the screen and center it
my_label.pack(side="right",expand=True)
# Advanced vs Keyword Arguments
# Arguments with default values written as keywords allow you to invoke the function with
# without having to pass arguments
def my_function(a=1,b=2,c=3):
    return a+b+c
print(my_function())
# can alter the defaults by passing an argument to change any default
print(my_function(c=4))
# Function with unlimited *arguments asterisk is needed but can be named any alias
# arguments are of type Tuple
def add(*arguments):
    print(type(arguments))
    return sum(arguments)
print(add(1,2,3,4,5))







# Keep window object open so it doesn't close
window.mainloop()