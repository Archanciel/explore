from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label

# RecycleView related imports
from kivy.properties import BooleanProperty
from kivy.uix.behaviors import FocusBehavior
from kivy.uix.recycleboxlayout import RecycleBoxLayout
from kivy.uix.recycleview.layout import LayoutSelectionBehavior
from kivy.uix.recycleview.views import RecycleDataViewBehavior

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
	recycleViewList = None

	def refresh_view_attrs(self, rv, index, data):
		''' Catch and handle the view changes '''
		
		# storing reference on the recycle view
		self.rv = rv
		
		self.index = index

		return super(SelectableLabel, self).refresh_view_attrs(
			rv, index, data)

	def on_touch_down(self, touch):
		''' Add selection on touch down '''
		if super(SelectableLabel, self).on_touch_down(touch):
			return True
		if self.collide_point(*touch.pos) and self.selectable:
			# since the item was touched down to select or unselect it,
			# we are no longer in the state of moving up or down the item
			self.rv.parent.parent.wasMoveButtonPressed = False
			
			result = self.parent.select_with_touch(self.index, touch)
			
			self.rv.parent.parent.recycleViewList.data[self.index]['selected'] = self.selected
			self.rv.parent.parent.manageStateOfMoveButtons()
			
			return result
		else: # only for debug
			index = self.index
			selected = self.selected

	def apply_selection(self, rv, index, is_selected):
		''' Respond to the selection of items in the view. '''
		if rv.parent.parent.wasMoveButtonPressed:
			if rv.parent.parent.getSelectedItem() == index:  # <<------
				is_selected = True  # <<------
				self.selected = False  # <<------
			elif not rv.parent.parent.getSelectedItem() == -1:  # <<------
				is_selected = False  # <<------
				self.selected = True  # <<------
	
		selItemIndexes = self.rv.parent.parent.getSelectItemIndexes()
	
		if not self.selected and not is_selected:
			# case when adding a new list item
			self.rv.parent.parent.recycleViewList.data[index]['selected'] = self.selected
			return
		elif self.selected and not is_selected:
			# toggling from selected to unselected
			self.selected = False
			self.rv.parent.parent.recycleViewList.data[index]['selected'] = self.selected
		else:
			# toggling from unselected to selected
			self.selected = not self.selected
			self.rv.parent.parent.recycleViewList.data[index]['selected'] = self.selected

class KivyRecycleViewGUI(BoxLayout):
	def __init__(self, **kwargs):
		super(KivyRecycleViewGUI, self).__init__(**kwargs)
		self.wasMoveButtonPressed = False

		# setting RecycleView list item height from config
		self.populateList()

	def populateList(self):
		for i in range(6):
			listEntry = {'text': 'line {}'.format(i), 'selected': False}
			self.recycleViewList.data.append(listEntry)

	def moveUpSelItem(self):
		self.wasMoveButtonPressed = True
		oldIndex = self.getSelectedItem()
		if oldIndex == -1:
			# the case when no item is selected
			return
		newIndex = oldIndex - 1
		requestTotalNumber = len(self.recycleViewList.data)

		if newIndex < 0:
			# if first line request is moved up, it is moved at the end of the
			# request history list
			newIndex = requestTotalNumber - 1

		self.moveItemInList(list=self.recycleViewList.data, oldIndex=oldIndex, newIndex=newIndex)

	def moveDownSelItem(self):
		self.wasMoveButtonPressed = True
		oldIndex = self.getSelectedItem()
		if oldIndex == -1:
			# the case when no item is selected
			return
		newIndex = oldIndex + 1
		requestTotalNumber = len(self.recycleViewList.data)

		if newIndex == requestTotalNumber:
			# if first line request is moved up, it is moved at the end of the
			# request history list
			newIndex = 0

		self.moveItemInList(list=self.recycleViewList.data, oldIndex=oldIndex, newIndex=newIndex)

	def getSelectedItem(self):
		i = 0
		
		for item in self.recycleViewList.data:
			if item['selected']:
				return i
			else:
				i += 1
				
		return -1
		
	def moveItemInList(self, list, oldIndex, newIndex):
		list.insert(newIndex, list.pop(oldIndex))
		list[oldIndex]['selected'] = False
		list[newIndex]['selected'] = True

	def manageStateOfMoveButtons(self):
		if self.getSelectedItem() == -1:
			self.moveUpButton.disabled = True
			self.moveDownButton.disabled = True
		else:
			self.moveUpButton.disabled = False
			self.moveDownButton.disabled = False
			
	def getSelectItemIndexes(self): # only for debug
		i = 0
		indexes = []
	
		for item in self.recycleViewList.data:
			if item['selected']:
				indexes.append(i)
			i += 1
			
		return indexes

class KivyRecycleView_moveButtonsDataApp(App):
	def build(self): # implicitely looks for a kv file of name kivyrecycleview.kv which is
					 # class name without App, in lowercases

		return KivyRecycleViewGUI()

if __name__ == '__main__':
	dbApp = KivyRecycleView_moveButtonsDataApp()

	dbApp.run()