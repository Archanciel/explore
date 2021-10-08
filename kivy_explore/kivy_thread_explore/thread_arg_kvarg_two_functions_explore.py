import threading, time

def myFunc(name='', age=0):
	print('My name is {}. I am {} years old'.format(name, age))


def myEndFunc(name='', age=0):
	print('MY SURNAME WAS {}. I was {} years old'.format(name.upper(), age))


def startWithCallback(func, endFunc, endFuncArgs=None, kwargs=None):
	"""Start 'func' in a new thread T, then start self (and return T)."""
	if endFuncArgs is None:
		endFuncArgs = ()
	if kwargs is None:
		kwargs = {}
		
	args = (func, endFunc) + endFuncArgs
	
	def _callback(func, endFunc, *a, **kw):
		for i in range(5):
			time.sleep(1)
			func(**kw)
			
		endFunc(*a)
	
	t = threading.Thread(target=_callback, args=args, kwargs=kwargs)
	t.setName('Exec thread ' + t.getName())
	t.daemon = True
	t.start()
	
	return t

thread = startWithCallback(func=myFunc, endFunc=myEndFunc, endFuncArgs=('paulo le scientifique', 14), kwargs={'name': 'Jean-Pierre', 'age': 60})
print(thread.getName(), 'started ...')
time.sleep(6)   # necessary, otherwise, since the daemon thread property is
				# set to True, the program will end and suppress the thread
				# before it starts working !
