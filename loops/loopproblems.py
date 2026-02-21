#Take a password as input and check if:
#It has at least 8 characters
#Contains at least one digit
#Print “Strong Password” or “Weak Password”.

password=input("Enter a Password")
isinteger=False
for character in password:
    if character.isdigit():
        isinteger=True
        
if len(password) >= 8 and isinteger == True:
    print("Strong password")
else:
    print("weak password")
