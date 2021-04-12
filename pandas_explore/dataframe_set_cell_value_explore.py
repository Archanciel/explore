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
	CAPITAL: [10000, 30000, 4000, 24000, 16000],
	DATEFROM: ['2021-01-01 00:00:00', '2021-01-02 00:00:00', '2021-01-01 00:00:01', '2021-01-03 00:00:00', '2021-01-04 00:00:00'],
	DATETO: ['2021-01-01', '2021-01-05', '2021-01-02', '2021-01-03', '2021-01-05'],
	YIELD: [100, 300, 40, 240, 160]
	})

# set col type as float64, otherwise, setting cell value to 10003.5 will result as setting it
# to 10003 !
df = df.astype({CAPITAL: 'float64'})

df = df.set_index(DATEFROM)
print(df)
print()

print(df.info())

# setting cell value
df.at['2021-01-01 00:00:00', CAPITAL] = 10003.5

print(df.info())
print(df)

print('\n---- D F 2 ----\n')

df2 = pd.DataFrame({
	OWNER: 2*['JOE']+3*['ROB'],
	CAPITAL: [10000, 30000, 4000, 24000, 16000],
	DATEFROM: ['2021-01-01 00:00:00', '2021-01-02 00:00:00', '2021-01-01 00:00:01', '2021-01-03 00:00:00', '2021-01-04 00:00:00'],
	DATETO: ['2021-01-01', '2021-01-05', '2021-01-02', '2021-01-03', '2021-01-05'],
	YIELD: [100, 300, 40, 240, 160]
	})

print(df2)
print()

print(df2.info())

# set col type as float64, otherwise, setting cell value to 10003.5 will result as setting it
# to 10003 !
df2 = df2.astype({CAPITAL: 'float64'})

# setting cell value
df2.iat[0, 1] = 10003.5

print(df2.info())
print(df2)

