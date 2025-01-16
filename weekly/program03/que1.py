'''this program prints "hello stranger" as output 
if the user enters blank in their name'''

name = input("hello, what is your name? ")
if name.strip() == "":
    print("hello, stranger!")
else:
    print(f"hello, {name}. good to meet you!")
    