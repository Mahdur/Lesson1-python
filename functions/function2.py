def addition(a,b):
    return a+b
print(addition)

def subtraction(a,b):
    return a-b
print(subtraction(10,8))

def multiply(a,b):
    return a**b
print(multiply(10,4))

def divide(a,b):
    return a/b
print(divide(20,4))

num1=int(input("enter your first number"))
num2=int(input("enter your second number"))
operation=input("Choose operation out of A D M S")
if operation == "A":
    print(addition(num1,num2))
elif operation == "D":
    print(divide(num1,num2))
elif operation == "M":
    print(multiply(num1,num2))
elif operation == "S":
    print(subtraction(num1,num2))




