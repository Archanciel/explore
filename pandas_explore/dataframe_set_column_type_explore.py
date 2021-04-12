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


# setting cell value
df.iat[0, 1] = 10003.5

print(df)
print()

print(df.info())

# set col type as float64, otherwise, setting cell value to 10003.5 will result as setting it
# to 10003 !
df = df.astype({CAPITAL: 'float64'})

# setting cell value
df.iat[0, 1] = 10003.5

print(df)
print()
print(df.info())
