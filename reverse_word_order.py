
def reverse_string():
    """A function that takes input from a user and shows it to them backwards"""
    sentence = input("Please type any sentence and I'll show you it backwards. ")
    new_sentence = sentence[::-1]
    return new_sentence


print(reverse_string())