import subprocess
import time
import pyautogui

EVERNOTE_TIME_SLEEP = 0.2

attachmentFilePathName = r'D:\Users\Jean-Pierre\Downloads\Audiobooks\Various\Wear a mask. Help slow the spread of Covid-19._1.mp3'
noteTitle = 'Essai note audio'

subprocess.call([r'C:\Users\Jean-Pierre\AppData\Local\Programs\Evernote\Evernote.exe'])

# Créer
#time.sleep(1)
pyautogui.click(248, 408)

# Note
time.sleep(EVERNOTE_TIME_SLEEP)
pyautogui.click(248, 408)

# + icon
time.sleep(EVERNOTE_TIME_SLEEP * 20)
pyautogui.click(1209, 248)

# Pièce jointe
time.sleep(EVERNOTE_TIME_SLEEP)
pyautogui.click(1002, 571)

# File field
time.sleep(EVERNOTE_TIME_SLEEP)
pyautogui.typewrite(attachmentFilePathName)

# Open button
time.sleep(EVERNOTE_TIME_SLEEP)
pyautogui.click(859, 870)

# Note title
time.sleep(EVERNOTE_TIME_SLEEP * 10)
pyautogui.click(1233, 370)
time.sleep(EVERNOTE_TIME_SLEEP)
pyautogui.typewrite(noteTitle)

