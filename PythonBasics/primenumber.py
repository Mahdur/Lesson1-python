number = int(input("enter a numberr"))

if number <= 1:
    print("Not Prime")
else:
    

    for i in range(2, number):
        if number % i == 0:
            print("no")