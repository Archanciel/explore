import matplotlib as mpl
import matplotlib.pyplot as plt

plt.style.use('ggplot')
import pandas as pd
import numpy as np
from datetime import datetime

n = 100
idx = pd.date_range(start=datetime(2016, 1, 1, 10), freq='10Min', periods=n)
data = pd.DataFrame(data={'price': np.cumsum([0.0001] * n + np.random.random(n)),
                          'volume': np.random.randint(low=100, high=10000, size=n)}, index=idx)

fig, ax = plt.subplots(nrows=2, sharex=True, figsize=(15,8))

ax[0].plot(data.index, data.price)
ax[1].bar(data.index, data.volume, width=1/(5*len(data.index)))

xfmt = mpl.dates.DateFormatter('%H:%M')
ax[1].xaxis.set_major_locator(mpl.dates.HourLocator(interval=3))
ax[1].xaxis.set_major_formatter(xfmt)

ax[1].xaxis.set_minor_locator(mpl.dates.HourLocator(interval=1))
ax[1].xaxis.set_minor_formatter(xfmt)

ax[1].get_xaxis().set_tick_params(which='major', pad=25)

fig.autofmt_xdate()
plt.show()