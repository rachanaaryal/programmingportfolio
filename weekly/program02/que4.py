'''this program gives how many sweets to give to each
pupil, and how many will be left over.'''

sweets = int(input("How many sweets are in the tub? "))
pupils = int(input("how many pupils are attending today? "))

sweetsPerPupil = sweets//pupils
leftoverSweet = sweets % pupils

print(f"each pupil will receive {sweetsPerPupil} sweet(s), and there will be {leftoverSweet} sweet(s) left over.")