import pygame.mixer

SOUND_FILE = 'c:/temp/JMJ.mp3'
#SOUND_FILE = '/storage/emulated/0/music/JMJ.mp3'

pygame.mixer.pre_init(44100, -16, 2, 2048) # if missing, the play speed will be too slow
pygame.mixer.init()

pygame.mixer.music.load(SOUND_FILE)
pygame.mixer.music.play(loops=0, start=1626)
pygame.init() # required for pygame.event.wait() to work !

while pygame.mixer.music.get_busy():
    pygame.event.wait()

