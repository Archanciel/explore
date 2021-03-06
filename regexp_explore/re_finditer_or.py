import re

def findAllValues(fullCommandStrForStatusBar):
	print()
	print(fullCommandStrForStatusBar)
	return re.findall(r"(\d+\.\d+|\d)", fullCommandStrForStatusBar)

fullCommandStrForStatusBar = 'eth btc 0 kraken -vs3eth -fseth.kraken 0.0387 ETH/BTC * 25.83979328 BTC/ETH = 1 ETH/ETH)'
print(findAllValues(fullCommandStrForStatusBar))

fullCommandStrForStatusBar = 'eth btc 0 kraken -vs3eth -fsbtc.kraken 0.03871 ETH/BTC * 1 BTC/BTC = 0.03871 ETH/BTC)'
print(findAllValues(fullCommandStrForStatusBar))
