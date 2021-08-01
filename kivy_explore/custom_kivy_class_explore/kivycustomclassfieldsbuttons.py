from kivy.uix.boxlayout import BoxLayout


class KivyCustomClassFieldsButtons(BoxLayout):
	def __init__(self, **kwargs):
		super(KivyCustomClassFieldsButtons, self).__init__(**kwargs)
		
	def printFirstText(self):
		print(self.ids.first_text_input.text)
	
	def printSecondText(self):
		print(self.ids.second_text_input.text)
