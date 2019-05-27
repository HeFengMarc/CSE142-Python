# In this program we are designing a Guessing game. I import the random function
# at the beginning of this program such that we can use it to determine the
# random interger. The user can play this game for infinite number of tries if
# they want to. At the end of this program, there are detailed information about
# the game.

import random

total_game = 0
total_guesses = 0
best_guesses = 0
# Build the three-line Haiku
print("Guessing game begins")
print("Hope you can enjoy the game")
print("Have fun and relax")
# Keep running the loop until the user said they do not want to play the game
# anymore. Count the number of game at the beginning of this loop
while True:
    total_game = total_game + 1
    print("I'm thinking of a number between 1 and 100...")
    rand_num = random.randint(1,101)
    guess_num = 0
    trying_time = 0
     # Counting the number of guesses for each term.
    while True:
        trying_time = trying_time + 1
        guess_num = input("Your guess? ")
        if int(guess_num) > rand_num:
            print("It's lower.")
        elif int(guess_num) < rand_num:
            print("It's higher.")
        else:
            if trying_time == 1:
                print("You got it right in 1 guess!")
            else:
                print("You got it right in " + str(trying_time) + " guesses!")
                total_guesses = total_guesses + trying_time
                if total_game == 1:
                    best_guesses = total_guesses
                else:
                    if total_guesses < best_guesses:
                        best_guesses = total_guesses
            break
    again_or_not = input("Do you want to try again? ")
    print()
    # If the user wants to play one more game, the while loop while keep running.
    # Otherwise, the whole loop will stop, and the detailed information about
    # this game will appear.
    if again_or_not.startswith('y') or again_or_not.startswith('Y'):
        continue
    else:
        print("Overall results:")
        print("Total games   =", total_game)
        print("Total guesses =", total_guesses)
        print("Guesses/game  =", round(total_guesses * 10/total_game)/10)
        exit()
