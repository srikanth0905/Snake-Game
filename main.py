from turtle import Screen
from snake import Snake
import time

# setting up screen to play the game
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)  # this will turn off animation, which will get rid of jarring snake
screen.title("Snake Game")


snake = Snake()

# moving the snake forward
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

screen.exitonclick()
