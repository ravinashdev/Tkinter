# Advanced vs Keyword Arguments
# Arguments with default values written as keywords allow you to invoke the function with
# without having to pass arguments
def my_function(a=1,b=2,c=3):
    return a+b+c
print(my_function())
# can alter the defaults by passing an argument to change any default
print(my_function(c=4))
# ARGUMENTS
# Function with unlimited *arguments asterisk is needed but can be named any alias
# arguments are of type Tuple
# arguments are iterable and indexed
def add(*arguments):
    print(type(arguments))
    print(arguments[0])
    for argument in arguments:
        print(argument)
    return sum(arguments)
print(add(1,2,3,4,5))
# KEYWORD ARGUMENTS
# Function with unlimited **keyword_arguments double asterisk is needed but can be named any alias
# arguments are of type dictionary with key:value pair
def calculate(**keyword_arguments):
    print(type(keyword_arguments))
    print(keyword_arguments)
    for key, value in keyword_arguments.items():
        print(key, value)
print(calculate(a=1,b=2,c=3))

# Use **kwargs to create a Class
class Car:
    def __init__(self, **keyword_arguments):
        # Use the get method instead of key[value] in the event the keyword_argument doesn't exist
        self.make = keyword_arguments.get("make")
        self.model = keyword_arguments.get("model")
        self.year = keyword_arguments.get("year")
        # Set the default unless argument is given in the **kwargs
        self.price = keyword_arguments.get("price", 80000 )

new_car = Car(make="Lexus", model="GX550", year=2021)
print(new_car.make)
print(new_car.model)
print(new_car.year)
# Price returns the default value since it was never set in the keyword_arguments
print(new_car.price)