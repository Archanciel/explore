import threading, time

def my_func(name='', age=0):
	print('My name is {}. I am {} years old'.format(name, age))
	
def start_with_callback(func, args=None, kwargs=None):
	"""Start 'func' in a new thread T, then start self (and return T)."""
	if args is None:
		args = ()
	if kwargs is None:
		kwargs = {}
	args = (func,) + args
	
	def _callback(func, *a, **kw):
		for i in range(5):
			time.sleep(1)
			func(*a, **kw)
	
	t = threading.Thread(target=_callback, args=args, kwargs=kwargs)
	t.setName('Bus Callback ' + t.getName())
	t.start()
	
	return t

start_with_callback(func=my_func, kwargs={'name': 'Jean-Pierre', 'age': 60})