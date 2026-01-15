attempts=0
while attempts < 5:
    print("you can still login")
    attempts=attempts+1
    print(f"{5-attempts} attempts left")

word1="meditation"
for character in word1:
    print(character,end="-")

word2="encyclopedia"
print(word2 [::-1])
print(len(word2))
for w in word2[::-1]:
    print(w,end="-")
print()

#A natural number is any number from negative infinity to 0 and 0 to infinity
sum=0
# for i in range(10):
#     sum =sum+i
# print(sum)

i=0
while i < 10:
    sum=sum+i
    i = i+1
print(sum)

#Write a program that prints the multiplication table of a given number up to ten
#5x1=5
#5x2=10
#5x3=15
#5x4=20
#5x5=25
#5x

number=int(input("Enter a number"))
for i in range(1,11):
    print(f"{number}x{i}={number*i}")

integer=int(input("enter a number"))
for i in range(10,0,-1):
    print(f"{integer}x{i}={integer*i}")
   

