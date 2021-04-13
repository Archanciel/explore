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
#		newDf = newDf.append({OWNER: '',
#							  DEPWITHDR: '',
#						 	 CAPITAL: '',
#							  DATEFROM: '',
#							  DATETO: '',
#							  YIELD: ''}, ignore_index=True)
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

# Alternative solution
print('\nAlternative solution\n')

df2 = pd.DataFrame({
	OWNER: 2*['JOE']+3*['ROB'],
	DEPWITHDR: [10000, 20000, 4000, 20000, -8000],
	CAPITAL: [10000, 30000, 4000, 24000, 16000],
	DATEFROM: ['2021-01-01', '2021-01-02', '2021-01-01', '2021-01-03', '2021-01-04'],
	DATETO: ['2021-01-01', '2021-01-05', '2021-01-02', '2021-01-03', '2021-01-05'],
	YIELD: [100, 300, 40, 240, 160]
	})

print(df2)
print()
df_total = pd.concat((
    df2,
    df2.replace({o: o + ' total' for o in df2[OWNER].unique()}).groupby(OWNER).agg({DEPWITHDR: sum, YIELD: sum}).reset_index())
).fillna('').reset_index().sort_values([OWNER, DATEFROM, DATETO])
print(df_total)
'''
Explanation:

df.replace({o: o + ' total' for o in df[OWNER].unique()}): 
replace each occurrence of the name of every owner with the name itself 
plus the string ' total' (e.g., 'JOE' -> 'JOE total'); so that the result of the 
groupby will have those values in the column OWNER.

groupby(OWNER).agg({DEPWITHDR: sum, YIELD: sum}): 
get the sum of the column DEPWITHDR and YIELD per each owner.

pd.concat(...).fillna('').reset_index().sort_values([OWNER, DATEFROM, DATETO]): 
concatenate the original DataFrame and that with the totals and then sort rows 
by column OWNER, than DATEFROM, than DATETO, so that the rows with the totals 
for each OWNER will be placed at the ends of the rows belonging to that owner 
(because they ends with ' total') and moreover the rows will be chronologically 
sorted by DATEFROM, DATETO.	
'''