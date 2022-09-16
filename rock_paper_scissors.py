
# two player rock paper scissors game

while True:
    print("Let's play Rock-Paper-Scissors!\nPress 'exit' to quit.")
    print()
    player_one = input("Player One, you go. ").lower()
    if player_one.lower() == "exit":
        print("Goodbye.")
        break
    player_two = input("It's your turn Player Two. ").lower()
    if player_two.lower() == "exit":
        print("Goodbye.")
        break
    elif player_one == "rock" and player_two == "scissors":
        print("Player One wins!")
    elif player_one == "scissors" and player_two == "paper":
        print("Player One wins!")
    elif player_one == "paper" and player_two == "rock":
        print("Player One wins!")
    else:
        print("Player Two wins!")
    print()






