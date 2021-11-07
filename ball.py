import pygame

class Ball:
    def __init__(self, x, y, size, vx=5, vy=5):
        self.x = x
        self.y = y
        self.size = size
        self.vx = vx
        self.vy = vy

    def bounce_off_paddle(self):
        self.vx *= -1

    def bounce_off_wall(self):
        self.vy *= -1

    def move(self):
        self.x += self.vx
        self.y += self.vy

    def draw(self, screen, color):
        rectangle = (self.x - self.size/2, self.y - self.size/2, self.size, self.size)
        pygame.draw.rect(screen, color, rectangle)
