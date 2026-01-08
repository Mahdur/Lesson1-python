text =input("Enter a string")
text2 = "Mahdur"
print(text2.find('u'))

revText = text[::-1]
text = revText

print("Reverse of Given String is:")
print(text)
#this print reverses the string so it is backwards
print(text[::2])
#this string takes every second letter
print(text[:3])
#this print takes the first 3 letters

print(text[-3:-1])
#this print takes the 4,5 letters

print(text[-3::])
#this print takes the last 3 letters

line = input("enter a string")


print(line[3::3])