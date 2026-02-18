import random
random_number= random.randint(1,21)
print(random_number)

game = True
while game == True:
    userinput=int(input("enter a number between 1 and 20: "))
    if userinput == random_number:
        print("Congratulations you won")
        game = False
    elif userinput < random_number:
        print("Higher")
    elif userinput > random_number:
        print("lower")
        
