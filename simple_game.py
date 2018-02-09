#!/usr/bin/env python3

import  random

number=random.randint(1,10)

tries=1

uname = input("Hello,What's your username?!")

print("Hello",uname +".",)

question = input("Would you like to play a game?(Y/N)")

if question =="N":
    print("Oh.okay")

if question=="Y":

    print("I'm thinking of a number between 1 & 10")

    guess=int(input("Have a guess"))

    if guess<number:
        print("Gauss lower...")

        if guess>number:
            print("Gauess higher...")
            while guess!=number:
                tries+=1
                guess=int(input("Try again..."))
            if guess<number:

                print("Gauss Higher...")
                if guess == number:

                    print("You're right you win!The number was",number,"and it's only ",tries,"tries");



