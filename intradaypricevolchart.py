import matplotlib as mpl
import matplotlib.pyplot as plt

plt.style.use('ggplot')
import pandas as pd
import numpy as np
from datetime import datetime

n = 3600
idx = pd.date_range(start=datetime.now(), freq='1S', periods=n)
data = pd.DataFrame(data={'price': np.cumsum([0.0001] * n + np.random.random(n)),
                          'volume': np.random.randint(low=1, high=10000, size=n)}, index=idx)
data = pd.read_csv('secondary-2018-08-12-21-32-56.csv', index_col=0, sep='\t')
print(data.head())
fig, ax = plt.subplots(nrows=2, sharex=True, figsize=(10,5))

ax[0].plot(data.index, data['PRICE'])
ax[1].bar(data.index, data['VOLUME'])

fmt = mpl.dates.DateFormatter('%M:%S')
#ax[1].xaxis.set_major_locator(mpl.dates.HourLocator(interval=1))
#aaaax[1].xaxis.set_major_formatter(xfmt)

#ax[1].xaxis.set_minor_locator(mpl.dates.HourLocator(interval=1))
#aaaax[1].xaxis.set_minor_formatter(xfmt)

ax[1].get_xaxis().set_tick_params(which='major', pad=15)

fig.autofmt_xdate()
plt.show()