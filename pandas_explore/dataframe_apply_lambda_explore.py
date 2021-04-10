import pandas as pd
import numpy as np

df = pd.DataFrame([[10, 100, np.nan, 1000]] * 5, columns=['one', 'two', 'three', 'four'])
print(df)
df = df.apply(lambda x: x * 1.1 if x.name in ['two', 'three', 'four'] else x)
#df = df.apply(lambda x: x * 2.1 if x.name in ['one'] else x)
df = df.apply(lambda x: x * 2.1 if x.name == 'one' else x)

print(df)