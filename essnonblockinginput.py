import msvcrt
import time

'''
Warning: works on Windows only !
'''
num = 0
done = False

while not done:
    print(num)
    num += 1

    if msvcrt.kbhit():
        print("you pressed '" + msvcrt.getch().decode('utf-8') + "', so now I quit")
        done = True
    else:
        time.sleep(0.5)