import time, sys

def updateProgress(progress, total, fill = '-'): 
    #sys.stdout.write('\r[{0}] {1}%'.format('#' * progress, progress / total * 100))
    print('\r[{0}] {1}%'.format(fill * progress, progress / total * 100), end='')

for i in range(11):
    updateProgress(i, 10, '█')
    time.sleep(0.5)
print()
for i in range(11):
    updateProgress(i, 10)
    time.sleep(0.5)