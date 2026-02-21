#this program prints Vihaan can vte only when the age is equal to or larger than 18
#however it wont print anything if its less than 18
age = 18

if age >= 18:
    print("Vihaan can vote")

#below program will always print something.
#if age is greater than 10 

Mahdur_age = 14

if Mahdur_age >= 18:
    print("Vihaan can vote")
elif Mahdur_age >= 10:
    print("Vihaan can go to see the voting process")

    
 #this will always print something if age is greater than 9

age = 10

if age >= 18:
    print("Vihaan can vote")
elif age >= 11:
    print("Vihaan can go to see the voting process")
elif age >= 9:
    print("Vihaan can just watch a movie")

#Now it will always print something

age_mahdur = 10

if age_mahdur >= 18:
    print("Vihaan can vote")
elif age_mahdur >= 11:
    print("Vihaan can go to see the voting process")
elif age_mahdur >= 9:
    print("Vihaan can just watch a movie")
else:
    print("Vihaan can only play a game")

#Below is the program to check grade

score = int(input("What's your score"))

if score >= 85:
    print("you got an A")
elif score >= 70:
    print("You got a B")
elif score >= 50:
    print("you got a C")
else:
    print("you failed")