import webbrowser
import pyautogui
import time

# The browser used is Brave on Windows 10. According to your PC,
# you may have to alter the click() coordinates. Watch this video
# to understand how pyautogui is used to get the mouse position:
# https://www.youtube.com/watch?v=xVR-8xuBp3k&t=38s
#
# Then, use pyautogui_get_position.py to get the mouse positions ...

whatsAppUrl = 'https://web.whatsapp.com/'
contactTargetName = '822' # part of target phone number
message = 'Hello, I send you an audio file ...'
attachmentFilePathName = r'D:\Users\Jean-Pierre\Downloads\Audiobooks\Various\Wear a mask. Help slow the spread of Covid-19._1.mp3'

webbrowser.open(whatsAppUrl)
time.sleep(5)

# click on contact search field
pyautogui.click(152, 247)

# select the targer contact
pyautogui.typewrite(contactTargetName)
time.sleep(2)

# activate the targer contact
pyautogui.click(202, 468)
time.sleep(1)

# send text message before sending the audio file
pyautogui.click(988, 1395)
pyautogui.typewrite(message)
pyautogui.click(2105, 1390)

# click on attachment icon
pyautogui.click(894, 1385)

# click on photo/video icon. Sending audio works if it is sent as a photo
# or video !
time.sleep(0.5)
pyautogui.click(894, 1268)

# enter attachment file path name
time.sleep(0.5)
pyautogui.typewrite(attachmentFilePathName)

# click on Open button
pyautogui.click(795,776)

# click on Send icon
print('Time sleeping for 20 seconds to make sure the audio file is uploaded ...')
time.sleep(20)
pyautogui.click(2060,1203)
