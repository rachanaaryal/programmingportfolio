'''this program decrypts the encrypted message'''

import random

def decrypt_message(encrypted_message, interval):
    original_message = []
    for i in range(len(encrypted_message)):
        if (i + 1) % (interval + 1) != 0:  
            original_message.append(encrypted_message[i])
    
    decrypted_message = ''.join(original_message)
    
    return decrypted_message
message = input("Enter an encrypted message: ")
interval = int(input("Enter the interval used during encryption: "))

decrypted_message = decrypt_message(message, interval)

print(f"Decrypted message: {decrypted_message}")
