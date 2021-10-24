
class Snake:
    def __init__(self):
        self.dir = 0 # 0,1,2,3
        self.positions = [(0,0)]

class GreedySnakeUI :
    def __init__(self):
        self.snake = Snake()
        self.food = [(2,3), (3, 5)]

        self.hight = 100
        self.width = 100

ui = GreedySnakeUI()
