'''this program processes a string representing a message and reports the six
most common letters, along with the number of times they appear'''


from collections import Counter

def frequency_analysis(message):
    message = message.lower()

    letter_counts = Counter(char for char in message if char.isalpha())

    most_common = letter_counts.most_common(6)

    return most_common

def main():
    print("Frequency Analysis Tool")
    print("Enter the encrypted message below:")
    
    message = input("> ")

    results = frequency_analysis(message)

    print("\nThe six most common letters are:")
    for letter, count in results:
        print(f"{letter}: {count} times")

main()
