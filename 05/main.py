# LESSON 5
# IMPORTS, EGG GAME SETUP

# IMPORTS
import os # let's us execute command line commands
import time # let's us add time delays

# CLEAR SCREEN WHEN PROGRAM STARTS
os.system('clear')

# DEFINE VARIABLES
gold = 0
eggs = 0
price = 250
discount = 50
reward = 100
exp = 0
energy = 100
delay = 1
cheat = True
discounted = False
running = True

# START GAME LOOP
while running:
    # TODO add discount to price if exp > 5
    if discounted == False:
        if exp >= 5:
            price -= discount
            discounted = True

    # setup program display
    print("WELCOME TO EGG WORLD!!!\n")
    print("Inventory")
    print(f"gold: {gold} | eggs: {eggs} | energy: {energy} | exp: {exp} \n")
    print(f"1. Do Quest - cost: 100 energy")
    print(f"2. Buy Egg - cost: {price} gold")
    print(f"3. Sleep - restores 100 energy")
    print("4. Quit\n")

    # get player input
    choice = input("Select an option (1, 2, 3 or 4): ")

    # check player input and display correct logic
    # if player enters 1... Do Quest
    if choice == '1':
        if energy >= 100:
            print("Doing Quest!")
            time.sleep(delay) 
            print(f"Quest Complete! exp and gold received!")
            time.sleep(delay+1) 
            os.system('clear')
            # TODO increase gold by reward amount
            gold += reward
            # TODO add 1 exp
            exp += 1
            # TODO reduce energy by 100
            energy -= 100
        else:
            print("Not enough energy, try sleeping.")
            time.sleep(delay) 
            os.system('clear')

    # if player enters 2... Buy Egg if player has enough gold
    elif choice == '2':
        if gold >= price:
            print("Buying Egg!")
            time.sleep(delay)
            os.system('clear')
            # TODO increase eggs by 1
            eggs += 1
            # TODO decrease gold by egg_price
            gold -= price
        else:
            print("Not enough money, try doing some quests.")
            time.sleep(delay)
            os.system('clear')

    # if player enters 3... Sleep and regain energy
    elif choice == '3':
        print("Sleeping...ZZZZZZZZZZ!")
        time.sleep(0.2)
        print("3...")
        time.sleep(0.6)
        print("2..")
        time.sleep(0.6)
        print("1.")
        time.sleep(0.6)
        print("Done! I feel more energetic!")
        time.sleep(delay)
        os.system('clear')
        # TODO increase energy by 100
        energy += 100

    # if player enters 4... Exit Program (while loop)
    elif choice == '4':
        #exit the while loop
        running = False 

    # if player enters superman... player found hidden cheat code
    elif choice == 'superman':
        if cheat:
            print("You found the cheatcode...here is some money")
            time.sleep(delay)
            os.system('clear')
            # TODO increase gold by 250
            gold += 250
            # TODO lock cheat code after 1 use
            cheat = False
        else:
            print("You already used the cheat code!")
            time.sleep(delay)
            os.system('clear')

    # if player enters anything else, try again
    else:
        print("choose a valid option...")
        time.sleep(delay)
        os.system('clear')

# while loop has exited, continue program...
print("\nThanks for playing!")
time.sleep(delay+1)
os.system('clear')