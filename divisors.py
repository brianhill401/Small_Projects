
# A program that asks the user for a number and then prints
# out a list of all the divisors of that number.

user_choice = int(input("Please give me a number. "))
new_list = []
for i in range(1, user_choice + 1):
    if user_choice % i == 0:
        new_list.append(i)
print(new_list)