import pandas as pd

OWNER = 'OWNER'
CAPITAL = 'CAPITAL'
YIELD = 'YIELD AMT'
TOTAL = 'TOTAL'

# defining the dataframe
df = pd.DataFrame({OWNER: 2 * ['Joe'] + 3 * ['Carla'] + ['Rob'],
                   CAPITAL: [10000, 5000, 20000, 3000, -4000, 2000],
                   YIELD: [1000, 500, 2000, 300, 400, 200]})
'''
   OWNER  CAPITAL  YIELD AMT
0    Joe    10000       1000
1    Joe     5000        500
2  Carla    20000       2000
3  Carla     3000        300
4  Carla    -4000        400
5    Rob     2000        200
'''

print(df)
print()

# grouping the rows by owner
dfg = df.groupby([OWNER]).sum().reset_index()
'''
   OWNER  CAPITAL  YIELD AMT
0  Carla    19000       2700
1    Joe    15000       1500
2    Rob     2000        200
'''

print(dfg)
print()

# adding a TOTAL column (see alternative solution below !)
for index in range(0, len(dfg)):
	dfg.loc[index, TOTAL] = dfg.loc[index, CAPITAL] + dfg.loc[index, YIELD]
'''
   OWNER  CAPITAL  YIELD AMT    TOTAL
0  Carla    19000       2700  21700.0
1    Joe    15000       1500  16500.0
2    Rob     2000        200   2200.0
'''

print(dfg)
print()

# resetting index to OWNER column
dfg = dfg.set_index(OWNER)
'''
       CAPITAL  YIELD AMT    TOTAL
OWNER
Carla    19000       2700  21700.0
Joe      15000       1500  16500.0
Rob       2000        200   2200.0
'''

print(dfg)
print()

# finally, adding a TOTAL row
dfg.loc[TOTAL] = dfg.sum(numeric_only=True, axis=0)[[CAPITAL, YIELD, TOTAL]]
'''
       CAPITAL  YIELD AMT    TOTAL
OWNER
Carla  19000.0     2700.0  21700.0
Joe    15000.0     1500.0  16500.0
Rob     2000.0      200.0   2200.0
TOTAL  36000.0     4400.0  40400.0
'''

print(dfg.fillna(''))

# Alternative solution
df_2 = pd.DataFrame({OWNER: 2 * ['Joe'] + 3 * ['Carla'] + ['Rob'],
                   CAPITAL: [10000, 5000, 20000, 3000, -4000, 2000],
                   YIELD: [1000, 500, 2000, 300, 400, 200]})
print('\nAlternative solution\n')
print(df_2)

df_2[TOTAL] = df_2[CAPITAL] + df_2[YIELD]
output = df_2.groupby(by=[OWNER]).sum()
print(output)