import pandas as pd

OWNER = 'OWNER'
DEPWITHDR = 'DEP/WITHDR'
DATEFROM = 'FROM'
DATETO = 'TO'
CAPITAL = 'CAPITAL'
YIELD = 'YIELD AMT'
TOTAL = 'TOTAL'

df = pd.DataFrame({
	OWNER: 2*['JOE']+3*['ROB'],
	DEPWITHDR: [10000, 20000, 4000, 20000, -8000],
	CAPITAL: [10000, 30000, 4000, 24000, 16000],
	DATEFROM: ['2021-01-01', '2021-01-02', '2021-01-01', '2021-01-03', '2021-01-04'],
	DATETO: ['2021-01-01', '2021-01-05', '2021-01-02', '2021-01-03', '2021-01-05'],
	YIELD: [100, 300, 40, 240, 160]
	})

print(df)
print()

newDf = pd.DataFrame(columns=[OWNER, DEPWITHDR, CAPITAL, DATEFROM, DATETO, YIELD])

#print(newDf)
currentOwner = df.loc[1, OWNER]
totalDepWithdr = 0
totalYield = 0

for index, row in df.iterrows():
	if currentOwner == row[OWNER]:
		newDf = newDf.append({OWNER: row[OWNER], 
							  DEPWITHDR: row[DEPWITHDR],
							  CAPITAL: row[CAPITAL],
							  DATEFROM: row[DATEFROM],
							  DATETO: row[DATETO],
							  YIELD: row[YIELD]}, ignore_index=True)
		totalDepWithdr += row[DEPWITHDR]
		totalYield += row[YIELD]
	else:
		newDf = newDf.append({OWNER: TOTAL + ' ' + currentOwner,
							  DEPWITHDR: totalDepWithdr,
						 	 CAPITAL: '',
							  DATEFROM: '',
							  DATETO: '',
							  YIELD: totalYield}, ignore_index=True)
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
		totalDepWithdr = row[DEPWITHDR]
		totalYield = row[YIELD]
		
newDf = newDf.append({OWNER: TOTAL + ' ' + currentOwner,
					  DEPWITHDR: totalDepWithdr,
				 	 CAPITAL: '',
					  DATEFROM: '',
					  DATETO: '',
					  YIELD: totalYield}, ignore_index=True)
	
print(newDf)
