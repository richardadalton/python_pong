import unittest
from pong import Pong, paddle_start_y, paddle_upper_limit, paddle_lower_limit
from paddle import paddle_step_size

class Test_paddle(unittest.TestCase):


    def test_left_paddle_start_position(self):
        pong = Pong()
        self.assertEqual(pong.leftPaddle.x, 20)
        self.assertEqual(pong.leftPaddle.y, paddle_start_y)


    def test_can_move_left_paddle_up(self):
        pong = Pong()
        pong.moveLeftUp()
        self.assertEqual(pong.leftPaddle.y, paddle_start_y - paddle_step_size)


    def test_can_move_left_paddle_down(self):
        pong = Pong()
        pong.moveLeftDown()
        self.assertEqual(pong.leftPaddle.y, paddle_start_y + paddle_step_size)


    def test_can_not_move_left_paddle_up_if_touching_top_wall(self):
        pong = Pong()
        pong.leftPaddle.moveTo(paddle_upper_limit)
        pong.moveLeftUp()
        self.assertEqual(pong.leftPaddle.y, paddle_upper_limit)


    def test_can_not_move_left_paddle_down_if_touching_bottom_wall(self):
        pong = Pong()
        pong.moveLeftTo(paddle_lower_limit)
        pong.moveLeftDown()
        self.assertEqual(pong.leftPaddle.y, paddle_lower_limit)



    def test_right_paddle_start_position(self):
        pong = Pong()
        self.assertEqual(pong.rightPaddle.x, 970)
        self.assertEqual(pong.rightPaddle.y, paddle_start_y)


    def test_can_move_lright_paddle_up(self):
        pong = Pong()
        pong.moveRightUp()
        self.assertEqual(pong.rightPaddle.y, paddle_start_y - paddle_step_size)


    def test_can_move_right_paddle_down(self):
        pong = Pong()
        pong.moveRightDown()
        self.assertEqual(pong.rightPaddle.y, paddle_start_y + paddle_step_size)


    def test_can_not_move_right_paddle_up_if_touching_top_wall(self):
        pong = Pong()
        pong.rightPaddle.moveTo(paddle_upper_limit)
        pong.moveRightUp()
        self.assertEqual(pong.rightPaddle.y, paddle_upper_limit)


    def test_can_not_move_right_paddle_down_if_touching_bottom_wall(self):
        pong = Pong()
        pong.moveRightTo(paddle_lower_limit)
        pong.moveRightDown()
        self.assertEqual(pong.rightPaddle.y, paddle_lower_limit)
