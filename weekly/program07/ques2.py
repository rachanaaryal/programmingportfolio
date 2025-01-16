'''this program takes two words as parameters as returns a sorted list'''


def letters_in_either(word1, word2):
    return sorted(set(word1) | set(word2)) 

def letters_in_both(word1, word2):
    return sorted(set(word1) & set(word2))  

def letters_in_either_but_not_both(word1, word2):
    return sorted(set(word1) ^ set(word2)) 

word1 = input("Enter the first word: ").lower()  
word2 = input("Enter the second word: ").lower()

print(f"Letters in at least one of the words: {letters_in_either(word1, word2)}")
print(f"Letters in both words: {letters_in_both(word1, word2)}")
print(f"Letters in either but not both: {letters_in_either_but_not_both(word1, word2)}")
