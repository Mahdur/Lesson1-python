import random
random_number= random.randint(1,10)
print(random_number)
userinput=int(input("enter a number between 1 and 10: "))
if userinput == random_number:
    print("Congratulations, YOU WON")
elif userinput != random_number:
    print("Try again")