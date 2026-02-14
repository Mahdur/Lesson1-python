try:
    num1, num2 = eval(input("enter two numbers, seperated by a coma : "))
    result=num1 / num2
    print("Result is", result)

except ZeroDivisionError: 
    print("Division by zero is error !!")

except SyntaxError:
    print("Coma is missing. Enter numbers seperated by coma like this 1, 2")

except:
    print("Wrong Input")

else:
    print("No exceptions")

finally:
    print("this will execute no matter what")


