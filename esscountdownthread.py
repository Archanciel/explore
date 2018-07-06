import time
from threading import Thread, Event

class ThreadedCountdown(Thread):
    def __init__(self, worker, event, duration):
        Thread.__init__(self)
        self.worker = worker
        self.stopped = event
        self.duration = duration

    def run(self):
        while not self.stopped.wait(1):
            print('\r' + str(self.duration), end='')
            self.duration -= 1
            
            if self.duration < 0:
                self.worker.stop()
                self.stopped.set()
            # call a function

class Worker:
    def __init__(self):
        self.finish = False
        
    def work(self):
        for i in range(5):
            if self.finish:
                break
            print("processing {}".format(i))
            time.sleep(4)
            
    def stop(self):
        self.finish = True

worker = Worker()    
stopFlag = Event()
countdown = ThreadedCountdown(worker, stopFlag, 10)
countdown.start()
worker.work()

# this will stop the threaded countdown
# once in case the worker has finished
# working before the countdown is over
stopFlag.set()