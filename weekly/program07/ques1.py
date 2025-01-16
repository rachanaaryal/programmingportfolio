'''this program sorts unique letter of a string'''

def letters(string):
    unique_letters = set(string)
    sorted_letters = sorted([char for char in unique_letters if char.isalpha()])
    
    return sorted_letters

test_string = input("Enter a string: ")
result = letters(test_string)

print(f"Sorted unique letters: {result}")