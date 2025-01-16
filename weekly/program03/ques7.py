'''thos program print the table of 7 for the numbers between 0 to 12 only '''

number = int(input("enter any number from 0 to 12: "))

if 0<= number <=12:
    print(f"\nTimes tables for{number}: ")
    for i in range(13):
        print(f"{i} x {number} = {i* number}")

else:
    print("please enter a number between 0 and 12.")
