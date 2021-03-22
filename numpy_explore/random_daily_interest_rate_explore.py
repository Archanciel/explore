import numpy as np

# generating an array of random values in the range of 1.15 - 1.25,
# i.e. returns between 15 % and 25 % per annum
randomYearlyInterest = np.random.uniform(low=1.15, high=1.25, size=(50))
print(randomYearlyInterest)
print()

# obtaining an array of corresponding daily interest rates which are 
# 365th root of a yearly interest rate
randomDailyInterest = np.power(randomYearlyInterest, 1/365)
print(randomDailyInterest)