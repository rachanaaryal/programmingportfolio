'''this program creates a function that has a single string as its parameter, and returns the number of
uppercase letters, and the number of lowercase letters in the string'''


def letters(s):
    
    uppercase = sum(1 for char in s if char.isupper())
    lowercase = sum(1 for char in s if char.islower())
    return uppercase, lowercase

string = input("Enter a string: ")
upper_count, lower_count = letters(string)

print(f"The string contains {upper_count} uppercase letter(s) and {lower_count} lowercase letter(s).")
