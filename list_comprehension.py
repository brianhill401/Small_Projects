
# a program that takes a list and makes a new list with only the
# even numbers in it.

list = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

new_list = [number for number in list if number % 2 == 0]

print(new_list)