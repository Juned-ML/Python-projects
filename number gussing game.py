print("this is a number gussing game for fun ")
import random

name = input("Enter your name: ")
print(f"ok MR.{name},let's start the game")
print("there are three levels in the game")
print("1. easy (1-25)")
print("2. medium (1-50)")
print("3. hard (1-100)")

choice = int(input("enter the choice that you want the level of game: "))
if choice == 1:
    number = random.randint(1, 25)
    print("you have 6 chances to guess the correct number")
    chances = 6
    for i in range(chances):
        guess = float(input("enter your guess number: "))
        if guess != number:
            print("you have", chances - i - 1, "chances left")  

            elif guess > number:
            print("too high!!")

            elif guess < number:
            print("too low!!")

        if guess == number:
            print("congratulations! you guessed the correct number")
            break

if choice == 2:
    number = random.randint(1,50)
    print("in this level you have 8 chances to guess correct number")
    chances = 8
    for i in range(chances):
        guess = float(input("enter your guess number: "))
        if guess != number:
            print("you have", chances -i-1,"chances left")

            elif guess > number:
            print("too high!!")

            elif guess < number:
            print("too low!!")

        if guess == number:
            print("congratulations! you guessed the correct number")
            break       

if choice == 3:
    number = random.randint(1,100)
    print("in this level you have 10 chances to guess correct number")
    chances = 10
    for i in range(chances):
        guess = float(input("enter your guess number: "))
        if guess != number:
            print("you have", chances - i - 1, "chances left")

            elif guess > number:
            print("too high!!")

            elif guess < number:
            print("too low!!")

        if guess == number:
            print("congratulations! you guessed the correct number")
            break