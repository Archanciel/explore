import pandas as pd
import numpy as np

# loading initial returns csv file
initialReturnsDf = pd.read_csv('init_returns.csv', parse_dates=['DATE'], dtype={'GAIN': np.float64})
initialReturnsDf = initialReturnsDf.set_index(['DATE'])

# inserting two empty columns
initialReturnsDf.insert(loc=0, column='CAPITAL', value=[0 for i in range(initialReturnsDf.shape[0])])
initialReturnsDf.insert(loc=0, column='DEPOT/RETRAIT', value=[0 for i in range(initialReturnsDf.shape[0])])

# converting the two columns to float64
initialReturnsDf[['CAPITAL', 'DEPOT/RETRAIT']] = initialReturnsDf[['CAPITAL', 'DEPOT/RETRAIT']].apply(np.float64)		

# loading deposits csv file
depositsDf = pd.read_csv('deposits.csv', parse_dates=['DATE'], dtype={'DEPOT/RETRAIT': np.float64})
depositsDf = depositsDf.set_index(['DATE'])


print('\ninitialReturnsDf')
print(initialReturnsDf)
initialReturnsDf.info()

print('\ndepositsDf')
print(depositsDf)
depositsDf.info()

# appending depositsDf to initialReturnsDf, then sorting and converting NaN to zero
initialReturnsDf = initialReturnsDf.append(depositsDf).sort_index().fillna(0)

print('\ninitialReturnsDf after appending depositsDf')
print(initialReturnsDf)

# replace DATE index with integer index

	# save old DATE index Column
initialReturnsDf['DATE'] = initialReturnsDf.index

	# reposition the DATE column to the left of the data frame
cols = initialReturnsDf.columns.to_list()
cols = cols[-1:] + cols[:-1]
initialReturnsDf = initialReturnsDf[cols]

	# set integer index
initialReturnsDf['IDX'] = range(1, len(initialReturnsDf) + 1)
initialReturnsDf = initialReturnsDf.set_index('IDX')

# update CAPITAL values
initialReturnsDf.loc[1, 'CAPITAL'] = initialReturnsDf.loc[1, 'DEPOT/RETRAIT']

for i in range(2, len(initialReturnsDf) + 1):
    initialReturnsDf.loc[i, 'CAPITAL'] = initialReturnsDf.loc[i-1, 'CAPITAL'] + initialReturnsDf.loc[i, 'DEPOT/RETRAIT'] + initialReturnsDf.loc[i, 'GAIN']

print('\ninitialReturnsDf after updating CAPITAL')
print(initialReturnsDf)