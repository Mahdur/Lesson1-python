def welcome():
    print("welcome")
welcome()

def welcome(name,age):
    print(f"welcome{name} congratulation for turning {age}")
welcome(" Mahdur", 15)

#print total bill and total bill contains 10 percent tip
bill=float(input("enter the bill"))
tip=float(input("enter your tip in percentage of base bill range from 0-0.5"))
def money(bill,tip):
    print(f"your bill is{bill} and your tip is{tip}")
    print("your total bill is", (bill*tip)+bill)
money(bill,tip)
