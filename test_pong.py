import unittest
from config import Config
from pong import Pong
from paddle import Paddle
from ball import Ball
import pygame


class TestPong(unittest.TestCase):

    def setUp(self):
        pygame.init()

    # Ball
    def test_ball_start_position(self):
        hit_wall = pygame.mixer.Sound('pong_wall.wav')
        hit_paddle = pygame.mixer.Sound('pong_wall.wav')
        pong = Pong(hit_wall, hit_paddle)

        self.assertEqual(pong.ball.x, Config.ball_left_start_x)
        self.assertEqual(pong.ball.y, Config.ball_left_start_y)

    def test_ball_serve_left(self):
        hit_wall = pygame.mixer.Sound('pong_wall.wav')
        hit_paddle = pygame.mixer.Sound('pong_wall.wav')
        pong = Pong(hit_wall, hit_paddle)

        pong.serve_left()
        self.assertEqual(pong.ball.x, Config.ball_left_start_x)
        self.assertEqual(pong.ball.y, Config.ball_left_start_y)
        self.assertEqual(pong.ball.vx, Config.ball_serve_left_vx)
        self.assertEqual(pong.ball.vy, Config.ball_serve_left_vy)

    def test_ball_serve_right(self):
        hit_wall = pygame.mixer.Sound('pong_wall.wav')
        hit_paddle = pygame.mixer.Sound('pong_wall.wav')
        pong = Pong(hit_wall, hit_paddle)

        pong.serve_right()
        self.assertEqual(pong.ball.x, Config.ball_right_start_x)
        self.assertEqual(pong.ball.y, Config.ball_right_start_y)
        self.assertEqual(pong.ball.vx, Config.ball_serve_right_vx)
        self.assertEqual(pong.ball.vy, Config.ball_serve_right_vy)

    def test_move_ball(self):
        hit_wall = pygame.mixer.Sound('pong_wall.wav')
        hit_paddle = pygame.mixer.Sound('pong_wall.wav')
        pong = Pong(hit_wall, hit_paddle)

        pong.move_ball()
        self.assertEqual(pong.ball.x, Config.ball_left_start_x + Config.ball_serve_left_vx)
        self.assertEqual(pong.ball.y, Config.ball_left_start_y + Config.ball_serve_left_vy)


    def test_bounce_ball_against_top_wall(self):
        hit_wall = pygame.mixer.Sound('pong_wall.wav')
        hit_paddle = pygame.mixer.Sound('pong_wall.wav')
        pong = Pong(hit_wall, hit_paddle)

        pong.ball = Ball(Config.ball_left_start_x, 10, 5, -5, -5)
        pong.move_ball()
        self.assertEqual(pong.ball.vx, -5)
        self.assertEqual(pong.ball.vy, 5)

    def test_bounce_ball_against_bottom_wall(self):
        hit_wall = pygame.mixer.Sound('pong_wall.wav')
        hit_paddle = pygame.mixer.Sound('pong_wall.wav')
        pong = Pong(hit_wall, hit_paddle)

        pong.ball = Ball(Config.ball_left_start_x, 500 - 10, 5, 5)
        pong.move_ball()
        self.assertEqual(pong.ball.vx, 5)
        self.assertEqual(pong.ball.vy, -5)

    def test_bounce_ball_against_left_paddle(self):
        hit_wall = pygame.mixer.Sound('pong_wall.wav')
        hit_paddle = pygame.mixer.Sound('pong_wall.wav')
        pong = Pong(hit_wall, hit_paddle)

        pong.ball = Ball(30, 250, 5, -5, -5)
        pong.move_ball()
        self.assertEqual(pong.ball.vx, 5)
        self.assertEqual(pong.ball.vy, -5)

    def test_bounce_ball_against_right_paddle(self):
        hit_wall = pygame.mixer.Sound('pong_wall.wav')
        hit_paddle = pygame.mixer.Sound('pong_wall.wav')
        pong = Pong(hit_wall, hit_paddle)

        pong.ball = Ball(970, 250, 5, 5, 5)
        pong.move_ball()
        self.assertEqual(pong.ball.vx, -5)
        self.assertEqual(pong.ball.vy, 5)

    def test_ball_missed_on_left(self):
        hit_wall = pygame.mixer.Sound('pong_wall.wav')
        hit_paddle = pygame.mixer.Sound('pong_wall.wav')
        pong = Pong(hit_wall, hit_paddle)

        pong.ball = Ball(-5, 250, -5, -5)
        pong.move_ball()
        self.assertEqual(pong.ball.x, Config.ball_left_start_x)
        self.assertEqual(pong.ball.y, Config.ball_left_start_y)
        self.assertEqual(pong.ball.vx, 0)
        self.assertEqual(pong.ball.vy, 0)

    def test_ball_missed_on_right(self):
        hit_wall = pygame.mixer.Sound('pong_wall.wav')
        hit_paddle = pygame.mixer.Sound('pong_wall.wav')
        pong = Pong(hit_wall, hit_paddle)

        pong.ball = Ball(1005, 250, 5, 5)
        pong.move_ball()
        self.assertEqual(pong.ball.x, Config.ball_right_start_x)
        self.assertEqual(pong.ball.y, Config.ball_right_start_y)
        self.assertEqual(pong.ball.vx, 0)
        self.assertEqual(pong.ball.vy, 0)


    # Paddle
    def test_can_not_move_paddle_above_upper_limit(self):
        hit_wall = pygame.mixer.Sound('pong_wall.wav')
        hit_paddle = pygame.mixer.Sound('pong_wall.wav')
        pong = Pong(hit_wall, hit_paddle)

        paddle = Paddle(20, 40, Config.paddle_upper_limit, Config.paddle_lower_limit)
        pong.leftPaddle = paddle
        pong.move_left_up()
        self.assertEqual(pong.leftPaddle.y, Config.paddle_upper_limit)

    def test_can_not_move_paddle_below_lower_limit(self):
        hit_wall = pygame.mixer.Sound('pong_wall.wav')
        hit_paddle = pygame.mixer.Sound('pong_wall.wav')
        pong = Pong(hit_wall, hit_paddle)

        paddle = Paddle(20, 460, Config.paddle_upper_limit, Config.paddle_lower_limit)
        pong.leftPaddle = paddle
        pong.move_left_down()
        self.assertEqual(pong.leftPaddle.y, Config.paddle_lower_limit)


    # Left Paddle
    def test_left_paddle_start_position(self):
        hit_wall = pygame.mixer.Sound('pong_wall.wav')
        hit_paddle = pygame.mixer.Sound('pong_wall.wav')
        pong = Pong(hit_wall, hit_paddle)

        self.assertEqual(pong.leftPaddle.x, Config.paddle_left_start_x)
        self.assertEqual(pong.leftPaddle.y, Config.paddle_left_start_y)

    def test_can_move_left_paddle_up(self):
        hit_wall = pygame.mixer.Sound('pong_wall.wav')
        hit_paddle = pygame.mixer.Sound('pong_wall.wav')
        pong = Pong(hit_wall, hit_paddle)

        pong.move_left_up()
        self.assertEqual(pong.leftPaddle.y, Config.paddle_left_start_y - pong.leftPaddle.step_size)

    def test_can_move_left_paddle_down(self):
        hit_wall = pygame.mixer.Sound('pong_wall.wav')
        hit_paddle = pygame.mixer.Sound('pong_wall.wav')
        pong = Pong(hit_wall, hit_paddle)

        pong.move_left_down()
        self.assertEqual(pong.leftPaddle.y, Config.paddle_left_start_y + pong.leftPaddle.step_size)


    # Right Paddle
    def test_right_paddle_start_position(self):
        hit_wall = pygame.mixer.Sound('pong_wall.wav')
        hit_paddle = pygame.mixer.Sound('pong_wall.wav')
        pong = Pong(hit_wall, hit_paddle)

        self.assertEqual(pong.rightPaddle.x, Config.paddle_right_start_x)
        self.assertEqual(pong.rightPaddle.y, Config.paddle_right_start_y)

    def test_can_move_right_paddle_up(self):
        hit_wall = pygame.mixer.Sound('pong_wall.wav')
        hit_paddle = pygame.mixer.Sound('pong_wall.wav')
        pong = Pong(hit_wall, hit_paddle)

        pong.move_right_up()
        self.assertEqual(pong.rightPaddle.y, Config.paddle_right_start_y - pong.rightPaddle.step_size)

    def test_can_move_right_paddle_down(self):
        hit_wall = pygame.mixer.Sound('pong_wall.wav')
        hit_paddle = pygame.mixer.Sound('pong_wall.wav')
        pong = Pong(hit_wall, hit_paddle)

        pong.move_right_down()
        self.assertEqual(pong.rightPaddle.y, Config.paddle_right_start_y + pong.rightPaddle.step_size)



if __name__ == '__main__':
    unittest.main()