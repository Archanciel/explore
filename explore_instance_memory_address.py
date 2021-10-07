import _ctypes
import re

class MyClass():
	def __init__(self, nameStr):
		self.nameStr = nameStr

def di(obj_id):
	""" Inverse of id() function. """
	return _ctypes.PyObj_FromPtr(obj_id)


if __name__ == '__main__':
	mc = MyClass('hello')
	
	id = id(mc)
	
	instanceRefStr = str(di(id))
#	print(instanceRefStr)

	addressLst = re.findall(r'0x[0-9A-F]+', instanceRefStr, re.I)
	
	for address in addressLst:
		print(di(bytes.fromhex(address)))
