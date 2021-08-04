# SťckOverflow link: https://www.google.com/url?sa=t&source=web&rct=j&url=https://stackoverflow.com/questions/55851223/kivy-setting-event-actions-using-dynamic-classes&ved=2ahUKEwjS1uq88JLyAhXd_rsIHbFQDOgQrAIoAXoECA0QAg&usg=AOvVaw1xwccBqDp5Gc9mNSGQdrbk

from kivy.base import runTouchApp
from kivy.lang import Builder


runTouchApp(Builder.load_string("""
<UserSelectionInput@BoxLayout>:
	orientation: 'horizontal'
	size_hint: None, 1
	spacing: 4

	lb_text: ''
	sp_values: '', ''
	text: user_selection_spinner.text

	Label:
		id: user_selection_label
		size_hint_x: 0.4
		text: root.lb_text
	Spinner:
		id: user_selection_spinner
		text: 'Select'
		values: root.sp_values

<InnerBox@AnchorLayout>:
	anchor_x: 'center'
	anchor_y: 'center'

	BoxLayout:
		orientation: 'horizontal'
		size_hint: None, 1
		width: 2 * root.width / 3
		spacing: 1

		UserSelectionInput:
			width: root.width / 3
			sp_values: 'A', 'B', 'C'
			lb_text: 'Type'
			on_text:
				print("UserSelectionInput.spinner_1: text=", self.text)

		UserSelectionInput:
			width: root.width / 3
			sp_values: 'D', 'E', 'F', 'G'
			lb_text: 'Version'
			on_text:
				print("UserSelectionInput.spinner_2: text=", self.text)

<MainContent@GridLayout>:
	rows: 3

	Label:
		text: "Some Text"
	GridLayout:
		cols: 1
		InnerBox:

MainContent:

"""))