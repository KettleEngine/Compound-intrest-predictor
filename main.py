import random
import math


def predictionRun(start, added, years, rate, minimumRate, maximumRate, CheckNum):

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
    #total is not very easy to read so it gets formatted into an easyer to read format
    totalFormatted = '{:,.2f}'.format(total)

    #CheckNum checks for when it has hit a specific value and then saves the number of itterations it took to get there
    if total >= CheckNum:
      return [i, total]


milMonth = []

predictionNum = 1000

#allows me to run the prediction as many times as i want and therefor get an average
for i in range(predictionNum):
  milMonth.append(predictionRun(50000, 0, 100, 0.8, 0.6, 1.4, 1000000))

#stores the values of the months and ammounts. i chose to do it this way instead of a 2d array becasue the 2d array orriginally had issues with reading the correct data so instead i just made 2 1d arrays and it works fine
months = []
ammount = []
for j in range(len(milMonth)):
  months.append(milMonth[j][0])
  ammount.append(milMonth[j][1])

# this is here just to average the results of all the month values
def Average(month):
  return sum(month) / len(month)

#this then just formats it again so that it is not displaying like 8 decimal places
avgAmount = Average(ammount)
avgAmount = '{:,.2f}'.format(avgAmount)

#displays the data
print("Average Month: ", Average(months))
print("Average Amount: ", avgAmount)
