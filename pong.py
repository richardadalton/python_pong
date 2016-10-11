from paddle import Paddle, paddle_size

width_of_court = 1000
height_of_court = 500
paddle_start_y = (height_of_court / 2) - (paddle_size / 2)
paddle_upper_limit = 0
paddle_lower_limit = height_of_court - paddle_size

class Pong:

    def __init__(self):
        self.leftPaddle = Paddle(20, 210)
        self.rightPaddle = Paddle(970, 210)

    def moveLeftUp(self):
        if self.leftPaddle.y > 0:
            self.leftPaddle.moveUp()


    def moveLeftDown(self):
        if self.leftPaddle.y < (500 - 80):
            self.leftPaddle.moveDown()


    def moveLeftTo(self, y):
        self.leftPaddle.moveTo(y)


    def moveRightUp(self):
        if self.rightPaddle.y > 0:
            self.rightPaddle.moveUp()


    def moveRightDown(self):
        if self.rightPaddle.y < (500 - 80):
            self.rightPaddle.moveDown()


    def moveRightTo(self, y):
        self.rightPaddle.moveTo(y)
