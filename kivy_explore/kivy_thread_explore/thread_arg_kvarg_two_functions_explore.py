import threading, time

def my_func(name='', age=0):
	print('My name is {}. I am {} years old'.format(name, age))


def my_end_func(name='', age=0):
	print('MY FURNAME WAS {}. I was {} years old'.format(name.upper(), age))


def start_with_callback(func, endFunc, args=None, kwargs=None):
	"""Start 'func' in a new thread T, then start self (and return T)."""
	if args is None:
		args = ()
	if kwargs is None:
		kwargs = {}
	args = (func, endFunc) + args
	
	def _callback(func, endFunc, *a, **kw):
		for i in range(5):
			time.sleep(1)
			func(**kw)
			
		endFunc(*a)
	
	t = threading.Thread(target=_callback, args=args, kwargs=kwargs)
	t.setName('Bus Callback ' + t.getName())
	t.daemon = True
	t.start()
	
	return t

start_with_callback(func=my_func, endFunc=my_end_func, args=('paulo le scientifique', 14), kwargs={'name': 'Jean-Pierre', 'age': 60})
time.sleep(6)   # necessary, otherwise, since the daemon thread property is
				# set to True, the program will end and suppress the thread
				# before it starts working !
