

def get_prime():
    """A function that asks the user for a number and tells them if it's a
    prime number."""
    guess = int(input("Give me a number and I will tell you if it's a prime number. "))
    for i in range(2, guess):
        if guess % i == 0:
            print(f"{guess} is not a prime number.")
            break
        else:
            print(f"{guess} is a prime number.")
            break

get_prime()





