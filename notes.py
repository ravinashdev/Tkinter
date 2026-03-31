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