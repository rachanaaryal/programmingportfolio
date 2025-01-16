'''this program gives the binary value of an integer'''

def binary(n):
    if n < 0:
        print("The number must be positive!")
        return None

    binary = ""
    while n > 0:
        remainder = n % 2
        binary = str(remainder) + binary
        n = n // 2

    return binary

number = int(input("Enter a positive integer: "))
if number < 0:
    print("Please enter a positive number.")
else:
    binary_representation = binary(number)
    print(f"The binary representation of {number} is: {binary_representation}")
