import pandas as pd
import numpy as np

yieldDic = {'DATE': ['2021-01-01','2021-01-02', '2021-01-03', '2021-01-04', '2021-01-05'],
			'RATE': [0, 0.0004, 0.00045, 0.00042, 0.00043]}
df = pd.DataFrame(data=yieldDic)
df['CAPITAL'] = [1000, 0, 0, 0, 0]
df['YIELD'] = [0, 0, 0, 0, 0]
maxIdx = len(df)
lastRowIdx = maxIdx - 1

for i in range(0, maxIdx):
	capital = df.loc[i, 'CAPITAL']
	yieldAmount = capital * df.loc[i, 'RATE']
	df.loc[i, 'YIELD'] = yieldAmount
	capYield = capital + yieldAmount
	df.loc[i, 'CAPITAL'] = capYield
	if i < lastRowIdx:
		df.loc[i + 1, 'CAPITAL'] = capYield

print(df)
randomYearlyInterestRates = np.random.uniform(low=1.15, high=1.25, size=(50))
randomDailyInterestRates = np.power(randomYearlyInterestRates, 1/365)
print(randomDailyInterestRates)
