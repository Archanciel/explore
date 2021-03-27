import pandas as pd
import numpy as np

data = {'CAPITAL': [10000, 80000, 25000],
		'REVENUE': [500, 4200, 2500]}
df = pd.DataFrame(data=data)
df['YIELD %'] = df['REVENUE'] / df['CAPITAL'] * 100
df.loc['TOTAL'] = df[['CAPITAL', 'REVENUE']].sum(numeric_only=True, axis=0)
print(df.fillna(''))
