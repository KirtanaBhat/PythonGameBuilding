from turtle import Turtle


class Border(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(-290, 289)
        self.pensize(4)
        self.color("maroon")

    def make_border(self):
        self.speed("fastest")
        self.pendown()
        self.forward(582)
        self.setheading(270)
        self.forward(564)
        self.setheading(180)
        self.forward(582)
        self.pensize(2)
        self.setheading(90)
        self.forward(582)

