my_set = {1, 2, 3, 3, 4, 5, 5, 5 }

print(my_set)

my_set.add(7)
print("below is my set 1 \n",my_set)

my_set2 = {1, 2, 2, 3, 3, 3, 5, 5, 6, 6, 7, 7, 7}
print("Below is my set 2 \n",my_set2)
print("Below is the common element between these 2 sets using common intersection")
print(my_set.intersection(my_set2))

# union prints all the numbers used in both set and intersection only prints the numbers repeated in both sets
print(my_set.union(my_set2 ))
