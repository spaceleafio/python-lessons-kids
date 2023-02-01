# LESSON 02: Comparison Operators, CONDITIONAL Logic: If Statements, Else Statements, Elif Statements
# greater than: >                 3 > 1
# less than: <                    1 < 3
# equal: ==                       1 == 1
# greater than or equal to:      >=
# less than or equal to:         <=
# not equal to                   !=

# ASSIGNMENT: Do any if, elif, else code using any one of the comparison operators
# Update the current 



wallet = -10000000000000000000
price = 350
# if we have enough money in the wallet to buy the egg
if(wallet >= price):
    # print the success message
    print("Success, you bought the egg!")
    # subtract price from wallet 
    wallet = wallet - price
    print(wallet)
elif(wallet == 0):
    print("You have no money at all!")
elif(wallet < 0): # check if wallet is less than 0 ie: NEGATIVE
    print("NEGATIVE")
else:
    print("You don't have enough money!!")

print("THIS IS THE END")



# if(1 <= 1):
#     print("TRUE!!!")
# else:
#     print("FALSE!!!")


# variables can change
# gold = 0
# print(gold)
# gold = 200 
# print(gold)

