import pandas as pd
import numpy as np

data = [{'cap': 1000, 'rev': 20},{'cap': 5000, 'rev': 150}]
df = pd.DataFrame(data, index=['JPS', 'Papa'])

print(df)
df['yield %'] = df['rev'] / df['cap'] * 100
print(df)
