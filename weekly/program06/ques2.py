'''this program gives thefcator of a positive integer'''


def factors(n):
    if n <= 0:
        return "Please provide a positive integer."

    factors = []
    for i in range(1, n + 1):
        if n % i == 0: 
            factors.append(i)
    return factors

number = int(input("Enter a positive integer: "))
if number <= 0:
    print("Please enter a positive integer.")
else:
    result = factors(number)
    print(f"The factors of {number} are: {result}")
