#take 2 input one for numerator and one for denominator and check 
# using if else condition if they are divisible or not. If denominator is 0 print wrong input

numerator = int(input("enter a numerator"))
denominator = int(input("enter a denominator"))

if denominator == 0:
    print("wrong input")
elif numerator%denominator == 0:
    print("This is divisible")
else:
    print("its not divisible")


   