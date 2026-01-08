
attempts = 3
while attempts > 0:
    Password = input("What is the password")

    
    if Password == "Mahdur":    
        print("You logged in succesfully")
        break
    else:
        print("Incorrect Password try again")
        attempts=attempts-1
        print(f"{attempts} attempts left")
