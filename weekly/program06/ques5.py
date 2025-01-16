'''this program give the interval time used to encrypt the message'''

import random
import string

def encrypt_message_with_gaps(message):
    interval = random.randint(2, 20)
    
    encrypted_message = []
    for i in range(len(message)):
        encrypted_message.append(message[i]) 
        if (i + 1) % interval == 0:
            random_letter = random.choice(string.ascii_lowercase)  
            encrypted_message.append(random_letter)
    encrypted_message_str = ''.join(encrypted_message)
    
    return encrypted_message_str, interval

message = input("Enter a message to encrypt: ")
encrypted_message, interval = encrypt_message_with_gaps(message)

print(f"Encrypted message: {encrypted_message}")
print(f"Interval used: {interval}")
