import pandas as pd

# THIS VARIANT IS BETTER IN MY OPINION

OWNER = 'OWNER'
CAPITAL_USD = 'CAPITAL USD'
YIELD_USD = 'YIELD USD'
CAPITAL_CHF = 'CAPITAL CHF'
YIELD_CHF = 'YIELD CHF'
CAPITAL_EUR = 'CAPITAL EUR'
YIELD_EUR = 'YIELD EUR'
CAPITAL_DM = 'CAPITAL DM'
YIELD_DM = 'YIELD DM'

df = pd.DataFrame({OWNER: ['John', 'John', 'John', 'John', 'John', 'John', 'Rob', 'Rob', 'Rob', 'Rob', 'Rob',
						   'Rob', 'Rob', 'Rob', 'Tom', 'Tom', 'Tom', 'Tom', 'Tom', 'Tom', 'Bob', 'Bob', 'Bob',
						   'Bob', 'Bob'],
				   CAPITAL_USD: [10000, 5000, 20000, 4000, 3000] * 5,
				   YIELD_USD: [1000, 500, 2000, 400, 300] * 5,
				   CAPITAL_CHF: [10000, 5000, 20000, 4000, 3000] * 5,
				   YIELD_CHF: [1000, 500, 2000, 400, 300] * 5,
				   CAPITAL_EUR: [10000, 5000, 20000, 4000, 3000] * 5,
				   YIELD_EUR: [1000, 500, 2000, 400, 300] * 5,
				   CAPITAL_DM: [10000, 5000, 20000, 4000, 3000] * 5,
				   YIELD_DM: [1000, 500, 2000, 400, 300] * 5})

# Summing USD, CHF and D( columns
dfGroupOwnerTotal = df.groupby([OWNER]).agg({CAPITAL_USD: 'sum',
											 YIELD_USD: 'sum',
											 CAPITAL_CHF: 'sum',
											 YIELD_CHF: 'sum',
											 CAPITAL_DM: 'sum',
											 YIELD_DM: 'sum'})
totalDf = pd.DataFrame(columns=[OWNER,
								CAPITAL_USD,
								YIELD_USD,
								CAPITAL_CHF,
								YIELD_CHF,
								CAPITAL_EUR,
								YIELD_EUR,
								CAPITAL_DM,
								YIELD_DM])
currentOwner = df.loc[1, OWNER]
totalDfIndex = 0

# deactivating SettingWithCopyWarning caueed by totalRow[OWNER] += ' total'
pd.set_option('mode.chained_assignment', None)

for index, row in df.iterrows():
	if currentOwner == row[OWNER]:
		totalDf = totalDf.append({OWNER: row[OWNER],
								  CAPITAL_USD: row[CAPITAL_USD],
								  YIELD_USD: row[YIELD_USD],
								  CAPITAL_CHF: row[CAPITAL_CHF],
								  YIELD_CHF: row[YIELD_CHF],
								  CAPITAL_EUR: row[CAPITAL_EUR],
								  YIELD_EUR: row[YIELD_EUR],
								  CAPITAL_DM: row[CAPITAL_DM],
								  YIELD_DM: row[YIELD_DM]}, ignore_index=True)
	else:
		totalRow = dfGroupOwnerTotal.loc[currentOwner]
		totalDf = totalDf.append(totalRow, ignore_index=True)
		totalDf.iloc[totalDfIndex][OWNER] = currentOwner + ' total'
		
		# overwriting DM capital total by a non numeric string title
		totalDf.iloc[totalDfIndex][CAPITAL_DM] = 'Total yield DM'
		
		totalDfIndex += 1
		totalDf = totalDf.append({OWNER: row[OWNER],
								  CAPITAL_USD: row[CAPITAL_USD],
								  YIELD_USD: row[YIELD_USD],
								  CAPITAL_CHF: row[CAPITAL_CHF],
								  YIELD_CHF: row[YIELD_CHF],
								  CAPITAL_EUR: row[CAPITAL_EUR],
								  YIELD_EUR: row[YIELD_EUR],
								  CAPITAL_DM: row[CAPITAL_DM],
								  YIELD_DM: row[YIELD_DM]}, ignore_index=True)
		currentOwner = row[OWNER]
	totalDfIndex += 1

totalRow = dfGroupOwnerTotal.loc[currentOwner]
totalDf = totalDf.append(totalRow, ignore_index=True)
totalDf.iloc[totalDfIndex][OWNER] = currentOwner + ' total'

print('TARGET DATAFRAME\n')
print(totalDf.fillna('').to_string())
