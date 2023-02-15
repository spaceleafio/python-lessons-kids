# LESSON 4
# INPUTS & WHILE LOOPS

#------------------------- basic program loop
running = True
while running:
    # setup program options and get user selection (input)
    print("1. Do Quest")
    print("2. Buy Egg")
    print("3. Quit")
    choice = input("Select an option (1, 2 or 3): ")

    # check user input and display correct logic
    # if user enters 1... Do Quest
    if choice == '1':
        print("Doing Quest!")

    # if user enters 2... Buy Egg
    elif choice == '2':
        print("Buying Egg!")

    # if user enters 3... Exit Program (while loop)
    elif choice == '3':
        print("Quitting!")
        #exit the while loop
        running = False 

    # if user enters superman... User found hidden cheat code
    elif choice == 'superman':
        print("You found the cheatcode...")

    # if user enters anything else, try again
    else:
        print("choose a valid option...")


# while loop has exited, continue program...
print("Game Over")








# First reference examples, uncomment lines between ---- to execute:
#------------------ basic input
# x = input("Enter something cool: ")
# print(f"You entered: {x}")
#------------------ basic while loop
# count = 10000
# while count > 0:
#     print(count)
#     count = count - 1
# print("Program Over")