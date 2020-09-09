import logging
from logging import info as v
from logging import debug as d
from logging import error, warning

def myFunction():
	v("Verbose messages explain normal functioning. v() aka logging.info()")
	d("Debug messages show technical details of the program. d() aka logging.debug().")
	warning("Warnings are for problems that still allow the program to run. logging.warning().")
	error("Errors mean a failed operation. logging.error(). Also consider sys.exit('Fobarization failed.') or raise().")
	logging.info('ii')
def main():
	logging.basicConfig(level=logging.INFO, format="%(funcName)s():%(lineno)i: %(message)s %(levelname)s")
	print("Use print() to always show lines. For example, normal program output. ")
	myFunction()
	
if __name__ == "__main__":
	main()