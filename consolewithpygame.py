import pygame
import time
from pygame.locals import *

def display(str, centerx, centery):
    text = font.render(str, True, (255, 255, 255), (0, 0, 0))
    textRect = text.get_rect()
    textRect.centerx = centerx
    textRect.centery = centery

    screen.blit(text, textRect)
    pygame.display.update()

pygame.init()
screen = pygame.display.set_mode( (640,480) )
pygame.display.set_caption('Python numbers')

font = pygame.font.Font(None, 27)

centerx = screen.get_rect().centerx + screen.get_rect().centerx * 29 / 30
centery = screen.get_rect().centery + screen.get_rect().centery * 19 / 20

num = 0
done = False
while not done:
    display(str(num), centerx, centery)
    num += 1

    pygame.event.pump()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        done = True
    else:
        time.sleep(0.2)