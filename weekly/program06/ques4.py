'''this program encrypts a message'''

def encrypt_message(message):
    message_no_spaces = message.replace(" ", "")
    reversed_message = message_no_spaces[::-1]
    
    return reversed_message

original_message = input("Enter a message to encrypt: ")
encrypted_message = encrypt_message(original_message)

print(f"Encrypted message: {encrypted_message}")
