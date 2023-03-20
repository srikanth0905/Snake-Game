from turtle import Turtle, Screen

# setting up screen to play the game
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")

# creating 3 turtle/squares which will form snake and placing them side by side to each other
starting_position = [(0, 0), (-20, 0), (-40, 0)]
for position in starting_position:
    new_segment = Turtle(shape="square")
    new_segment.color("white")
    new_segment.goto(position)











screen.exitonclick()
