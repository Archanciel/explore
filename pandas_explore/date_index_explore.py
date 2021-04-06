import pandas as pd

DATE = 'DATE'
CAPITAL = 'CAPITAL'
EARNING = 'EARNING'

df = pd.DataFrame({DATE: ['2021/01/01', '2021/01/02', '2021/01/03'],
				   CAPITAL: [1000, 5000, 3000],
				   EARNING: [10, 50, 30]})
df = df.set_index(DATE)
				   
print(df)
print(df.iloc[-1][CAPITAL] + df.iloc[-1][EARNING])