import time

from kivy.app import App
from kivy.config import Config
from kivy.properties import ObjectProperty
from kivy.uix.boxlayout import BoxLayout

from septhreadexec import SepThreadExec

class ScrollableMarkupLabelGUI(BoxLayout):
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
		"""
		Called when clearButton is pressed.
		"""
		self.currentLineNb = -1
		self.textInput.text = ''
		self.textOutput.text = ''
		self.textInput.focus = True

	def addMultipleLines(self):
		"""
		Called when addLinesButton is pressed.
		"""
		self.disableButtons()
		
		sepThreadExec = SepThreadExec(callerGUI=self,
		                              func=self.addLinesLoop,
		                              endFunc=self.enableButtons)
		sepThreadExec.start()
	
	def addLinesLoop(self):
		self.disableButtons()
		
		resultStr = 'aaa'
		
		for i in range(5):
			if len(self.textOutput.text) == 0:
				self.textOutput.text = resultStr + ' ' + str(i)
			else:
				self.textOutput.text = self.textOutput.text + '\n' + resultStr + ' ' + str(i)
			
			time.sleep(1)

	def enableButtons(self):
		self.addLinesButton.disabled = False
		self.clearButton.disabled = False

	def disableButtons(self):
		self.addLinesButton.disabled = True
		self.clearButton.disabled = True

	def displayMsg(self, msgStr):
		if len(self.textOutput.text) == 0:
			self.textOutput.text = msgStr
		else:
			self.textOutput.text = self.textOutput.text + '\n' + msgStr


class ScrollableLabelMarkupApp(App):
	def build(self):
		Config.set('graphics', 'width', '400')
		Config.set('graphics', 'height', '300')
		Config.write()

		self.gui = ScrollableMarkupLabelGUI()
  
		return self.gui

ScrollableLabelMarkupApp().run()
