import pygame
import time
from pygame.locals import *

def display(str):
    text = font.render(str, True, (255, 255, 255), (0, 0, 0))
    textRect = text.get_rect()
    textRect.centerx = screen.get_rect().centerx
    textRect.centery = screen.get_rect().centery

    screen.blit(text, textRect)
    pygame.display.update()

pygame.init()
screen = pygame.display.set_mode( (640,480) )
pygame.display.set_caption('Python numbers')

font = pygame.font.Font(None, 27)

num = 0
done = False
while not done:
    display( str(num) )
    num += 1

    pygame.event.pump()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        done = True
    else:
        time.sleep(0.2)