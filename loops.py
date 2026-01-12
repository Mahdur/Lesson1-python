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

