'''this program requires the user to set a password that is atleast 8-12 characters long '''


password1 = input("enter a password that is 8-12 characters long: ")

if len(password1) < 8 or len(password1) > 12:
    print("try again")

else:
    password2 = input("eneter your password again")

    if password1 == password2:
        print("password set")

    else:
        print("password do not match try again")