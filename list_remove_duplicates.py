
# creates a function that removes duplicates from a list

def remove_duplicates_1(old_list):
    """A function that takes a list and eliminates all duplicates."""
    new_list = list(set(old_list))
    return new_list

a = [1, 1, 3, 9, 9, 7, 100]
print(remove_duplicates_1(a))












