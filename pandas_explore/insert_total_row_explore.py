import pandas as pd
import numpy as np

OWNER = 'OWNER'
CAPITAL = 'CAPITAL'
YIELD = 'YIELD'
TOTAL = 'TOTAL'

df = pd.DataFrame({OWNER: ['JPS', 'JPS', 'PAPA', 'PAPA', 'BEA'], 
				   CAPITAL: [10000, 5000, 20000, 4000, 3000],
				   YIELD: [1000, 500, 2000, 400, 300]})
print(df)
print()

dfByOwner = df.groupby(by=(OWNER))

for owner, group in dfByOwner:
	print(owner)
	print(group[[CAPITAL, YIELD]])
	print(TOTAL, group[CAPITAL].agg(np.sum), group[YIELD].agg(np.sum))	
	#print(group[[CAPITAL, YIELD]].agg(np.sum))	

print()

print(dfByOwner[CAPITAL].agg(np.sum))

print()

df = pd.DataFrame({'case_type':['Service']*20+['chargeback']*9,'claim_type':['service']*5+['local_charges']*5+['service_not_used']*5+['supplier_service']*5+['service']*8+['local_charges']})
print(df)
df_out = df.groupby(by=["case_type", "claim_type"])["case_type"].count()

(pd.concat([df_out.to_frame(),
           df_out.sum(level=0).to_frame()
                 .assign(claim_type= "total")
                 .set_index('claim_type', append=True)])
  .sort_index())
  
print(df_out)

