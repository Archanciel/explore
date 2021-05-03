import pandas as pd

CRYPTO = 'CHSB'
DF_RATE = 'AT DF RT'
CUR_RATE = 'AT CUR RT'
AVERAGE_RATE = 'AVG RT'
REALIZED_CAP_GAIN = 'REALI CAP G'
REALIZED_CAP_GAIN_PERCENT = 'REALI CAP G %'
POTENTIAL_CAP_GAIN = 'POT CAP G'
POTENTIAL_CAP_GAIN_PERCENT = 'POT CAP G %'
YIELD_CHSB = 'Y CHSB'
YIELD_CUR_RATE = 'Y CUR RATE'

SELL_ALL_DEPOSIT_SELL_ALL_YIELD = 'SELL_ALL_DEPOSIT_SELL_ALL_YIELD'
SELL_ALL_DEPOSIT_SELL_ONLY_ONE_YIELD = 'SELL_ALL_DEPOSIT_SELL_ONLY_ONE_YIELD'
SELL_ALL_DEPOSIT_SELL_1000_YIELDS = 'SELL_ALL_DEPOSIT_SELL_1000_YIELDS'
SELL_ALL_DEPOSIT_SELL_ALL_MINUS_ONE_YIELD = 'SELL_ALL_DEPOSIT_SELL_ALL_MINUS_ONE_YIELD'
SELL_ALL_DEPOSIT_SELL_NO_YIELD = 'SELL_ALL_DEPOSIT_SELL_NO_YIELD'

