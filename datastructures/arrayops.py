import array as arr

a=arr.array('1',[1,2,3])

print("/nThe new created array is :", end = "")
for i in range (0, 3):
    print (a[i], end = "")
print()

b = arr.array('d' [2.5, 3.2, 3.3])


a.insert(1, 4)

print ("\nArray after insertion : ", end ="")
for i in (a):
    print(i, en = "")
print()

b.append(4.4)

print("\nArray agyer insertion : ", end = "")
for i in (b):
    print (i, end = "")
print()

print("Access element is: ", a[0])
print("Access element is: ", b[2])
