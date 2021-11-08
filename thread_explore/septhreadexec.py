# Works on Windows and on Android

import threading, time
from multiprocessing import Process

class SepThreadExec:
	def __init__(self, callerGUI, func, endFunc, funcArgs=None, endFuncArgs=None):
		self.callerGUI = callerGUI
		
		if endFuncArgs is None:
			endFuncArgs = ()
		if funcArgs is None:
			funcArgs = {}
		
		args = (func, endFunc) + endFuncArgs
		
		self.p = Process(target=self._callback, args=args, kwargs=funcArgs)
		self.p.daemon = True
	
	def _callback(self, func, endFunc, *a, **kw):
		func(**kw)
		endFunc(*a)
	
	def start(self):
		self.callerGUI.displayMsg('Process started ...')
		self.p.start()
		
	def stop(self):
		self.p.terminate()

class GUIStub:
	def displayMsg(self, msg):
		print('GUIStub' + ' ' + msg)
		
	def myFunc(self, name='', age=0):
		for i in range(5):
			time.sleep(1)
			print('{}: My name is {}. I am {} years old'.format(i + 1, name, age))

def myEndFunc(name='', age=0):
	print('MY SURNAME WAS {}. I was {} years old'.format(name.upper(), age))

if __name__ == "__main__":
	
	gui = GUIStub()
	
	ste = SepThreadExec(callerGUI=gui,
	                    func=gui.myFunc,
	                    endFunc=myEndFunc,
	                    funcArgs={'name': 'Jean-Pierre', 'age': 60},
	                    endFuncArgs=('paulo le scientifique', 14))
	
	ste.start()
	time.sleep(3)
	ste.stop()
	time.sleep(3)
