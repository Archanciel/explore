import pandas as pd
import numpy as np

data = [{'a': 1, 'b': 2, 'c': 54},{'a': 5, 'b': 10, 'c': 20}]
df = pd.DataFrame(data, index=['first', 'second'])
print(df)
print()
meanDf = df.apply(np.mean, axis=1)
print(meanDf)
addDf = pd.concat([df, meanDf], axis=1)
print(addDf)