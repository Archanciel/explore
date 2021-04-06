import pandas as pd

data = [{'cap': 1000, 'rev': 20},{'cap': 5000, 'rev': 150}]

df_index_1 = pd.DataFrame(data, index=range(1, len(data) + 1))
print(df_index_1)

df_index_default = pd.DataFrame(data)
print(df_index_default)