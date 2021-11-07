import pygame

class Paddle:

    def __init__(self, x, y, upper_limit, lower_limit):
        self.x = x
        self.y = y
        self.upper_limit = upper_limit
        self.lower_limit = lower_limit
        self.size = 80
        self.step_size = 5

    def move_up(self):
        if self.y > self.upper_limit:
            self.y -= self.step_size

    def move_down(self):
        if self.y < self.lower_limit:
           self.y += self.step_size

    def draw(self, screen, color):
        rectangle = (self.x, self.y - (self.size / 2) , 10, self.size)
        pygame.draw.rect(screen, color, rectangle)
