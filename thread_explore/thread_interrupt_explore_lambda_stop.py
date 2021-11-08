# Python program killing
# threads using stop
# flag
#
# https://www.geeksforgeeks.org/python-different-ways-to-kill-a-thread/

import threading
import time


def run(stop):
	while True:
		print('thread running')
		if stop():
			print('stopping')
			break


def main():
	stop_threads = False
	t1 = threading.Thread(target=run, args=(lambda: stop_threads,))
	t1.start()
	time.sleep(1)
	stop_threads = True
	t1.join()
	time.sleep(1)


main()
