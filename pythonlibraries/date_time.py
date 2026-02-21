import random
import time

def getRandomDate(startDate, endDate ):
    print("Printing randome date between", startDate, " and ", endDate)
    randomGenerator = random.random()
    print("randomGenerator value is:" ,randomGenerator)
    dateFormat = '%m/%d/%Y'

    startTime = time.mktime(time.strptime(startDate, dateFormat))
    print("startTime= ",startTime)
    endTime = time.mktime(time.strptime(endDate, dateFormat))
    print("endTime= ",endTime)

    randomeTime = startTime + randomGenerator * (endTime - startTime)
    randomDate = time.strftime(dateFormat, time.localtime(randomeTime))
    return randomDate
print("Random Date = ", getRandomDate("1/1/2026", "12/12/2018"))
