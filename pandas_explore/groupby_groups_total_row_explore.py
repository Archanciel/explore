import pandas as pd
import numpy as np

OWNER = 'OWNER'
CAPITAL = 'CAPITAL'
YIELD = 'YIELD'
TOTAL = 'TOTAL'

df = pd.DataFrame({
"Group": 3*['X']+5*['Y'],
"Subgroup": 2*['a']+['z']+3*['a']+2*['z'],
"Value": [12, 4, 5, 7, 3, 14, 21, 8]
})

print(df)

df1 = df.assign(Subgroup=lambda x: "Total")

#print(df1)

df2 = df.assign(Group=lambda x: "Total", Subgroup=lambda x: "Total")

#print(df2)

df_subtotal = pd.concat([
    df,
    df.assign(Subgroup=lambda x: "Total"),
    df.assign(Group=lambda x: "Total", Subgroup=lambda x: "Total")
])

#print(df_subtotal)

df3 = pd.concat([
    df,
    df.assign(Subgroup=lambda x: "Total"),
    df.assign(Group=lambda x: "Total", Subgroup=lambda x: "Total")
]).groupby(by=['Group', 'Subgroup'], observed=True).sum()

print(df3)

cat_Group = pd.CategoricalDtype(categories=list(df['Group'].unique()) + ['Total'], ordered=True)
cat_Subgroup = pd.CategoricalDtype(categories=list(df['Subgroup'].unique()) + ['Total'], ordered=True)

df_subtotal['Group'] = df_subtotal['Group'].astype(cat_Group)
df_subtotal['Subgroup'] = df_subtotal['Subgroup'].astype(cat_Subgroup)
df4 = df_subtotal.groupby(by=['Group', 'Subgroup'], observed=True).sum()
print(df4)