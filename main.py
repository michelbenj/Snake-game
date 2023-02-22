from turtle import Screen, Turtle, Shape
import random
import time
from Snake import Snake
from food import Food
from Scoreboard import Score
screen = Screen()
screen.setup(width = 600,height = 600)
screen.bgcolor('black')
screen.title("Snake Game")


s = Shape('compound')
poly = ((10,-10), (-10,-10), (-10,10), (10,10))
s.addcomponent(poly , 'white', 'white')
screen.register_shape("Square", s)
screen.tracer(0)

snake = Snake()
food = Food()
score = Score()


screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

snake_headx = snake.snake_body[0].xcor()
snake_heady = snake.snake_body[0].ycor


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.09)
    snake.move()
    if snake.snake_body[0].distance(food) < 15:
        food.Refresh()
        snake.extend_on_food()
        score.score_inc()
    if snake.snake_body[0].xcor() > 290 or snake.snake_body[0].xcor() < -290 or snake.snake_body[0].ycor() > 290 or snake.snake_body[0].ycor() < -290:
        score.reset()
        snake.snake_reset()




    for initials in range(len(snake.snake_body[1:])):
            if snake.snake_body[0].distance(snake.snake_body[1:][initials].position()) < 10:
                score.reset()
                snake.snake_reset()





screen.exitonclick()