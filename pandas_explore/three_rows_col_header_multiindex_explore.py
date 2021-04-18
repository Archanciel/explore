import pandas as pd
import numpy as np

OWNER = 'OWNER'
DEPWITHDR = 'DEP/WITHDR'
CAPITAL = 'CAPITAL'
CHSB_DP_I = 'CHSB'
CHF_DP_I = 'CHF'
CHF_DP_C = ' CHF'
CHSB_C_C = ' CHSB'
CHF_C_C = '  CHF'
CHSB_Y = '  CHSB'
CHF_Y = '   CHF'
YIELD = 'YIELD AMT'
INIT = 'DT FROM RATE'
CURR = 'CURR RATE'


df = pd.DataFrame({
	OWNER: 4*['JPS']+2*['Papa'],
	CHSB_DP_I: [4422, 511, 2047, 300, 15941, 8973],
	CHF_DP_I: [2287, 366, 2867, 420, 15941, 8973],
	CHF_DP_C: [4152, 479, 1930, 284, 15941, 8973],
	CHSB_C_C: [4422, 4948, 7009, 7312, 15941, 8973],
	CHF_C_C: [4152, 4704, 6688, 6978, 15941, 8973],
	CHSB_Y: [14, 12, 2, 27, 92, 106],
	CHF_Y: [13, 11, 1.9, 25, 92, 106]
	})
	

print(df)

print('\nUsing pd.from_tuples()')
arrays = [
	np.array([' ', ' ', ' ', DEPWITHDR, ' ', CAPITAL, ' ', YIELD]),
	np.array([' ', ' ', INIT, CURR, ' ', CURR, ' ', CURR]),
	np.array([OWNER, CHSB_DP_I, CHF_DP_I, CHF_DP_C, CHSB_C_C, CHF_C_C, CHSB_Y, CHF_Y])
]
tuples = list(zip(*arrays))
index = pd.MultiIndex.from_tuples(tuples)
df.columns = index
pd.set_option('display.max_columns', None)
print(df)