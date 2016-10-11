
paddle_size = 80
paddle_step_size = 5

class Paddle:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def moveUp(self):
        self.y -= 5

    def moveDown(self):
        self.y += 5

    def moveTo(self, y):
        self.y = y
