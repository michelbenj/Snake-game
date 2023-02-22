from turtle import Turtle

POSITION = [(0,0), (0,-20), (0,-40)]

MOVE_DISTANCE = 20

UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180
class Snake(Turtle):

    def __init__(self):
        self.snake_body = []
        self.create_snake()

    def create_snake(self):
        for initials in POSITION:
            self.extend_snake(initials)

    def extend_on_food(self):
        self.extend_snake(self.snake_body[-1].position())

    def extend_snake(self, position):
        body = Turtle()
        body.shape('Square')
        body.color('white')
        body.penup()
        body.goto(position)
        self.snake_body.append(body)

    def snake_reset(self):
        for seg in self.snake_body:
            seg.goto(1000,1000)
        self.snake_body.clear()
        self.create_snake()


    def move(self):

        for bodies in range(len(self.snake_body) - 1, 0, -1):
            next_x = self.snake_body[bodies - 1].xcor()
            next_y = self.snake_body[bodies - 1].ycor()
            self.snake_body[bodies].goto(next_x, next_y)
        self.snake_body[0].forward(MOVE_DISTANCE)

    def up(self):
        for heads in range(len(self.snake_body)):
            if self.snake_body[heads].heading() != DOWN:
                self.snake_body[heads].setheading(UP)

    def down(self):
        for heads in range(len(self.snake_body)):
            if self.snake_body[heads].heading() != UP:
                self.snake_body[heads].setheading(DOWN)

    def left(self):
        for heads in range(len(self.snake_body)):
            if self.snake_body[heads].heading() != RIGHT:
                self.snake_body[heads].setheading(LEFT)

    def right(self):
        for heads in range(len(self.snake_body)):
            if self.snake_body[heads].heading() != LEFT:
                self.snake_body[heads].setheading(RIGHT)


















