# Snake, Water and Gun Game
'''
1 for snake
-1 for water
0 for gun
'''

import random

computer = random.choice([-1, 0, 1])
youstr = input("Enter your choice: ")
youDict = {'s': 1, 'w': -1, "g": 0}
reversedDict = {1: "Snake", -1: "Water", 0: "Gun"}

you = youDict[youstr]

# By now we have 2 number (variables), you and computer

print(f"You chose {reversedDict[you]} \nComputer chose {reversedDict[computer]}")

if(computer == you):
    print("Its a draw")

elif(computer == -1 and you == 1):
    print("You Win!")
    
elif(computer == -1 and you == 0):
    print("You Lose!")

elif(computer == 1 and you == -1):
    print("you Lose!")

elif(computer == 1 and you == 0):
    print("you Win!")
       
elif(computer == 0 and you == -1):
    print("you Win!")   
    
elif(computer == 0 and you == 1):
    print("you Lose!")   
    
else:
    print("Something want wrong")