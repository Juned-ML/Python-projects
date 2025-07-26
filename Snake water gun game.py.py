#this the game of snake water and gun 
#to refreash the chidhood memory to include in it

import random
name = input("enter your name here:")
print(f"ok Mr. {name} let's began the game of snake watr and gun")

player = input("enter your_choice(snake,water,gun):")
computer = random.choice(["snake:","water","gun"])

print(f"you choose {player} and computer {computer}")

if player == computer:
   print("result, is draw")

elif player == "snake" and  computer == "water":
    print(f"{name},you win")

elif player == "water" and computer == "gun":
    print(f"{name},you win")
     
elif player == "gun" and computer == "sanke":
 print(f"{name},you win")

else:
   print("opps!!! computer wins")





   





