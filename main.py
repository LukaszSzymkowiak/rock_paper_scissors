""" Rock, paper, scissors game"""

from functions import *


# main
def main():
    print("Rock, paper, scissors game!")
    sleep(1)
    start_time = datetime.now()
    game()
    end_time = datetime.now()
    play_time = game_time(start_time, end_time)
    print(f"Game time: {play_time:.2f} seconds")


if __name__ == '__main__':
    main()
