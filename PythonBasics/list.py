mylist=["sydney",31.4,16,True]
for item in mylist:
    print(item)
mylist.append("sydney houses are amazing")
print(mylist)
mylist.insert(1,"skyscrapers")
print(mylist)
print(mylist[0:2])
print(mylist[1:2])
print(mylist[0])
print(mylist[4])
print(mylist[-1])
print(mylist[-2])
print(mylist[-3])
print(mylist[-4])
print(mylist[-5])
print(mylist[0:4:2])
mylist.remove(31.4)
print(mylist)
mylist.pop(-3)
print(mylist)

numbers = [3, 7, 2, 9, 4, 10, 1]
newlist=[]
for i in numbers:
    if i%2 == 0:
        print("The number is even")
        newlist.append(i)
print(newlist)



