import traceback, sys

def ff():
	mySecondFunction()
	
def mySecondFunction():
	myThirdFunction()

def myThirdFunction():
	a_list = [1, 2, 3]
	
	print(a_list[3])

if __name__ == "__main__":
	try:
		ff()
	except:
		exc_type, exc_value, exc_traceback = sys.exc_info()
		traceback.print_exception(exc_type, exc_value, exc_traceback)