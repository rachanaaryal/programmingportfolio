'''this program converts the temperature taken in celsius to fahrenheit and vice versa'''


def celcius(temp1):
    return (temp1 * 9/5) + 32

def fahrenheit(temp2):
    return(temp2- 32) * 5/9

temp1 = float(input("enter temperature in celcius: "))
temp2 = float(input("enter temperature in fahrenheit: "))

print(f"{temp1}C is equal to {celcius(temp1)}F")
print(f"{temp2}F is equal to {fahrenheit(temp2)}C")