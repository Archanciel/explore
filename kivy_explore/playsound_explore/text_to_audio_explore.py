import win32clipboard
from gtts import gTTS
import time
import tkinter as tk
import os
from pydub import AudioSegment
import soundfile as sf
import pyrubberband as pyrb


def create_mp3_from_text(text, lang="fr"):
	# converting text to mp3
	s = gTTS(text, lang=lang)
	print("Wait some seconds ...")
	s.save(f"text.mp3")
	
	# accelerating mp3
	increase_speed("text.mp3")

	# launches the audio file player
	os.system("analyzed_filepathX105.mp3")


def clip():
	win32clipboard.OpenClipboard()
	data = win32clipboard.GetClipboardData()
	win32clipboard.CloseClipboard()
	create_mp3_from_text(data)


def increase_speed(mp3FileName):
	sound = AudioSegment.from_file(mp3FileName)
	sound.export("text.wav", format="wav")
	y, sr = sf.read("text.wav")

	# Play back at 3X speed
	y_stretch = pyrb.time_stretch(y, sr, 3)
	sf.write("analyzed_filepathX105.wav", y_stretch, sr, format='wav')
	
	sound = AudioSegment.from_wav("analyzed_filepathX105.wav")
	sound.export("analyzed_filepathX105.mp3", format="mp3")

root = tk.Tk()
root.title("Select the text, press crtl + c then press the button")
root.geometry("400x200")
but = tk.Button(root, text="Get audio from clipboard", command=clip, width=20, height=10, bg="gold")
but.pack()

root.mainloop()
