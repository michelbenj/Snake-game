from turtle import Turtle

class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        with open("D:\data.txt") as file:
            number = file.read()
            self.high_score = int(number)
        self.color('white')
        self.goto(0,250)
        self.write(f"score: {self.score} High Score: {self.high_score}", align = 'center', font = ('arial', 24, 'normal'))

    def score_change(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align='center', font=('arial', 24, 'normal'))

    def score_inc(self):
        self.clear()
        self.score += 1
        self.write(f"Score: {self.score} High Score: {self.high_score}", align='center', font=('arial', 24, 'normal'))


    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("D:\data.txt", mode ="w") as file:
                file.write(f"{self.high_score}")
        self.score = 0
        self.score_change()


