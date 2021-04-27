import pandas as pd

CRYPTO = 'CHSB'
DF_RATE = 'AT DF RT'
CUR_RATE = 'AT CUR RT'
POTENTIAL_CAP_GAIN = 'POT CAP G'
AVERAGE_RATE = 'AVG RT'
REALIZED_CAP_GAIN = 'REALI CAP G'
YIELD_CHSB = 'Y CHSB'
YIELD_CHF = 'Y CHF'

df = pd.DataFrame({CRYPTO: [10000.0, 10000.0, 1000.0, -500.0, -500, 1000, -22531.55],
				   DF_RATE: [5000.0, 10000.0, 2000.0, -500.0, -1000, 800, -41500],
				   AVERAGE_RATE: [0.0] * 7,
				   CUR_RATE: [15000.0, 15000.0, 1500.0, -750.0, -750, 1500, -33797.325],
				   YIELD_CHSB: [155.26, 163.82, 167.66, 170.62, 162.54, 712.55, 0.10],
				   YIELD_CHF: [232.88, 245.72, 251.50, 255.93, 243.82, 1068.82, 0.15],
				   REALIZED_CAP_GAIN: [0.0] * 7,
				   POTENTIAL_CAP_GAIN: [0.0] * 7})
				   
print(df.to_string())
currentTotalCrypto = 0
currentTotalDfRate = 0
currentTotalCurRate = 0
currentAverageRate = 0
currentTotalYieldCrypto = 0
currentCryptoFiatRate = df.iloc[0][CUR_RATE] / df.iloc[0][CRYPTO]

for index, row in df.iterrows():
	depWithdrAmount = row[CRYPTO]
	currentTotalCrypto += depWithdrAmount
	currentTotalCurRate += row[CUR_RATE]
	currentTotalYieldCrypto += row[YIELD_CHSB]
	
	if depWithdrAmount > 0:
		currentTotalDfRate += row[DF_RATE]
		currentAverageRate = currentTotalDfRate / currentTotalCrypto
		df.iloc[index][POTENTIAL_CAP_GAIN] = currentTotalCurRate - \
											 (currentTotalCrypto * currentAverageRate) 
	else:
		df.iloc[index][REALIZED_CAP_GAIN] = -1 * (row[DF_RATE] - \
											depWithdrAmount * currentAverageRate)
		potentialCapitalGain = currentTotalCurRate - \
							   (currentTotalCrypto * currentAverageRate)
		if potentialCapitalGain < 0:
			potentialCapitalGain = round(currentTotalCurRate - \
							   (currentTotalCrypto * currentCryptoFiatRate), 6)
		df.iloc[index][POTENTIAL_CAP_GAIN] = potentialCapitalGain
				
	df.iloc[index][AVERAGE_RATE] = currentAverageRate
	
print(df.to_string())
