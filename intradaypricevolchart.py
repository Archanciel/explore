import matplotlib.pyplot as plt

plt.style.use('ggplot')
import pandas as pd

data = pd.read_csv('secondary-2018-08-19-22-44-28.csv', index_col=0, sep='\t')
print(data.head(50))
fig, ax = plt.subplots(nrows=2, sharex=True, figsize=(10,5))

ax[0].plot(data.index, data['PRICE'])
ax[1].bar(data.index, data['VOLUME'])

plt.show()