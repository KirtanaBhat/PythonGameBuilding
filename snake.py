from turtle import Turtle
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.squares = []
        self.create_snake()

    def create_snake(self):
        for pos in STARTING_POSITIONS:
            self.add_square(pos)

    def add_square(self, position):
        new_sq = Turtle("circle")
        new_sq.color("teal")
        new_sq.penup()
        new_sq.goto(position)
        self.squares.append(new_sq)

    def increase_snake_length(self):
        self.add_square(self.squares[-1].position())

    def move(self):
        for i in range(len(self.squares) - 1, 0, -1):
            self.squares[i].goto(self.squares[i - 1].xcor(), self.squares[i - 1].ycor())
        self.squares[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.squares[0].heading() != DOWN:
            self.squares[0].setheading(UP)

    def down(self):
        if self.squares[0].heading() != UP:
            self.squares[0].setheading(DOWN)

    def left(self):
        if self.squares[0].heading() != RIGHT:
            self.squares[0].setheading(LEFT)

    def right(self):
        if self.squares[0].heading() != LEFT:
            self.squares[0].setheading(RIGHT)

    def reset(self):
        for i in self.squares:
            i.goto(1000, 1000)
        self.squares.clear()
        self.create_snake()