from turtle import Turtle
import time


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.s = 0
        file = open("HighScore.txt")
        self.high_score = int(file.read())
        file.close()
        self.color("white")
        self.penup()
        self.goto(0, 267)
        self.write(f"Score: {self.s}", move=False, align='center', font=('Arial', 12, 'normal'))
        self.hideturtle()

    def increase_score(self):
        self.s += 1
        self.clear()
        self.write(f"Score: {self.s}              High score: {self.high_score}", move=False, align='center', font=('Arial', 12, 'normal'))

    # def game_over(self):
    #     self.goto(x=0, y=0)
    #     for _ in range(0,4):
    #         self.clear()
    #         self.color("white")
    #         self.write("GAME OVER!", move=False, align='center', font=('Arial', 12, 'normal'))
    #         time.sleep(0.1)
    #         self.clear()
    #         self.color("maroon")
    #         self.write("GAME OVER!", move=False, align='center', font=('Arial', 12, 'normal'))
    #         time.sleep(0.1)

    def reset(self):
        if self.s > self.high_score:
            self.high_score = self.s
            file = open("HighScore.txt", "w")
            file.write(f"{self.high_score}")
            file.close()
        self.s = -1
        self.increase_score()
