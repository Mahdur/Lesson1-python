choice = input("do you go left or right or forward ").lower()

if choice == "left":
    print("You meet a divine sage")
    action = input("do you talk to him or ignore him? ").lower()

    if action == "talk":
        print("You get to learn alot game over")
    elif action == "ignore":
        print("you loose a lifetime of an oppurtunity")
    else:
        print("you are confused game over")

elif choice == "right":
    print("you see a dark cave")
    action = input("do you enter or run").lower()
    if action == "enter":
        print("You see a demon")
        fight = input("Do you fight or flee").lower()
        if fight == "fight":
            print("you fought bravely you win")
        elif fight == "flee":
            print("You escaped safely play next time")
        else:
            print("you hesitated too long game over")
    elif action == "run":
        print("you got scared game over")
    else:
        print("invalid choice game over")
elif choice == "forward":
    island = input("You see an island do you enter or not? ").lower()
    if island == "enter":
        treasure = input("you find treasure worth 1 million dollars do you collect it or not? ")
        if treasure == "collect":
            print("money was cursed you rot in hell game over")
        elif treasure == "not":
            print("you get 1 billion dollar of gold")
    elif island == "not":
        print("your stuck game over")
    
        
else:
    print("You stand still forever game over")



        



    
