import threading, time

def my_func(name='', age=0):
	for i in range(5):
		print('My name is {}. I am {} years old'.format(name, age))
		time.sleep(1)

def start_with_callback(func, kwargs=None):
	"""Start 'func' in a new thread T, then start self (and return T)."""
	if kwargs is None:
		kwargs = {}
	
	t = threading.Thread(target=func, kwargs=kwargs)
	t.setName('Bus Callback ' + t.getName())
	t.daemon = True
	t.start()
	
	return t

start_with_callback(func=my_func, kwargs={'name': 'Jean-Pierre', 'age': 60})
time.sleep(6)   # necessary, otherwise, since the daemon thread property is
				# set to True, the program will end and suppress the thread
				# before it starts working !
