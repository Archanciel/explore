import pandas as pd

OWNER = 'OWNER'
DEPWITHDR = 'DEP WITHDR'
YIELD = 'YIELD AMT'
DATE_TIME = 'DATE'
TOTAL = 'TOTAL'

# defining the dataframe
df = pd.DataFrame({OWNER: 2 * ['Joe'] + 3 * ['Carla'] + ['Rob'],
				   DATE_TIME: ['2021/01/01 00:00:00', '2021/01/02 00:00:00', '2021/01/03 00:00:00', '2021/01/04 00:00:00', '2021/01/05 00:00:00', '2021/01/06 00:00:00'],
                   DEPWITHDR: [10000, 5000, 20000, 3000, -4000, 2000],
                   YIELD: [1000, 500, 2000, 300, 400, 200]})

print(df)
print()

duplSeries = df.duplicated(subset=[DATE_TIME])

print(duplSeries)
print()

print('Is a datetime duplicated: ', duplSeries.any())

index = None

try:
	index = list(duplSeries).index(True)
except ValueError:
	pass
	
print(index)
