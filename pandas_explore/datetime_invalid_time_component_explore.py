import pandas as pd
from datetime import datetime

OWNER = 'OWNER'
DEPWITHDR = 'DEP WITHDR'
YIELD = 'YIELD AMT'
DATE_TIME = 'DATE'
TOTAL = 'TOTAL'

# defining the dataframe
df = pd.DataFrame({OWNER: 2 * ['Joe'] + 3 * ['Carla'] + ['Rob'],
				   DATE_TIME: ['2021/01/01 00:00:00', '2021/01/02 10:00:00', '2021/01/03 00:00:00', '2021/01/04 00:00:00', '2021/01/05 00:00:00', '2021/01/06 00:00:00'],
                   DEPWITHDR: [10000, 5000, 20000, 3000, -4000, 2000],
                   YIELD: [1000, 500, 2000, 300, 400, 200]})

print(df)
print()

dfDateTimeLst = list(df[DATE_TIME])

dtNine = datetime.strptime('09:00:00', '%H:%M:%S')

badTimeIndex = None

try:
	badTimeIndex = next(i for i, v in enumerate(dfDateTimeLst) if datetime.strptime(v, '%Y/%m/%d %H:%M:%S').time() > dtNine.time())
except StopIteration:
	pass

print(badTimeIndex)

# print(dtNine.time())
# for index, row in df.iterrows():
# 	dateTimeStr = row[DATE_TIME]
# 	dt = datetime.strptime(dateTimeStr, '%Y/%m/%d %H:%M:%S')
# 	print(dt.time())
# 	print(dt.time() > dtNine.time())
