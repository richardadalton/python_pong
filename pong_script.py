import pygame
import sys
from pong import Pong, paddle_size

white = 255, 255, 255
width, height = 1000, 500

ball = {
    "x": 40,
    "y": 250,
    "vx": 5,
    "vy": 5
}



def clear_screen(screen):
    screen.fill((0, 0, 0))


# Court
def draw_court(screen):
    rectangle = (495, 0, 10, 500)
    pygame.draw.rect(screen, white, rectangle)


# Ball
def draw_ball(screen, ball):
    rectangle = (ball['x'], ball['y'], 20, 20)
    pygame.draw.rect(screen, white, rectangle)

def move_ball(ball):
    ball['x'] += ball['vx']
    ball['y'] += ball['vy']

def reset_ball_left(ball):
    ball['x'] = 40
    ball['y'] = 250
    ball['vx'] = 0
    ball['vy'] = 0

def reset_ball_right(ball):
    ball['x'] = 940
    ball['y'] = 250
    ball['vx'] = 0
    ball['vy'] = 0


# Paddle
def draw_paddle(screen, paddle):
    rectangle = (paddle.x, paddle.y, 10, paddle_size)
    pygame.draw.rect(screen, white, rectangle)


def draw_paddles(screen, pong):
    draw_paddle(screen, pong.leftPaddle)
    draw_paddle(screen, pong.rightPaddle)


def check_collisions(ball, pong):
    def check_hit_top_wall():
        if ball['y'] < 0 or ball['y'] > (height - 20):
            ball['vy'] = -ball['vy']
            hit_wall.play()

    def check_hit_left_paddle():
        if ball['x'] == 30 and ball['y'] >= pong.leftPaddle.y and ball['y'] <= (pong.leftPaddle.y + paddle_size):
            ball['vx'] = -ball['vx']
            hit_paddle.play()

    def check_hit_right_paddle():
        if ball['x'] == 960 and ball['y'] >= pong.rightPaddle.y and ball['y'] <= (pong.rightPaddle.y + paddle_size):
            ball['vx'] = -ball['vx']
            hit_paddle.play()

    def check_score_left():
        if ball['x'] < 0:
            reset_ball_left(ball)

    def check_score_right():
        if ball['x'] > 1000:
            reset_ball_right(ball)

    check_hit_top_wall()
    check_hit_left_paddle()
    check_hit_right_paddle()
    check_score_left()
    check_score_right()


def refresh_screen(screen, width, height):
    clear_screen(screen)
    draw_court(screen)
    draw_ball(screen, ball)
    draw_paddles(screen, pong)
    pygame.display.update()



pygame.init()
hit_wall = pygame.mixer.Sound('pong_wall.wav')
hit_paddle = pygame.mixer.Sound('pong_wall.wav')

screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

pong = Pong()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_q]:
        pong.moveLeftUp()
    if keys[pygame.K_a]:
        pong.moveLeftDown()

    if keys[pygame.K_p]:
        pong.moveRightUp()
    if keys[pygame.K_l]:
        pong.moveRightDown()

    if keys[pygame.K_SPACE]:
        if ball['vx'] == 0:
            if ball['x'] == 40:
                ball['vx'] = 5
                ball['vy'] = 5
            else:
                ball['vx'] = -5
                ball['vy'] = -5

    move_ball(ball)
    check_collisions(ball, pong)
    refresh_screen(screen, width, height)
