
# a program that asks the user a word and tells them if it's a palindrome.
word = input("Let's test if a word is a palindrome!\nTell me a word. ")

if word[::-1] == word[::]:
    print("That word is a palindrome.")
else:
    print("That word is not a palindrome.")







