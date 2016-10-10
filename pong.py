import pygame
import sys
from pygame.locals import *

white = 255, 255, 255
width, height = 1000, 500

b1x, b1y = 20, 250

x, y = 40, 250
vx, vy = 5, 5




def clear_screen(screen):
    screen.fill((0, 0, 0))

def draw_ball(screen):
    rectangle = (x, y, 20, 20)
    pygame.draw.rect(screen, white, rectangle)


def draw_bat(screen):
    rectangle = (b1x, b1y, 10, 80)
    pygame.draw.rect(screen, white, rectangle)


def refresh_screen(screen, width, height):
    clear_screen(screen)
    draw_ball(screen)
    draw_bat(screen)
    pygame.display.update()



pygame.init()
blip = pygame.mixer.Sound('pongblipf4.wav')

screen = pygame.display.set_mode((width, height))

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    x += vx
    y += vy

    if x < 10 and y < (b1y + 80) and y > b1y:
        vx = -vx
    elif x > (width - 20):
        vx = -vx
        blip.play()
    elif y < 0 or y > (height - 20):
        vy = -vy
        blip.play()


    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        b1y -= 5
    if keys[pygame.K_DOWN]:
        b1y += 5

    refresh_screen(screen, width, height)
