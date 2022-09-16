
# creating a function that creates a random password and then asking the user how many characters
import string
import random

def pw_generator(size, chars=string.ascii_letters + string.digits + string.punctuation):
    """A function that creates a random password."""
    return "".join(random.choice(chars) for i in range(size))

while True:
    print(pw_generator(int(input("How many characters would you like in your password? "))))