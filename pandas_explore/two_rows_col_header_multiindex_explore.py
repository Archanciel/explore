import pandas as pd

OWNER = 'OWNER'
CAPITAL = 'CAPITAL'
USD = 'USD'
CHF = 'CHF'
YIELD = 'YIELD AMT'

df = pd.DataFrame({
	OWNER: 2*['JOE']+3*['ROB'],
	USD: [10000, 30000, 4000, 24000, 16000],
	CHF: [9000, 27000, 3600, 21600, 14400],
	YIELD: [100, 300, 40, 240, 160]
	})

print(df)
'''
  OWNER    USD    CHF  YIELD AMT
0   JOE  10000   9000        100
1   JOE  30000  27000        300
2   ROB   4000   3600         40
3   ROB  24000  21600        240
4   ROB  16000  14400        160
'''

df.columns = pd.MultiIndex.from_product([[CAPITAL], df.columns])
print('\nUsing pd.from_product()')
print(df)
'''
  CAPITAL                        
    OWNER    USD    CHF YIELD AMT
0     JOE  10000   9000       100
1     JOE  30000  27000       300
2     ROB   4000   3600        40
3     ROB  24000  21600       240
4     ROB  16000  14400       160
'''

# HOW DO I OBTAIN THIS ?
'''
                CAPITAL                        
    OWNER    USD    CHF YIELD AMT
0     JOE  10000   9000       100
1     JOE  30000  27000       300
2     ROB   4000   3600        40
3     ROB  24000  21600       240
4     ROB  16000  14400       160
'''

df_ok = pd.DataFrame({
	OWNER: 2*['JOE']+3*['ROB'],
	USD: [10000, 30000, 4000, 24000, 16000],
	CHF: [9000, 27000, 3600, 21600, 14400],
	YIELD: [100, 300, 40, 240, 160]
	})

df_ok.columns = pd.MultiIndex.from_arrays([[' ', ' ', CAPITAL, ' '], df_ok.columns])

print('\nUsing pd.from_arrays()')
print()
print(df_ok)
'''
                CAPITAL                        
    OWNER    USD    CHF YIELD AMT
0     JOE  10000   9000       100
1     JOE  30000  27000       300
2     ROB   4000   3600        40
3     ROB  24000  21600       240
4     ROB  16000  14400       160
'''

csvFileName = 'multiindex.csv'
dfFile = pd.read_csv(csvFileName, header=[0, 1])
print('\nFrom {}'.format(csvFileName))
print(dfFile)
'''
                CAPITAL                        
    OWNER    USD    CHF YIELD AMT
0     JOE  10000   9000       100
1     JOE  30000  27000       300
2     ROB   4000   3600        40
3     ROB  24000  21600       240
4     ROB  16000  14400       160
'''
