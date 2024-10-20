from turtle import Turtle, Screen
import time

from food import Food
from scoreboard import Scoreboard
from snake import Snake

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("my snake game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.13)
    snake.move()

    # TODO 1. Detect the collision of the food
    if snake.head.distance(food) < 20:
        food.refresh()
        scoreboard.increase_score()
        scoreboard.update_scoreboard()
        snake.extend()

    # TODO 2.Detect the collision of the wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -300 or snake.head.ycor() > 300 or snake.head.ycor() < -290:
        scoreboard.reset()
        scoreboard.update_scoreboard()
        snake.reset()

    # TODO 3.Detect the collision of the tail
    for segment in snake.segment[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            scoreboard.update_scoreboard()
            snake.reset()


screen.exitonclick()