def computeDataFrameAmounts(sellType,
							droppedColLst):
	if sellType == SELL_ALL_DEPOSIT_SELL_ALL_YIELD:
		df = pd.DataFrame({CRYPTO: [10000.0, 10000.0, 1000.0, -500.0, -500, 1000, -22532.55],
						   DF_RATE: [5000.0, 10000.0, 2000.0, -500.0, -1000, 800, -25200 - 1839.06],
						   AVERAGE_RATE: [0.0] * 7,
						   CUR_RATE: [0.0] * 7,
						   YIELD_CHSB: [155.26, 163.82, 167.66, 170.62, 162.54, 712.55, 0.10],
						   YIELD_CUR_RATE: [0.0] * 7,
						   REALIZED_CAP_GAIN: [0.0] * 7,
						   REALIZED_CAP_GAIN_PERCENT: [0.0] * 7,
						   POTENTIAL_CAP_GAIN: [0.0] * 7,
						   POTENTIAL_CAP_GAIN_PERCENT: [0.0] * 7})
	elif sellType == SELL_ALL_DEPOSIT_SELL_ALL_MINUS_ONE_YIELD:
		df = pd.DataFrame({CRYPTO: [10000.0, 10000.0, 1000.0, -500.0, -500, 1000, -22531.55],
						   DF_RATE: [5000.0, 10000.0, 2000.0, -500.0, -1000, 800, -25200 - 1837.86],
						   AVERAGE_RATE: [0.0] * 7,
						   CUR_RATE: [0.0] * 7,
						   YIELD_CHSB: [155.26, 163.82, 167.66, 170.62, 162.54, 712.55, 0.10],
						   YIELD_CUR_RATE: [0.0] * 7,
						   REALIZED_CAP_GAIN: [0.0] * 7,
						   REALIZED_CAP_GAIN_PERCENT: [0.0] * 7,
						   POTENTIAL_CAP_GAIN: [0.0] * 7,
						   POTENTIAL_CAP_GAIN_PERCENT: [0.0] * 7})
	elif sellType == SELL_ALL_DEPOSIT_SELL_1000_YIELDS:
		df = pd.DataFrame({CRYPTO: [10000.0, 10000.0, 1000.0, -500.0, -500, 1000, -22000],
						   DF_RATE: [5000.0, 10000.0, 2000.0, -500.0, -1000, 800, -25200 - 1200],
						   AVERAGE_RATE: [0.0] * 7,
						   CUR_RATE: [0.0] * 7,
						   YIELD_CHSB: [155.26, 163.82, 167.66, 170.62, 162.54, 712.55, 0.10],
						   YIELD_CUR_RATE: [0.0] * 7,
						   REALIZED_CAP_GAIN: [0.0] * 7,
						   REALIZED_CAP_GAIN_PERCENT: [0.0] * 7,
						   POTENTIAL_CAP_GAIN: [0.0] * 7,
						   POTENTIAL_CAP_GAIN_PERCENT: [0.0] * 7})
	elif sellType == SELL_ALL_DEPOSIT_SELL_ONLY_ONE_YIELD:
		df = pd.DataFrame({CRYPTO: [10000.0, 10000.0, 1000.0, -500.0, -500, 1000, -21001],
						   DF_RATE: [5000.0, 10000.0, 2000.0, -500.0, -1000, 800, -25200 - 1.2],
						   AVERAGE_RATE: [0.0] * 7,
						   CUR_RATE: [0.0] * 7,
						   YIELD_CHSB: [155.26, 163.82, 167.66, 170.62, 162.54, 712.55, 0.10],
						   YIELD_CUR_RATE: [0.0] * 7,
						   REALIZED_CAP_GAIN: [0.0] * 7,
						   REALIZED_CAP_GAIN_PERCENT: [0.0] * 7,
						   POTENTIAL_CAP_GAIN: [0.0] * 7,
						   POTENTIAL_CAP_GAIN_PERCENT: [0.0] * 7})
	elif sellType == SELL_ALL_DEPOSIT_SELL_NO_YIELD:
		# the last sell is done at CRYPTO/FIAT rate of 1.2 which differs from the current
		# CRYPTO/FIAT rate of 1.5 !
		df = pd.DataFrame({CRYPTO: [10000.0, 10000.0, 1000.0, -500.0, -500, 1000, -21000],
						   DF_RATE: [5000.0, 10000.0, 2000.0, -500.0, -1000, 800, -25200],
						   AVERAGE_RATE: [0.0] * 7,
						   CUR_RATE: [0.0] * 7,
						   YIELD_CHSB: [155.26, 163.82, 167.66, 170.62, 162.54, 712.55, 0.10],
						   YIELD_CUR_RATE: [0.0] * 7,
						   REALIZED_CAP_GAIN: [0.0] * 7,
						   REALIZED_CAP_GAIN_PERCENT: [0.0] * 7,
						   POTENTIAL_CAP_GAIN: [0.0] * 7,
						   POTENTIAL_CAP_GAIN_PERCENT: [0.0] * 7})

	print('\n')
	print(sellType)
	print()
	dfToPrint = df.copy()
	dfToPrint.drop(droppedColLst, axis='columns', inplace=True)

	print(dfToPrint.to_string())

	currentTotalDepositCryptoAmount = 0
	previousCurrentTotalDepositCryptoAmount = 0
	currentDepositCryptoAverageFiatRateModifiedOnlyWhenNewPurchase = 0
	currentTotalYieldCrypto = 0
	currentCryptoFiatRate = 1.5
	
	for index, row in df.iterrows():
		depWithdrCryptoAmount = row[CRYPTO]
		depWithdrCryptoAmountAtDateFromFiatRate = row[DF_RATE]
		currentTotalDepositCryptoAmount += depWithdrCryptoAmount
		depWithdrCryptoAmountAtCurrentFiatRate = depWithdrCryptoAmount * currentCryptoFiatRate
		row[CUR_RATE] = depWithdrCryptoAmountAtCurrentFiatRate
		yieldCryptoAmount = row[YIELD_CHSB]
		df.iloc[index][YIELD_CUR_RATE] = yieldCryptoAmount * currentCryptoFiatRate
		currentTotalYieldCrypto += yieldCryptoAmount
		currentTotalDepositCryptoAmountAtAverageFiatRate = currentTotalDepositCryptoAmount * currentDepositCryptoAverageFiatRateModifiedOnlyWhenNewPurchase

		if depWithdrCryptoAmount > 0:
			# we are depositing (purchasing) cryptos ...
			if previousCurrentTotalDepositCryptoAmount == 0:
				# here, we are handling the very first deposit/purchase
				currentDepositCryptoAverageFiatRateModifiedOnlyWhenNewPurchase = depWithdrCryptoAmountAtDateFromFiatRate / \
																				 currentTotalDepositCryptoAmount
			else:
				# here, we are handling one of the next deposit/purchase
				currentDepositCryptoAverageFiatRateModifiedOnlyWhenNewPurchase = (previousCurrentTotalDepositCryptoAmount * currentDepositCryptoAverageFiatRateModifiedOnlyWhenNewPurchase + \
																				  depWithdrCryptoAmountAtDateFromFiatRate) / \
																				 currentTotalDepositCryptoAmount
			potentialCapitalGain = (currentTotalDepositCryptoAmount * currentCryptoFiatRate) + \
								   (currentTotalYieldCrypto * currentCryptoFiatRate) - \
								   currentTotalDepositCryptoAmount * currentDepositCryptoAverageFiatRateModifiedOnlyWhenNewPurchase
			if currentTotalDepositCryptoAmountAtAverageFiatRate != 0:
				potentialCapitalGainPercent = potentialCapitalGain / \
											  currentTotalDepositCryptoAmountAtAverageFiatRate * 100
			else:
				potentialCapitalGainPercent = 0.0
		else:
			# this is a withdrawal (or sale)...

			# the realized capital gain is equal to the sold crypro amount converted at the
			# crypto/fiat rate at the sell date minus the sold crypro amount converted at the
			# average crypto/fiat rate valid at the sell date, i.e. at the fiat average cost of
			# all the crypto amounts purchased before the sell date.
			if currentTotalDepositCryptoAmount < 0:
				withdrawalCryptoAmountWithoutSoldYieldAmount = depWithdrCryptoAmount - currentTotalDepositCryptoAmount
				realizedCapitalGain = -1 * depWithdrCryptoAmountAtDateFromFiatRate - -1 * withdrawalCryptoAmountWithoutSoldYieldAmount * currentDepositCryptoAverageFiatRateModifiedOnlyWhenNewPurchase
				df.iloc[index][REALIZED_CAP_GAIN] = realizedCapitalGain
				realizedCapitalGainPercent = -100 * realizedCapitalGain / \
											 currentTotalDepositCryptoAmountAtAverageFiatRate

				# the case if not only the current deposit crypto amount has been sold, but also
				# part of or all the accumulated yield crypto amounts
				potentialCapitalGain = (currentTotalDepositCryptoAmount + currentTotalYieldCrypto) * \
										currentCryptoFiatRate
				potentialCapitalGainPercent = -100 * potentialCapitalGain / \
											  currentTotalDepositCryptoAmountAtAverageFiatRate
			else:
				realizedCapitalGain = -1 * depWithdrCryptoAmountAtDateFromFiatRate - -1 * depWithdrCryptoAmount * currentDepositCryptoAverageFiatRateModifiedOnlyWhenNewPurchase
				df.iloc[index][REALIZED_CAP_GAIN] = realizedCapitalGain
				potentialCapitalGain = (currentTotalDepositCryptoAmount * currentCryptoFiatRate) + \
									   (currentTotalYieldCrypto * currentCryptoFiatRate) - \
									   currentTotalDepositCryptoAmountAtAverageFiatRate
				if currentTotalDepositCryptoAmountAtAverageFiatRate != 0:
					realizedCapitalGainPercent = realizedCapitalGain / \
												 currentTotalDepositCryptoAmountAtAverageFiatRate * 100
					potentialCapitalGainPercent = potentialCapitalGain / \
												  currentTotalDepositCryptoAmountAtAverageFiatRate * 100
				else:
					realizedCapitalGainPercent = 0.0
					potentialCapitalGainPercent = 0.0

			df.iloc[index][REALIZED_CAP_GAIN_PERCENT] = realizedCapitalGainPercent

		df.iloc[index][POTENTIAL_CAP_GAIN] = round(potentialCapitalGain, 8)	# rounding avoid data frame
																			# potential capital gain values
																			# exponential formatting
		df.iloc[index][POTENTIAL_CAP_GAIN_PERCENT] = round(potentialCapitalGainPercent, 8)	# rounding avoid data frame
																							# potential capital gain values
																							# exponential formatting

		df.iloc[index][AVERAGE_RATE] = currentDepositCryptoAverageFiatRateModifiedOnlyWhenNewPurchase
		previousCurrentTotalDepositCryptoAmount = currentTotalDepositCryptoAmount

	# drop columns
	dfToPrint = df.copy()
	dfToPrint.drop(droppedColLst, axis='columns', inplace=True)

	print(dfToPrint.to_string())

#droppedColLst = []
droppedColLst = [REALIZED_CAP_GAIN_PERCENT,
				 POTENTIAL_CAP_GAIN_PERCENT]

computeDataFrameAmounts(SELL_ALL_DEPOSIT_SELL_ALL_YIELD, droppedColLst)
computeDataFrameAmounts(SELL_ALL_DEPOSIT_SELL_ALL_MINUS_ONE_YIELD, droppedColLst)
computeDataFrameAmounts(SELL_ALL_DEPOSIT_SELL_1000_YIELDS, droppedColLst)
computeDataFrameAmounts(SELL_ALL_DEPOSIT_SELL_ONLY_ONE_YIELD, droppedColLst)
computeDataFrameAmounts(SELL_ALL_DEPOSIT_SELL_NO_YIELD, droppedColLst)

