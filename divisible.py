
# a program that asks a user for two numbers and determines if the number divides
# evenly into the other

print("Let's play Divisible!\nPress '0' to quit at any time.")
print()

while True:
    try:
        num = int(input("Please give me your first number. "))
    except ValueError:
        print("Please enter a valid integer")
        continue
    if num == 0:
        print("Goodbye.")
        break
    try:
        check = int(input('Please give me your second number. '))
    except ValueError:
        print("Please enter a valid integer")
        continue
    if check == 0:
        print("Goodbye.")
        break
    elif num % check == 0:
        print(f"{num} divides evenly by {check}.")
    else:
        print(f"{num} does not divide evenly by {check}.")
    print()







