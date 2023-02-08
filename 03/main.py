# LESSON 3
# FUNCTIONS, F-Strings

# def first_function():
#     print("Hello from the function!")

# first_function()

# Defining Functions to use in our program
# add(a,b) is expecting two input paramters `a` and `b` and will return them added together
def add(a,b):
    print(f"Adding {a} and {b}!") 
    return a + b

# subtract(a,b) is expecting two input paramters `a` and `b` and will return the difference    
def subtract(a,b):
    print(f"Subtracting {b} from {a}!")
    return a - b

# multiply(a,b) is expecting two input paramters `a` and `b` and will return them multiplied together
def multiply(a,b):
    print(f"Multiplying {a} and {b}!")
    return a * b

# divide(a,b) is expecting two input paramters `a` and `b` and will return dividing `a` by `b`
def divide(a,b):
    print(f"Dividing {a} by {b}!")
    return a / b

# add(a,b) is expecting two input paramters `a` and `b` and will return them added together
def birthday(day, month, year):
    print(f"You were born on the {day} day of the month {month} in the year {year}")

# Main program `main()` is defined here:
def main():
    print("Program starting")
    birthday(9, "march", 1990)
    result = add(105,7)
    print(result)
    print(subtract(100,1000))
    print(multiply(10,10))
    print(divide(11,3))

# We call main() to start the program
main()