'''this program creates a function that accepts a single
integer as a parameter and returns True if the integer is in the range 0 to 100, 
or False otherwise '''

def integer(n):
    return 0<= n <=100

numbers = [1, -1, 50, 0, 99, 100, -50]

for number in numbers:
    print(f"is {number} within the range 0 to 100? {integer(number)}")