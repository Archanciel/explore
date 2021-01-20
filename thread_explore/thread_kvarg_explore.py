import threading, time

def my_func(name='', age=0):
	print('My name is {}. I am {} years old'.format(name, age))
	
def start_with_callback(func, kwargs=None):
	"""Start 'func' in a new thread T, then start self (and return T)."""
	if kwargs is None:
		kwargs = {}
	
	def _callback(func, **kw):
		for i in range(5):
			time.sleep(1)
			func(**kw)
	
	t = threading.Thread(target=_callback, args=(func,), kwargs=kwargs)
	t.start()
	
	return t

start_with_callback(func=my_func, kwargs={'name': 'Jean-Pierre', 'age': 60})