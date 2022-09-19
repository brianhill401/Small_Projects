
# a program that tells the user in what year they will turn 100 years old.

current_year = 2022
name = input("What is your name? ")
age = int(input(f"What is your age {name}? "))
expected_year = (100 - age) + current_year
print(f"You will turn 100 in " + str(expected_year) + " " + name + ".")
print()

