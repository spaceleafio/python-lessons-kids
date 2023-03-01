import random

# picks a number between 1 and 100
x = random.randint(1,100)
gold = 0

# 10% chance
if x <= 10:
    print("You Scored!!")
    gold += 1000000

print(f'you have {gold} gold!')