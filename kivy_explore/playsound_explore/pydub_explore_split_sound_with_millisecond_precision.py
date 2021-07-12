from pydub import AudioSegment
import time

# https://github.com/jiaaro/pydub

audioPath = 'D:\\Users\\Jean-Pierre\\Downloads\\Audiobooks\\Various\\#9 Jancovici a répondu à vos questions - 26_05_2021.mp3'
#audioPath = 'D:\\Users\\Jean-Pierre\\Downloads\\Audiobooks\\Various\\Wear a mask. Help slow the spread of Covid-19..mp3'

st = time.time()
song = AudioSegment.from_mp3(audioPath)
se = time.time()
print(st-se)
# pydub does things in milliseconds
duration = 50 * 1000
firstPortion = song[48000:duration]
lastPortion = song[-20000:-7000]

# boost volume by 15dB
beginning = firstPortion + 15

# reduce volume by 15dB
end = lastPortion - 15

total = beginning + end

totalPath_1 = 'D:\\Users\\Jean-Pierre\\Downloads\\Audiobooks\\Various\\total_1.mp3'
total.export(totalPath_1, format="mp3")

se = time.time()
print(st-se)

firstPortion = song[48500:duration]
lastPortion = song[-20000:-7500]

# reduce volume by 15dB
beginning = firstPortion - 15

# boost volume by 15dB
end = lastPortion + 15

total = beginning + end

totalPath_2 = 'D:\\Users\\Jean-Pierre\\Downloads\\Audiobooks\\Various\\total_2.mp3'
total.export(totalPath_2, format="mp3")



