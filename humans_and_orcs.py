
# A program that will play the “Humans and Orcs” game with the user. The game works like this:
# Randomly generate a 4-digit number. Ask the user to guess a 4-digit number. For every digit that the
# user guessed correctly in the correct place, they have a “human”. For every digit the user guessed
# correctly in the wrong place is a “orc.” Every time the user makes a guess, tell them how many
# “humans” and “orcs” they have. Once the user guesses the correct number, the game is over. Keep track
# of the number of guesses the user makes throughout the game and tell the user at the end.

# Say the number generated by the computer is 1038. An example interaction could look like this:
#   Welcome to the Humans and Orcs Game!
#   Enter a number:
#   >>> 1234
#   2 humans, 2 orcs
#   >>> 1256
#   1 human, 3 orcs

import random

def compare_numbers(computer_number, user_guess):
    """A function that takes a string and sorts matching items at corresponding indexes."""
    human_orc = [0, 0] # humans, then orcs
    for i in range(len(computer_number)):
        if computer_number[i] == user_guess[i]:
            human_orc[0] += 1 # human
        else:
            human_orc[1] += 1 # orc
    return human_orc

print("Let's play a game called Humans and Orcs.\n"
      "I will generate a number and you have to guess the numbers one digit at a time.\n"
      "For every number in the right place you get a Human.\n"
      "For every number in the wrong place, you get an Orc.\n"
      "The game ends when you get 4 Humans.\n"
      "type 'exit' to quit playing.")
print()

random_number = str(random.randint(1000, 9999)) # random 4 digit number
guesses = 0

while True:
    user_guess = input("Please give me 4 numbers. ")
    human_orc_count = compare_numbers(random_number, user_guess)
    if user_guess.lower() == "exit":
        print("Goodbye.")
        break
    else:
        print(f"You have {human_orc_count[0]} humans and {human_orc_count[1]} orcs.")
        guesses += 1
    if human_orc_count[0] == 4:
        print(f"You win! You got it in {guesses} guesses.")
        break
    else:
        print("Please try again.")










