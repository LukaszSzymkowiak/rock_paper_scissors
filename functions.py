from random import *
from datetime import datetime
from time import sleep


# game time
def game_time(start, end):
    return (end - start).total_seconds()


# game
def game():
    equipment = {"r": "rock", "p": "paper", "s": "scissors"}
    user_points = 0
    computer_points = 0
    n = int(input("Set max points for game: "))
    while user_points < n and computer_points < n:
        print(f"Points\n"
              f"User: {user_points}\n"
              f"Computer: {computer_points}\n")
        user_choice = input("'r' for rock\n"
                            "'p' for paper\n"
                            "'s' for scissors\n"
                            "Choose: \n").lower()
        if user_choice in equipment:
            print(f"Your choice is {equipment[user_choice]}")
            computer_choice = choice(list(equipment.keys()))
            print(f"Computer choice is {equipment[computer_choice]}\n")
            if user_choice == "r" and computer_choice == "s":
                print("You win!\n")
                user_points += 1
            elif user_choice == "p" and computer_choice == "r":
                print("You win!\n")
                user_points += 1
            elif user_choice == "s" and computer_choice == "p":
                print("You win!\n")
                user_points += 1
            elif user_choice == computer_choice:
                print("Draw!\n")
            else:
                print("Computer win!\n")
                computer_points += 1
        else:
            print("Incorrect command.\n")

    print(f"Points\n"
          f"User: {user_points}\n"
          f"Computer: {computer_points}\n")
