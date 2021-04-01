import pandas as pd

# THIS VARIANT IS BETTER IN MY OPINION

OWNER = 'OWNER'
DEPWITHDR = 'DEP/WITHDR'
DATEFROM = 'DATE FROM'
DATETO = 'DATE TO'
CAPITAL = 'CAPITAL'
YIELD = 'YIELD AMT'
TOTAL = 'TOTAL'

addEmptyRow = False

df = pd.DataFrame({
	OWNER: 2*['JOE']+3*['ROB'],
	DEPWITHDR: [10000, 20000, 4000, 20000, -8000],
	CAPITAL: [10000, 30000, 4000, 24000, 16000],
	DATEFROM: ['2021-01-01', '2021-01-02', '2021-01-01', '2021-01-03', '2021-01-04'],
	DATETO: ['2021-01-01', '2021-01-05', '2021-01-02', '2021-01-03', '2021-01-05'],
	YIELD: [100, 1200, 80, 240, 320]
	})

print('SOURCE DATAFRAME\n')
print(df)
print()

newDf = pd.DataFrame(columns=[OWNER, DEPWITHDR, CAPITAL, DATEFROM, DATETO, YIELD])

currentOwner = df.loc[1, OWNER]

dfTotal = df.groupby([OWNER]).agg({DEPWITHDR:'sum', YIELD:'sum'}).reset_index()
totalIndex = 0

# deactivating SettingWithCopyWarning caueed by totalRow[OWNER] += ' total'
pd.set_option('mode.chained_assignment', None)

for index, row in df.iterrows():
	if currentOwner == row[OWNER]:
		newDf = newDf.append({OWNER: row[OWNER], 
							  DEPWITHDR: row[DEPWITHDR],
							  CAPITAL: row[CAPITAL],
							  DATEFROM: row[DATEFROM],
							  DATETO: row[DATETO],
							  YIELD: row[YIELD]}, ignore_index=True)
	else:
		totalRow = dfTotal.loc[totalIndex]
		totalRow[OWNER] += ' total'
		newDf = newDf.append(totalRow, ignore_index=True)
		totalIndex += 1
		
		if addEmptyRow:
			newDf = newDf.append({OWNER: '',
								  DEPWITHDR: '',
							     CAPITAL: '',
								  DATEFROM: '',
								  DATETO: '',
								  YIELD: ''}, ignore_index=True)
		newDf = newDf.append({OWNER: row[OWNER], 
							  DEPWITHDR: row[DEPWITHDR],
							  CAPITAL: row[CAPITAL],
							  DATEFROM: row[DATEFROM],
							  DATETO: row[DATETO],
							  YIELD: row[YIELD]}, ignore_index=True)
		currentOwner = row[OWNER]

totalRow = dfTotal.loc[totalIndex]
totalRow[OWNER] += ' total'
				
newDf = newDf.append(totalRow, ignore_index=True)

print('TARGET DATAFRAME\n')
print(newDf.fillna(''))
