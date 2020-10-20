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
    t = threading.Thread(target=thread_function, args=(1,))
    logging.info("Main    : before running thread")
    t.daemon = True
    t.start()
    logging.info("Main    : wait 2 seconds before closing the daemon thread")
    time.sleep(2)
    # t.join()
    logging.info("Main    : all done")