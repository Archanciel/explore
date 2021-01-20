import logging
import threading
import time

def thread_function():
    logging.info("Thread starting")
    
    for i in range(4):
    	logging.info("Thread working")
    	time.sleep(1)

    logging.info("Thread finishing")

if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")

    logging.info("Main    : before creating thread")
    t = threading.Thread(target=thread_function, args=())
    logging.info("Main    : before running thread")
    t.daemon = True
    t.start()
    logging.info("Main    : wait 2 seconds before closing the daemon thread")
    time.sleep(5)
    # t.join()
    logging.info("Main    : all done")