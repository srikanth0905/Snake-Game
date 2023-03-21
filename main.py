from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time

# setting up screen to play the game
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)  # this will turn off animation, which will get rid of jarring snake
screen.title("Snake Game")


snake = Snake()
food = Food()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")

# moving the snake forward
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    # moving snake
    snake.move()

    # Detect snake eating food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.reset()
        snake.reset()

    # Detect collision with tail
    # if head collides with any segment on its tail, trigger game_over
    for segment in snake.segments[1:]: # this will check collision with all the segments except its head i.e.,[0]
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()

screen.exitonclick()
