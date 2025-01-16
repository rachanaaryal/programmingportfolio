'''this program gives a set of bad passwords that cannot be set into the program'''


bad_passwords=['password','letmein', 'sesame','hello','justinbieber']

password1 = input("enter a password that is 8-12 characters long: ")

if len(password1) < 8 or len(password1) > 12:
    print("try again")

elif password1 in bad_passwords:
    print("password is predictable. try again")

else:
    password2 = input("enter your password again: ")

    if password1 == password2:
        print("password set")

    else:
        print("password do not match try again")