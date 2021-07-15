import webbrowser
import pyautogui
import time
import winsound

#webbrowser.open('https://web.whatsapp.com/')
print('Position mouse and wait 10 seconds...')
time.sleep(10)
frequency = 2500  # Set Frequency To 2500 Hertz
duration = 500  # Set Duration To 500 ms
winsound.Beep(frequency, duration)
print(pyautogui.position())
