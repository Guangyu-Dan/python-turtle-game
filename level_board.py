from turtle import Turtle

class Levelboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.level=0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-330, 250)
        self.write(f'level:{self.level}', align="center", font=("Courier", 20, "normal"))
