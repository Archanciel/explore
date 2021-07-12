import pywhatkit as py

phoneNumber = "+41{768224987}"
audioPath = "D:\\Users\\Jean-Pierre\\Downloads\\Audiobooks\\Mon expérience de MORT imminente  - et si l'AMOUR  était l'énergie physique la plus puissante _1.mp3"
audioPath = "D:\\Users\\Jean-Pierre\\Downloads\\images.png"

py.sendwhatmsg('f' + phoneNumber, "Hello Jean-Pierre, this is my message.", 0, 57, tab_close=True)
