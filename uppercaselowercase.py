text=input("enter a word")


upper = 0
lower = 0

for ch in text:
    if ch >= 'A' and ch <= 'Z':
        upper += 1
    elif ch >= 'a' and ch <= 'z':
        lower += 1