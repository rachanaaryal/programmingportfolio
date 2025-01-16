'''this program executes until the user successfully
chooses a password'''

bad_passwords=['password','letmein', 'sesame','hello','justinbieber']


while True:

    password1 = input("enter a password that is 8-12 characters long: ")

    if len(password1) < 8 or len(password1) > 12:
        print("password must contain 8 to 12 characters, try again")

    elif password1 in bad_passwords:
        print("password is predictable. try again")

    else:
        password2 = input("enter your password again: ")

        if password1 == password2:
            print("password set")
            break

        else:
            print("password do not match try again")