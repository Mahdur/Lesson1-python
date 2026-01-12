choice=input("you are stranded on an island, do you enter the island or not").lower()
if choice == "enter":
    shipwreck=input("you enter the island into a forest you cross the forest and go to a beach and find a shipwreck do you check it out?").lower()
    if shipwreck == "check":
        phone=input("You find a phone number do you call it?")
        if phone == "call":
            print("you got saved you win! ")
        elif phone == "no":
            print("you are stuck for an eternity you lose")
        else:
            print("you stood for too long you loose")
    elif shipwreck == "no":
        print("you are stuck in the island forever you loose")
    else:
        print("you stood too long you lose")
if choice == "no":
    print("you get stranded forever you loose")



    
