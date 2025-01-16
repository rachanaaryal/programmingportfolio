'''this program print the table of  any numbers between o to 12 but if the 
numbers that the user inputs is negative it prints the table backwards'''


number = int(input("enter any number from 0 to 12: "))

if -12 <= number <=12:

    print(f"\nTimes tables for{number}: ")
    if number<0:
        for i in range(12, -1, -1):
            print(f"{i} x {-number} = {i * -number}")
    else:
        for i in range(13):
            print(f"{i} x {number} = {i* number}")

else:
    print("please enter a number between 0 and 12.")
