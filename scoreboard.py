from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 240)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(0, 240)
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def draw_background(self):
        pass

    def game_over(self):
        self.goto(0, 0)
        self.color("red")
        self.write("GAME OVER", align=ALIGNMENT, font=("Courier", 36, "bold"))
        self.color("white")

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()