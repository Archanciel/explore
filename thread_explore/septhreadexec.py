import threading, time

class SepThreadExec:
	def __init__(self, callerGUI, func, endFunc, funcArgs=None, endFuncArgs=None):
		self.callerGUI = callerGUI
		
		if endFuncArgs is None:
			endFuncArgs = ()
		if funcArgs is None:
			funcArgs = {}
		
		args = (func, endFunc) + endFuncArgs
		
		def _callback(func, endFunc, *a, **kw):
			func(**kw)
			endFunc(*a)
		
		self.t = threading.Thread(target=_callback, args=args, kwargs=funcArgs)
		self.t.setName('Exec thread ' + self.t.getName())
		self.t.daemon = True
		
	def start(self):
		self.callerGUI.displayMsg(self.t.getName() + ' started ...')
		self.t.start()

class GUIStub:
	def __init__(self):
		self.stop = False
		
	def displayMsg(self, msg):
		print('GUIStub' + ' ' + msg)
		
	def myFunc(self, name='', age=0):
		for i in range(5):
			if not self.stop:
				time.sleep(1)
				print('My name is {}. I am {} years old'.format(name, age))
			else:
				print('stopping ...')
				break
			
if __name__ == "__main__":
	def myEndFunc(name='', age=0):
		print('MY SURNAME WAS {}. I was {} years old'.format(name.upper(), age))
	
	gui = GUIStub()
		
	ste = SepThreadExec(callerGUI=gui,
	              func=gui.myFunc,
	              endFunc=myEndFunc,
	              funcArgs={'name': 'Jean-Pierre', 'age': 60},
	              endFuncArgs=('paulo le scientifique', 14))
	
	ste.start()
	time.sleep(3)
	gui.stop = True
	time.sleep(3)
