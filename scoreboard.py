from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("high_score.txt") as data:
            self.high_score = int(data.read())
        self.goto(-30, 270)
        self.penup()
        self.color("white")
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        if self.score >= self.high_score:
            with open("high_score.txt", mode="w") as file:
                file.write(str(self.score))
            with open("high_score.txt", mode="r") as file:
                self.high_score = int(file.read())
        self.write(f"Score: {self.score} High score: {self.high_score}", font=FONT)

    def increase_score(self):
        self.score += 1

    def reset(self):
        self.score = 0

    # def game_over(self):
    #     self.goto(-50, 0)
    #     self.write("Game over", font=FONT)
