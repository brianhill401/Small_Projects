
# a game that asks the user to guess the number the computer generates
import random

number = random.randint(1, 10)
number_of_guesses = 1

while True:
    guess = input("Try to guess the number between 1 and 10.\nPress 'exit' to quit at any time. ")
    if guess.lower() == "exit":
        print("Goodbye")
        break
    elif int(guess) == number:
        print(f"You got it in {number_of_guesses} guesses.")
    elif int(guess) > number:
        print("You guessed too high, try again.")
    elif int(guess) < number:
        print("You guessed too low,try again.")
    number_of_guesses += 1
    print()








