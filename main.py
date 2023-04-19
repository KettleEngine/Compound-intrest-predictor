import random
import math


def predictionRun(start, added, years, rate, minimumRate, maximumRate):

  total = 0

  total = start * rate
  for i in range(years * 12 + 1):

    check = True
    while check == True:
      rateDecimal = random.random()
      rateNumber = random.randint(0, 1)
      rate = rateNumber + rateDecimal
      rate = math.ceil(rate * 100) / 100
      if rate >= minimumRate:
        check = False

    total = (total + added) * rate
    totalFormatted = '{:,.2f}'.format(total)
    #print("Rate: ", rate, " | month: ", i, " | total: ", totalFormatted)

    if total >= 1000000:
      return [i, total]


milMonth = []

predictionNum = 1000

for i in range(predictionNum):
  milMonth.append(predictionRun(50000, 0, 100, 0.8, 0.6, 1.4))

#print(milMonth)

months = []
ammount = []
for j in range(len(milMonth)):
  months.append(milMonth[j][0])
  ammount.append(milMonth[j][1])


def Average(month):
  return sum(month) / len(month)


avgAmount = Average(ammount)
avgAmount = '{:,.2f}'.format(avgAmount)

print("Average Month: ", Average(months))
print("Average Amount: ", avgAmount)
