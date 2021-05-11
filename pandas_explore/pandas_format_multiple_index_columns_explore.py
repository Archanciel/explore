import pandas as pd
import numpy as np
print(pd.__version__)
df = pd.DataFrame(dict(
    recruit_dt=["1/1/2017"]*3+["1/1/2018"]*3+["1/1/2019"]*3,
    label = [1,3,4]*3,
    nmem = np.random.choice(list(range(10000,3000000)),9),
    pct_fem = np.random.sample(9),
    mean_age = 50 + 10*np.random.sample(9),
    sd_age = 8 + 2*np.random.sample(9)
))

print(df.to_string())

dfp = pd.pivot_table(df, values=["nmem","pct_fem","mean_age","sd_age"], index="recruit_dt", columns="label")
dfp = dfp.reindex(columns=['nmem', 'pct_fem', 'mean_age', 'sd_age'], level=0)

dfpCopy = dfp.copy()

print(dfp.to_string())

dfp.columns.names = ["metrics","label"]
dfp.style.format("{:,}", subset=pd.IndexSlice[:,'nmem']) \
		 .format("{:.2%}", subset=pd.IndexSlice[:,'pct_fem']) \
		 .format("{:.2f}", subset=pd.IndexSlice[:,['mean_age','sd_age']])

print(dfp.to_string())

idx = pd.IndexSlice
formatter_dict = {i:"{:,}" for i in dfpCopy.loc[:, idx['nmem', :]].columns}
formatter_dict2 = {i:"{:.2%}" for i in dfpCopy.loc[:, idx['pct_fem', :]].columns}
formatter_dict3 = {i:"{:.2f}" for i in dfpCopy.loc[:, idx[['mean_age', 'sd_age'], :]].columns}
formatter_dict.update(formatter_dict2)
formatter_dict.update(formatter_dict3)
dfpCopy.style.format(formatter_dict)
print(dfpCopy.to_string())