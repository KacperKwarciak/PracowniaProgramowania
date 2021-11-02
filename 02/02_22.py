import random
dice=random.randint(1,6)
guess=input("Guess the number from 1 to 6: ")
guess=int(guess)
if dice==guess:
    print("True")
else:
    print("False")