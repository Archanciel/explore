import pandas as pd

OWNER = 'OWNER'
DEPWITHDR = 'DEP/WITHDR'
DATEFROM = 'FROM'
DATETO = 'TO'
CAPITAL = 'CAPITAL'
YIELD = 'YIELD AMT'
TOTAL = 'TOTAL'

df = pd.DataFrame({
	OWNER: 2*['JOE']+3*['ROB']+['BOB']*2,
	DEPWITHDR: [10000, 20000, 4000, 20000, -8000, 5000,-2000],
	CAPITAL: [10000, 30000, 4000, 24000, 16000, 5000, 3000],
	DATEFROM: ['2021-01-01', '2021-01-02', '2021-01-01', '2021-01-03', '2021-01-04', '2021-01-03', '2021-01-04'],
	DATETO: ['2021-01-01', '2021-01-05', '2021-01-02', '2021-01-03', '2021-01-05', '2021-01-03', '2021-01-04'],
	YIELD: [100, 300, 40, 240, 160, 50, 20]
	})

print(df)
print()

# first way
aggDic = {DEPWITHDR: 'sum', YIELD: 'sum'}
groupByDf = df.groupby([OWNER]).agg(aggDic).reset_index()
print(groupByDf)
excludeRow = ~groupByDf[OWNER].str.contains('OB')
groupByDf = groupByDf[excludeRow].reset_index()
print(groupByDf)

# second way
dfFiltered = df.loc[~df[OWNER].str.contains('OB')]
print(dfFiltered)
groupByDfFiltered = dfFiltered.groupby([OWNER]).agg(aggDic).reset_index()
print(groupByDfFiltered)

