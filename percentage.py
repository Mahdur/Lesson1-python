print("enter marks obtained in 4 subjects: ")
math = int(input("english :"))
english = int(input("Maths :"))
science = int(input("science :"))
history = int(input("History :"))

sum = math+english+science+history
print("sum of math,english,science and history")

perc = (sum/400)*100

print(end="Percentage Mark =")
print(perc)
