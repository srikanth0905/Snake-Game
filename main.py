from turtle import Turtle, Screen
import time

# setting up screen to play the game
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)  # this will turn off animation, which will get rid of jarring snake
screen.title("Snake Game")

# creating 3 turtle/squares which will form snake and placing them side by side to each other
starting_position = [(0, 0), (-20, 0), (-40, 0)]
segments = []
for position in starting_position:
    new_segment = Turtle(shape="square")
    new_segment.color("white")
    new_segment.penup()
    new_segment.goto(position)
    segments.append(new_segment)

# moving the snake forward
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    # moving the last block to the second-last block, so the rest of body follows snake's head
    # the range in for loop is (last block should move, to which new position, by how much block)
    for seg_num in range(len(segments) - 1, 0, -1):
        new_x = segments[seg_num - 1].xcor()
        new_y = segments[seg_num - 1].ycor()
        segments[seg_num].goto(new_x, new_y)
    segments[0].forward(20)

screen.exitonclick()
