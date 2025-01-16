'''this program return password set when the user sets a password 
and confirms the password again'''

password1 = input("eneter a password: ")
password2 = input("eneter the password again")

if password1 == password2:
    print("password set!!!")

else:
    print("passwords do not match. try again. ")