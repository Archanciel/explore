import pandas as pd 

from kivy.app import App
from kivy.config import Config
from kivy.properties import ObjectProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup

OWNER = 'OWNER'
CAPITAL_USD = 'CAPITAL USD'
YIELD_USD = 'YIELD USD'
CAPITAL_CHF = 'CAPITAL CHF'
YIELD_CHF = 'YIELD CHF'
CAPITAL_EUR = 'CAPITAL EUR'
YIELD_EUR = 'YIELD EUR'
CAPITAL_DM = 'CAPITAL DM'
YIELD_DM = 'YIELD DM'

class ScrollablePopup(Popup):
	contentBox = ObjectProperty()
	scrollView = ObjectProperty()

	def scrollToTop(self):
		self.scrollView.scroll_y = 1 # force scrolling to top

	def scrollToBottom(self):
		self.scrollView.scroll_y = 0 # force scrolling to bottom

	def initText(self, text):
		self.contentBox.content.text = text


class ScrollPopup(BoxLayout):
	popup = None

	def openPopup(self):
		self.popup = ScrollablePopup(title="Scrollable popup")

		dfstr = self.createDataframe()
		print(dfstr)
		text = dfstr
		self.popup.initText(text)
		self.popup.open()

	def createDataframe(self):
		df = pd.DataFrame({OWNER: ['John', 'John', 'John', 'John', 'John', 'John', 'Rob', 'Rob', 'Rob', 'Rob', 'Rob',
								   'Rob', 'Rob', 'Rob', 'Tom', 'Tom', 'Tom', 'Tom', 'Tom', 'Tom', 'Bob', 'Bob', 'Bob',
								   'Bob', 'Bob'] * 3,
						   CAPITAL_USD: [10000, 5000, 20000, 4000, 3000] * 15,
						   YIELD_USD: [1000, 500, 2000, 400, 300] * 15,
						   CAPITAL_CHF: [10000, 5000, 20000, 4000, 3000] * 15,
						   YIELD_CHF: [1000, 500, 2000, 400, 300] * 15,
						   CAPITAL_EUR: [10000, 5000, 20000, 4000, 3000] * 15,
						   YIELD_EUR: [1000, 500, 2000, 400, 300] * 15,
						   CAPITAL_DM: [10000, 5000, 20000, 4000, 3000] * 15,
						   YIELD_DM: [1000, 500, 2000, 400, 300] * 15})

		# adding OWNER total rows

		dfGroupOwnerTotal = df.groupby([OWNER]).agg({CAPITAL_USD: 'sum',
													 YIELD_USD: 'sum',
													 CAPITAL_CHF: 'sum',
													 YIELD_CHF: 'sum',
													 CAPITAL_EUR: 'sum',
													 YIELD_EUR: 'sum',
													 CAPITAL_DM: 'sum',
													 YIELD_DM: 'sum'})
		totalDf = pd.DataFrame(columns=[OWNER,
										CAPITAL_USD,
										YIELD_USD,
										CAPITAL_CHF,
										YIELD_CHF,
										CAPITAL_EUR,
										YIELD_EUR,
										CAPITAL_DM,
										YIELD_DM])
		currentOwner = df.loc[1, OWNER]
		totalDfIndex = 0

		# deactivating SettingWithCopyWarning caueed by totalRow[OWNER] += ' total'
		pd.set_option('mode.chained_assignment', None)

		for index, row in df.iterrows():
			if currentOwner == row[OWNER]:
				totalDf = totalDf.append({OWNER: row[OWNER],
										  CAPITAL_USD: row[CAPITAL_USD],
										  YIELD_USD: row[YIELD_USD],
										  CAPITAL_CHF: row[CAPITAL_CHF],
										  YIELD_CHF: row[YIELD_CHF],
										  CAPITAL_EUR: row[CAPITAL_EUR],
										  YIELD_EUR: row[YIELD_EUR],
										  CAPITAL_DM: row[CAPITAL_DM],
										  YIELD_DM: row[YIELD_DM]}, ignore_index=True)
			else:
				totalRow = dfGroupOwnerTotal.loc[currentOwner]
				totalDf = totalDf.append(totalRow, ignore_index=True)
				totalDf.iloc[totalDfIndex][OWNER] = currentOwner + ' total'
				totalDfIndex += 1
				totalDf = totalDf.append({OWNER: row[OWNER],
										  CAPITAL_USD: row[CAPITAL_USD],
										  YIELD_USD: row[YIELD_USD],
										  CAPITAL_CHF: row[CAPITAL_CHF],
										  YIELD_CHF: row[YIELD_CHF],
										  CAPITAL_EUR: row[CAPITAL_EUR],
										  YIELD_EUR: row[YIELD_EUR],
										  CAPITAL_DM: row[CAPITAL_DM],
										  YIELD_DM: row[YIELD_DM]}, ignore_index=True)
				currentOwner = row[OWNER]
			totalDfIndex += 1

		totalRow = dfGroupOwnerTotal.loc[currentOwner]
		totalDf = totalDf.append(totalRow, ignore_index=True)
		totalDf.iloc[totalDfIndex][OWNER] = currentOwner + ' total'

		return totalDf.to_string()


class ScrollPopupVertHorzPandasApp(App):
	def build(self): # implicitely looks for a kv file of name kivylistview1111.kv which is
					 # class name without App, in lowercases

		Config.set('graphics', 'width', '400')
		Config.set('graphics', 'height', '500')
		Config.write()

		return ScrollPopup()

	def on_pause(self):
		# Here you can save data if needed
		return True

	def on_resume(self):
		# Here you can check if any data needs replacing (usually nothing)
		pass

if __name__ == '__main__':
	ScrollPopupVertHorzPandasApp().run()