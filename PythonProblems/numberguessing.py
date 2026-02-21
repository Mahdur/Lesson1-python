import random

computor_number = random.randint(1, 100)
guess = 0   

while guess != computor_number:
    guess = int(input("Choose a number 1-100: "))

    if guess < computor_number:
        print("Higher")
    elif guess > computor_number:
        print("Lower")
    else:
        print("You got the answer")




