from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("Green")
        self.speed("fastest")
        self.Refresh()

    def Refresh(self):
        RANDOM_X = random.randint(-280, 280)
        RANDOM_Y = random.randint(-280, 280)
        self.goto(RANDOM_X, RANDOM_Y)

