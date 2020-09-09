from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label

# RecycleView related imports
from kivy.properties import BooleanProperty
from kivy.uix.behaviors import FocusBehavior
from kivy.uix.recycleboxlayout import RecycleBoxLayout
from kivy.uix.recycleview.layout import LayoutSelectionBehavior
from kivy.uix.recycleview.views import RecycleDataViewBehavior

import inspect

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
	
	def refresh_view_attrs(self, rv, index, data):
		''' Catch and handle the view changes '''
		self.rv = rv                            #<<------
		self.index = index

		return super(SelectableLabel, self).refresh_view_attrs(
			rv, index, data)

	def on_touch_down(self, touch):
		''' Add selection on touch down '''
		if super(SelectableLabel, self).on_touch_down(touch):
			return True
		if self.collide_point(*touch.pos) and self.selectable:
			info = inspect.currentframe()
			if self.rv.parent.parent.recycleViewCurrentSelIndex == self.index: #<<------
				self.selected = False                                          #<<------
				self.rv.parent.parent.recycleViewCurrentSelIndex = -1          #<<------
			else:                                                              #<<------
				self.rv.parent.parent.recycleViewCurrentSelIndex = self.index  #<<------

			self.rv.parent.parent.manageStateOfMoveButtons()

			res = self.parent.select_with_touch(self.index, touch)
			sel_nodes = self.rv.children[0].selected_nodes
			print(info.f_code.co_name, info.f_lineno,'index ', self.index, ' ', self.selected, ' ', sel_nodes)
			self.rv.parent.parent.moveType = None
			return res


	def apply_selection(self, rv, index, is_selected):
		''' Respond to the selection of items in the view. '''
		info = inspect.currentframe()
		# if rv.parent.parent.recycleViewCurrentSelIndex == index: #<<------
		# 	is_selected = True                                   #<<------
		# 	self.selected = False                                #<<------
		# else:                                                    #<<------
		# 	is_selected = False                                  #<<------
		# 	self.selected = True                                 #<<------
		
		if rv.parent.parent.moveType == 'down':
			if rv.parent.parent.recycleViewCurrentSelIndex - 1 == index:
				self.selected = False
			if rv.parent.parent.recycleViewCurrentSelIndex == index:
				self.selected = True
				rv.children[0].selected_nodes[0] = index
			print(info.f_code.co_name, info.f_lineno, 'index ', index, 'self.selected ', self.selected, 'is_selected ', is_selected, 'moveType ', rv.parent.parent.moveType, 'curr idx ', rv.parent.parent.recycleViewCurrentSelIndex, 'sel nodes', rv.children[0].selected_nodes)
			return
		elif rv.parent.parent.moveType == 'up':
			if rv.parent.parent.recycleViewCurrentSelIndex + 1 == index:
				self.selected = False
			if rv.parent.parent.recycleViewCurrentSelIndex == index:
				self.selected = True
				rv.children[0].selected_nodes[0] = index
			print(info.f_code.co_name, info.f_lineno, 'index ', index, 'self.selected ', self.selected, 'is_selected ', is_selected, 'moveType ', rv.parent.parent.moveType, 'curr idx ', rv.parent.parent.recycleViewCurrentSelIndex, 'sel nodes', rv.children[0].selected_nodes)
			return

		if not self.selected and not is_selected:
			# case when adding a new list item
			print(info.f_code.co_name, info.f_lineno, 'index ', index, 'self.selected ', self.selected, 'is_selected ', is_selected, 'moveType ', rv.parent.parent.moveType)
			return
		elif self.selected and not is_selected:
			# toggling from selected to unselected
			print(info.f_code.co_name, info.f_lineno, 'index ', index, 'self.selected ', self.selected, 'is_selected ', is_selected, '--> self.selected = False', 'moveType ', rv.parent.parent.moveType)
			self.selected = False                   #<<------
		else:
			# toggling from unselected to selected
			print(info.f_code.co_name, info.f_lineno, 'index ', index, 'self.selected ', self.selected, 'is_selected ', is_selected, '--> self.selected = not self.selected', 'moveType ', rv.parent.parent.moveType)
			self.selected = not self.selected       #<<------


class KivyRecycleView(BoxLayout):
	recycleViewCurrentSelIndex = -1

	def __init__(self, **kwargs):
		super(KivyRecycleView, self).__init__(**kwargs)

		# setting RecycleView list item height from config
		self.populateList()
		self.moveType = None

	def populateList(self):
		for i in range(6):
			listEntry = {'text': 'line {}'.format(i)}
			self.recycleViewList.data.append(listEntry)

	def moveUpSelItem(self):
		self.moveType = 'up'
		oldIndex = self.recycleViewCurrentSelIndex
	
		if oldIndex == -1:                                  #<<------
			return
		
		newIndex = oldIndex - 1
		itemTotalNumber = len(self.recycleViewList.data)
		
		if newIndex < 0:
			# if first line request is moved up, it is moved at the end of the
			# request history list
			newIndex = itemTotalNumber - 1
		
		self.moveItemInList(list=self.recycleViewList.data, oldIndex=oldIndex, newIndex=newIndex)
		self.recycleViewCurrentSelIndex = newIndex          #<<------

	def moveDownSelItem(self):
		self.moveType = 'down'
		oldIndex = self.recycleViewCurrentSelIndex
	
		if oldIndex == -1:                                  #<<------
			return
		
		newIndex = oldIndex + 1
		itemTotalNumber = len(self.recycleViewList.data)
		
		if newIndex == itemTotalNumber:
			# if last line request is moved down, it is moved at the beginning of the
			# request history list
			newIndex = 0
		
		self.moveItemInList(list=self.recycleViewList.data, oldIndex=oldIndex, newIndex=newIndex)
		self.recycleViewCurrentSelIndex = newIndex          #<<------

	def moveItemInList(self, list, oldIndex, newIndex):
		list.insert(newIndex, list.pop(oldIndex))

	def manageStateOfMoveButtons(self):
		if self.recycleViewCurrentSelIndex == -1:
			self.moveUpButton.disabled = True
			self.moveDownButton.disabled = True
		else:
			self.moveUpButton.disabled = False
			self.moveDownButton.disabled = False

class KivyRecycleView_moveButtonsApp(App):
	def build(self): # implicitely looks for a kv file of name kivyrecycleview.kv which is
					 # class name without App, in lowercases

		return KivyRecycleView()

if __name__ == '__main__':
	dbApp = KivyRecycleView_moveButtonsApp()

	dbApp.run()