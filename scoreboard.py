from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 16, "normal")
SCOREBOARD_COLOR = "white"


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        # reading high score from data.txt file
        with open("data.txt") as file:
            self.high_score = int(file.read())
        self.color(SCOREBOARD_COLOR)
        self.hideturtle()
        self.penup()
        self.goto(0, 275)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High-score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write(f"Game Over", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as file:
                file.write(str(self.high_score))
        self.score = 0
        self.update_scoreboard()

