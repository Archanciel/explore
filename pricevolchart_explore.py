import matplotlib as mpl
import matplotlib.pyplot as plt
 
plt.style.use('ggplot')
import pandas as pd
import numpy as np
from datetime import datetime
 
n = 1000

#setting index as second ticks
idx = pd.date_range(start=datetime.now(), freq='S', periods=n)

#generating data, placing them in a Pandas frame indexed by the seconds ticks
data = pd.DataFrame(data={'price': np.cumsum([0.0001] * n + np.random.random(n)),
                          'volume': np.random.randint(low=10, high=1000, size=n)}, index=idx)

#creating 2 subplots 
fig, ax = plt.subplots(nrows=2, sharex=True, figsize=(15,8))
 
#two ways of referencing Pandas dataframe columns: data['price'] or data.volume'']
ax[0].plot(data.index, data['price'])
ax[1].bar(data.index, data.volume, width=1/(50*len(data.index)))

#setting the 2 levels X axis labels 
xfmtMajor = mpl.dates.DateFormatter('%M:%S')
ax[1].xaxis.set_major_locator(mpl.dates.SecondLocator(interval=60))
ax[1].xaxis.set_major_formatter(xfmtMajor)

xfmtMinor = mpl.dates.DateFormatter('%S')
ax[1].xaxis.set_minor_locator(mpl.dates.SecondLocator(interval=30))
ax[1].xaxis.set_minor_formatter(xfmtMinor)

#defining the vertical interval between the major and minor X axis label rows
ax[1].get_xaxis().set_tick_params(which='major', pad=20)
 
fig.autofmt_xdate()
plt.show()