import pandas as pd
import numpy as np

OWNER = 'OWNER'
DEPWITHDR = 'DEP/WITHDR'
SUBGROUP = 'From'
DATETO = 'TO'
CAPITAL = 'CAPITAL'
YIELD = 'YIELD'
TOTAL = 'TOTAL'

df = pd.DataFrame({
OWNER: 2*['JPS']+3*['Papa'],
#SUBGROUP: 2*['a']+['z']+3*['a']+2*['z'],
SUBGROUP: ['2021-01-01', '2021-01-02', '2021-01-01', '2021-01-03', '2021-01-04'], 
DATETO: [12, 4, 5, 7, 3],
#DATETO: ['2021-01-01', '2021-01-05', '2021-01-02', '2021-01-03', '2021-01-05'],
DEPWITHDR: [10000, 20000, 4000, 20000, -8000]
})

print(df)

df_subtotal = pd.concat([
    df,
    df.assign(From=lambda x: TOTAL),
    df.assign(OWNER=lambda x: TOTAL, From=lambda x: TOTAL)
])

print(df_subtotal)

cat_Group = pd.CategoricalDtype(categories=list(df[OWNER].unique()) + [TOTAL], ordered=True)
cat_Subgroup = pd.CategoricalDtype(categories=list(df[SUBGROUP].unique()) + [TOTAL], ordered=True)

df_subtotal[OWNER] = df_subtotal[OWNER].astype(cat_Group)
df_subtotal[SUBGROUP] = df_subtotal[SUBGROUP].astype(cat_Subgroup)
df4 = df_subtotal.groupby(by=[OWNER, SUBGROUP], observed=True).sum()
print(df4)