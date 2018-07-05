import sys
import time

for i in range(6):
    sys.stdout.write("\rDoing thing %i" % i)
    #sys.stdout.flush()
    time.sleep(1)

#Not working !
#for i in range(3):
#    print("\rDoing thing %i" % i, '')
#    time.sleep(1)
