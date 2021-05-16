import numpy as np

def computeFiatYieldAmount(yieldPercentVector, 
						   yieldDaysVector, 
						   capCryptoAmountVector, 
						   fiatRate,
						   yieldDaysNumber):
	return ((np.power(1 + (yieldPercentVector / 100), yieldDaysNumber / yieldDaysVector) * \
			 capCryptoAmountVector) - capCryptoAmountVector) * fiatRate

yieldDaysVector = np.array([46, 82, 107])
yieldPercentVector = np.array([1.2084124, 2.1643035, 2.83334233])
fiatRate = 1.5
capCryptoAmountVector = np.array([1000, 5000, 3000])

fiatYieldAmountDaily = computeFiatYieldAmount(yieldPercentVector,
											  yieldDaysVector,
											  capCryptoAmountVector,
											  fiatRate,
											  yieldDaysNumber=1)

fiatYieldAmountMonthly = computeFiatYieldAmount(yieldPercentVector,
											  yieldDaysVector,
											  capCryptoAmountVector,
											  fiatRate,
											  yieldDaysNumber=30)

fiatYieldAmountYearly = computeFiatYieldAmount(yieldPercentVector,
											  yieldDaysVector,
											  capCryptoAmountVector,
											  fiatRate,
											  yieldDaysNumber=365)


print(fiatYieldAmountDaily)
print(fiatYieldAmountMonthly)
print(fiatYieldAmountYearly)