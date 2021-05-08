import pandas as pd
import numpy as np

OWNER = 'OWNER'
NUMERIC_LABEL = 'NUMERIC'
FLOAT_LABEL = 'FLOAT'
PERCENT_LABEL = 'PERCENT'
TEXT_LABEL = 'TEXT'
LOCATION_LABEL = 'INVEST TOWN'
USD_LABEL = 'USD'
EUR_LABEL = 'EUR'
USA_LABEL = 'USA LOCATION'
FRANCE_LABEL = 'FRANCE LOCATION'

USD_COL_1 = 'USD1'
EUR_COL_1 = 'EUR1'
USD_COL_2 = 'USD2'
EUR_COOL_2 = 'EUR2'
USD_COL_Y = 'USD YIELD'
EUR_COL_Y = 'EUR YIELD'
USA_COL = 'USA'
FRANCE_COL = 'FRANCE'


df = pd.DataFrame({
	OWNER: 5*['JOE']+3*['ROB'],
	USD_COL_1: [4422, 511, 2047, 300, 15941, 15941, 15941, 8973],
	EUR_COL_1: [4422, 511, 2047, 300, 15941, 15941, 15941, 8973],
	USD_COL_2: [4422, 511, 2047, 300, 15941, 15941, 15941, 8973],
	EUR_COOL_2: [4422, 511, 2047, 300, 15941, 15941, 15941, 8973],
	USD_COL_Y: [22, 11, 47, 30, 41, 15, 19, 3],
	EUR_COL_Y: [42, 51, 20, 3, 94, 11, 19, 8],
	USA_COL: ['NEW YORK', 'NEW YORK', 'NEW YORK', 'NEW YORK', 'NEW YORK', 'NEW YORK', 'NEW YORK', 'NEW YORK'],
	FRANCE_COL: ['PARIS', 'PARIS', 'PARIS', 'PARIS', 'PARIS', 'PARIS', 'PARIS', 'PARIS']
	})
	

print(df)

arrays = [
	np.array([' ', ' ', ' ', ' ', ' ', ' ', NUMERIC_LABEL, ' ', TEXT_LABEL]),
	np.array([' ', ' ', ' ', ' ', FLOAT_LABEL, ' ', PERCENT_LABEL, ' ', LOCATION_LABEL]),
	np.array([OWNER, USD_LABEL, EUR_LABEL, USD_LABEL, EUR_LABEL, USD_COL_Y, EUR_COL_Y, USA_LABEL, FRANCE_LABEL])
]
tuples = list(zip(*arrays))
index = pd.MultiIndex.from_tuples(tuples)
df.columns = index

df.style.format("{:.2%}", subset=pd.IndexSlice[:,PERCENT_LABEL]) \
		.format("{:.2f}", subset=pd.IndexSlice[:,[FLOAT_LABEL]])
df.style.bar(subset=[LOCATION_LABEL], align='mid', color=['#d65f5f', '#5fba7d'])


print(df.to_string(index=False))

str = \
'''
														NUMERIC                         TEXT
									FLOAT               PERCENT                  INVEST TOWN
OWNER      USD      EUR      USD      EUR USD YIELD   EUR YIELD USA LOCATION FRANCE LOCATION
  JOE  4422.00  4422.00  4422.00  4422.00      22 %        42 %   NEW YORK        PARIS
  JOE   511.00   511.00   511.00   511.00      11 %        51 %   NEW YORK        PARIS
  JOE  2047.00  2047.00  2047.00  2047.00      47 %        20 %   NEW YORK        PARIS
  JOE   300.00   300.00   300.00   300.00      30 %         3 %   NEW YORK        PARIS
  JOE 15941.00 15941.00 15941.00 15941.00      41 %        94 %   NEW YORK        PARIS
  ROB 15941.00 15941.00 15941.00 15941.00      15 %        11 %   NEW YORK        PARIS
  ROB 15941.00 15941.00 15941.00 15941.00      19 %        19 %   NEW YORK        PARIS
  ROB  8973.00  8973.00  8973.00  8973.00       3 %         8 %   NEW YORK        PARIS
'''

print(str)