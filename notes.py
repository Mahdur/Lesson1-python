Amount =int(input("Please enter the Amount for Withdraw"))

note_1 = Amount//100
note_2 = (Amount%100)//50
note_3 = ((Amount%100)%50)//10

print("Notes of $100" , note_1)
print("notes of $50" , note_2)
print("notes of $10" , note_3)