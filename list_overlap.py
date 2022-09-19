
# a program that creates two random lists and then prints the common numbers
import random

random_list_1 = random.sample(range(0, 100), 10)
random_list_2 = random.sample(range(0, 100), 15)
print(random_list_1)
print(random_list_2)
print()

common_list = set(random_list_1) & set(random_list_2)
common_list = list(common_list)
print(common_list)







