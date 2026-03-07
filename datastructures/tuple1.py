# create a tuple using ()
#number_tuple

# prints the items in the tuple
mytuple= (10, 20, 25.75, True, 'Mahdur')
print(mytuple)


#prints the length of the items in the tuple
print(f"The length of my tuple is {len(mytuple)}")


#prints the tuple horizontly
for i in range(5):
    print(mytuple[i],end=' ')

#names the item in the tuple
print(mytuple[0])

print(mytuple[3])

print(mytuple[-1])

#slicing
print(mytuple[3:7])

#mytuple(2) = 'G'
#print(mytuple[2])

#concatenation
tuple1 = 'P', 'Y', 'T', 'H', 'O', 'N'
tuple2 = (1, 2, 3)

#concatention
print(tuple1 + tuple2)

nest_tup = (1, 2, ('a', 'b'), [4,5,'nesting'])

print(nest_tup)

print(nest_tup[2])
print(nest_tup[-1][-1])



tuplex = ['tuple', False, 3.2, 1]
print(tuplex)

tuplex = [4, 6, 2, 8, 1]
print(tuplex)

tuple1 = (50, 10, 60, 70, 50)
print(tuple1.count(50))

tuplex = (2, 4, 3, 5, 4, 6, 7, 8, 6, 1)
_slice = tuplex[3:5]
print(_slice)
_slice = tuplex[2:6]
print(_slice)