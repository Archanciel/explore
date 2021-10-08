import time

from kivy.app import App
from kivy.config import Config
from kivy.properties import ObjectProperty
from kivy.uix.boxlayout import BoxLayout


class ScrollableMarkupLabel(BoxLayout):
	textInput = ObjectProperty()
	scroller = ObjectProperty()
	textOutput = ObjectProperty()
	
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		self.currentLineNb = -1

	def submitRequest(self):
		self.currentLineNb += 1
		
		if self.textOutput.text and self.textOutput.text != '':
			self.textOutput.text = self.textOutput.text + '\n' + self.textInput.text
		else:
			self.textOutput.text = self.textInput.text

		self.textInput.text = ''
		self.textInput.focus = True

	def text_changed(self, *args):
		width_calc = self.scroller.width
		for line_label in self.textOutput._lines_labels:
			width_calc = max(width_calc, line_label.width + 20)   # add 20 to avoid automatically creating a new line
		self.textOutput.width = width_calc

	def clearAll(self):
		self.currentLineNb = -1
		self.textInput.text = ''
		self.textOutput.text = ''
		self.textInput.focus = True

	def addMultipleLines(self):
		resultStr = 'aaa'
		
		for i in range(5):
			if len(self.textOutput.text) == 0:
				self.textOutput.text = resultStr + ' ' + str(i)
			else:
				self.textOutput.text = self.textOutput.text + '\n' +  resultStr + ' ' + str(i)
				
			time.sleep(1)
			
			# self.outputResultScrollView.scroll_to(100000)
			# self.resultOutput.cursor = (10000,0)


class ScrollableLabelMarkupApp(App):
	def build(self):
		Config.set('graphics', 'width', '400')
		Config.set('graphics', 'height', '300')
		Config.write()

		self.gui = ScrollableMarkupLabel()
  
		return self.gui

ScrollableLabelMarkupApp().run()
