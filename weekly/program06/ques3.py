'''this program finds out if a number is prime or not'''

def prime(n):
    if n <= 1:
        return False  
    for i in range(2, n):  
        if n % i == 0: 
            return False
    return True  

number = int(input("enter an integer: "))

if prime(number):
    print(f"{number} is a prime number.")
else:
    print(f"{number} is not a prime number.")
