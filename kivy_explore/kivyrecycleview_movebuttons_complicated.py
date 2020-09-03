from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label

# RecycleView related imports
from kivy.properties import BooleanProperty
from kivy.uix.behaviors import FocusBehavior
from kivy.uix.recycleboxlayout import RecycleBoxLayout
from kivy.uix.recycleview.layout import LayoutSelectionBehavior
from kivy.uix.recycleview.views import RecycleDataViewBehavior

MOVE_BUTTON_UP = 'up'
MOVE_BUTTON_DOWN = 'down'

class SelectableRecycleBoxLayout(FocusBehavior, LayoutSelectionBehavior,
								 RecycleBoxLayout):
	''' Adds selection and focus behaviour to the view. '''
 
	# required to authorise unselecting a selected item
	touch_deselect_last = BooleanProperty(True)
 
class SelectableLabel(RecycleDataViewBehavior, Label):
	''' Add selection support to the Label '''
	index = None
	selected = BooleanProperty(False)
	selectable = BooleanProperty(True)
	rv = None
 
	def refresh_view_attrs(self, rv, index, data):
		''' Catch and handle the view changes '''
		self.rv = rv
		self.index = index
 
		return super(SelectableLabel, self).refresh_view_attrs(
			rv, index, data)
 
	def on_touch_down(self, touch):
		''' Add selection on touch down '''
		# if self.selected:
		# 	self.rv.parent.parent.recycleViewCurrentSelIndex = -1
		# else:
		# 	self.rv.parent.parent.recycleViewCurrentSelIndex = self.index

		if super(SelectableLabel, self).on_touch_down(touch):
			return True
		if self.collide_point(*touch.pos) and self.selectable:
			return self.parent.select_with_touch(self.index, touch)
 
	def apply_selection(self, rv, index, is_selected):
		''' Respond to the selection of items in the view. '''
		# if rv.parent.parent.moveButtonPressed:
		# 	if rv.parent.parent.recycleViewCurrentSelIndex == index:
		# 		is_selected = True
		# 		self.selected = False
		# 	else:
		# 		is_selected = False
		# 		self.selected = True
		
		if not self.selected and not is_selected:
			# case when adding a new list item
			return
		elif self.selected and not is_selected:
			# toggling from selected to unselected
			if rv.parent.parent.moveButtonPressed:
				rv.parent.parent.moveButtonPressed = None
				self.selected = True
			else:
				self.selected = False
			#rv.parent.parent.moveButtonPressed = None
			#rv.parent.parent.recycleViewCurrentSelIndex = -1
		else:
			# toggling from unselected to selected
			self.selected = not self.selected
			#rv.parent.parent.recycleViewCurrentSelIndex = index
			if self.selected:
				if rv.parent.parent.moveButtonPressed == MOVE_BUTTON_UP:
					self.selected = False
					newSelIndex = index - 1
					newSelIndex = rv.parent.parent.getCorrectedIndex(newSelIndex)
					rv.parent.parent.recycleViewCurrentSelIndex = newSelIndex
				elif rv.parent.parent.moveButtonPressed == MOVE_BUTTON_DOWN:
					self.selected = False
					newSelIndex = index + 1
					newSelIndex = rv.parent.parent.getCorrectedIndex(newSelIndex)
					rv.parent.parent.recycleViewCurrentSelIndex = newSelIndex
				else:
					rv.parent.parent.recycleViewCurrentSelIndex = index


class KivyRecycleView(BoxLayout):
	def __init__(self, **kwargs):
		super(KivyRecycleView, self).__init__(**kwargs)
		self.recycleViewCurrentSelIndex = -1
		self.moveButtonPressed = None
		
		# setting RecycleView list item height from config
		self.populateList()
 
	def populateList(self):
		for i in range(6):
			listEntry = {'text': 'line {}'.format(i)}
			self.recycleViewList.data.append(listEntry)
 
	def moveUpSelItem(self):
		self.moveButtonPressed = MOVE_BUTTON_UP
		oldIndex = self.recycleViewCurrentSelIndex
		newIndex = oldIndex - 1
 
		newIndex = self.getCorrectedIndex(newIndex)
 
		self.moveItemInList(list=self.recycleViewList.data, oldIndex=oldIndex, newIndex=newIndex)
		self.recycleViewCurrentSelIndex = newIndex

	def moveDownSelItem(self):
		self.moveButtonPressed = MOVE_BUTTON_DOWN
		oldIndex = self.recycleViewCurrentSelIndex
		newIndex = oldIndex + 1
 
		newIndex = self.getCorrectedIndex(newIndex)
 
		self.moveItemInList(list=self.recycleViewList.data, oldIndex=oldIndex, newIndex=newIndex)
		self.recycleViewCurrentSelIndex = newIndex
	
	def getCorrectedIndex(self, index):
		itemTotalNumber = len(self.recycleViewList.data)
		
		if self.moveButtonPressed == MOVE_BUTTON_UP:
			if index < 0:
				# if first line request is moved up, it is moved at the end of the
				# item list
				index = itemTotalNumber - 1
			else:
				pass
		elif self.moveButtonPressed == MOVE_BUTTON_DOWN:
			if index == itemTotalNumber:
				# if first line request is moved up, it is moved at the beginning of the
				# item list
				index = 0
			else:
				pass
		
		return index
	
	def moveItemInList(self, list, oldIndex, newIndex):
		list.insert(newIndex, list.pop(oldIndex))
 
class KivyRecycleView_moveButtonsApp(App):
	def build(self): # implicitely looks for a kv file of name kivyrecycleview.kv which is
					 # class name without App, in lowercases
 
		return KivyRecycleView()
 
if __name__ == '__main__':
	dbApp = KivyRecycleView_moveButtonsApp()
 
	dbApp.run()
