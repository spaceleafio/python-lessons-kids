# LESSON 3
# FUNCTIONS

# def first_function():
#     print("Hello from the function!")

# first_function()

# Defining Functions to use in our program
# add(a,b) is expecting two input paramters 'a' and 'b'
def add(a,b):
    print(f"Adding {a} and {b}!") 
    return a + b
    
def subtract(a,b):
    print(f"Subtracting {a} and {b}!")
    return a - b

def multiply(a,b):
    print(f"Multiplying {a} and {b}!")
    return a * b

def divide(a,b):
    print(f"Dividing {a} and {b}!")
    return a / b

def birthday(day, month, year):
    print(f"You were born on the {day} day of the month {month} in the year {year}")

# Main program instructions
def main():
    print("Program starting")
    birthday(9, "march", 1990)
    result = add(105,7)
    print(result)
    print(subtract(100,1000))
    print(multiply(10,10))
    print(divide(11,3))

# REAL PROGRAM START
main()