def moveItemInList(list, oldIndex, newIndex):
	list.insert(newIndex, list.pop(oldIndex))
	
l = [4, 6, 9, 2]
print(l)
moveItemInList(l, 3, 2)
print(l)
