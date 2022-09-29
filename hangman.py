
# 1. loop max turn count 6
# 2. Get a guess
# 3. Check guess
# 4. Increase count if guess is wrong
# 5. Print correct letters
# 6. If they have all letters correct, break out of loop

# the word the user is trying to guess
answer_word = "PYTHON"
guesses = ""

# the number of guesses the user has
failed_guesses = 6

# loop until the player reaches max guesses
while failed_guesses > 0:

    # get the guess from the player
    print()
    player_guess = input("Please enter a letter: ")
    player_guess = player_guess.upper()

    if player_guess in answer_word:
        print(f"Awesome guess, there are one or more {player_guess}'s in the word.")
    else:
        failed_guesses -= 1
        print(f"I'm sorry, there are no {player_guess}'s in the word. You have {failed_guesses} guesses left.")

    # updates a list of all letters guessed
    guesses = guesses + player_guess
    wrong_letter_count = 0

    for letter in answer_word:
        if letter in guesses:
            print(f"{letter}", end="")
        else:
            print("_", end="")
            wrong_letter_count += 1


    # if there are no wrong letters left, the player wins
    if wrong_letter_count == 0:
        print()
        print("You did it, you won!")

print()
print("I'm sorry, you lose.")


