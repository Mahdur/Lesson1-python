list=["sydney","adelaid","perth", "darwin", "melbourne","brisbane"]
for city in list:
    if len(city)%2 == 0:
        print(city)
    
def printEvenCity(list):
    for city in list:
        if len(city)%2 == 0:
            return city

EvenCity=printEvenCity(list)
print(EvenCity)