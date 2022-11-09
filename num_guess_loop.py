# !/usr/bin/env python3
# Created by: Carolyn Webster Pless
# Created on: 2022/11/08
# Generates a random number then takes the user
# Input of a number. Uses a do..While loop and a break
# Statement to loop getting the user input

import random


def main():

    # Title
    print("Guess the number!\n")

    # Random number
    correct_number = random.randint(0, 9)

    # "DO... WHILE" loop to loop getting the user input
    while True:
        # User Input
        user_guess_str = input("Please enter a number between 0 and 9:")

        # To make sure the input is an integer
        try:
            user_guess_int = int(user_guess_str)

        # Exception which tells the user to enter an integer
        except Exception:
            print("Your number must be an integer!")

        else:
            if user_guess_int >= 0 and user_guess_int <= 9:
                if user_guess_int == correct_number:
                    print("You have guessed the number!")
                    break
                else:
                    print("You have guessed incorrectly. Please try again!")
            else:
                print("Please enter a whole number between 0 and 9! ")


if __name__ == "__main__":
    main()
