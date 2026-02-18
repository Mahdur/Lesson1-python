import random
random_number= random.randint(1,21)
print(random_number)

attempts=3

while attempts > 0:
    userinput=int(input("enter a number between 1 and 20: "))  
    if userinput != random_number:
        attempts= attempts - 1
        if attempts == 0:
            print("too many tries")
    elif userinput == random_number:
        print("Congratulations you won")
        break
    elif userinput < random_number:
        print("Higher")
    elif userinput > random_number:
        print("lower")
        
