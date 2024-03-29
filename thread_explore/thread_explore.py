import logging
import threading
import time

def thread_function(name):
	logging.info("Thread %s: starting", name)
	
	for i in range(4):
		logging.info("Thread {} working".format(name))
		time.sleep(1)

	logging.info("Thread %s: finishing", name)

if __name__ == "__main__":
	format = "%(asctime)s: %(message)s"
	logging.basicConfig(format=format, level=logging.INFO,
						datefmt="%H:%M:%S")

	logging.info("Main    : before creating thread")
	x = threading.Thread(target=thread_function, args=(1,))
	logging.info("Main    : before running thread")
	x.start()
	logging.info("Main    : wait for the thread to finish")
	# x.join()
	logging.info("Main    : all done")