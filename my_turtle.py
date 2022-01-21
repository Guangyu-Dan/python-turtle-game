from turtle import Turtle


class My_turtle(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("turtle")
        self.penup()
        self.y_move = 20
        self.shapesize(1.5,1.5,1)

    def move(self):
        new_y = self.ycor() + self.y_move
        self.goto(0, new_y)

    def reset_position(self):
        self.goto(0, -260)

    def reset_orientation(self):
        self.left(90)


