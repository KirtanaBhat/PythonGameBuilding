from turtle import Screen
from snake import Snake
from food import Food
# from playsound import playsound
from scoreboard import ScoreBoard
from border import Border
import time

score = ScoreBoard()
snake = Snake()
food = Food()
screen = Screen()
border = Border()
border.make_border()

screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.title("Snake")
screen.tracer(0)

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.squares[0].distance(food) < 20:
        food.refresh()
        screen.update()
        #playsound("nom nom nom.wav")
        snake.increase_snake_length()
        screen.update()
        score.increase_score()

    #Collision with wall
    if snake.squares[0].xcor() > 290 or snake.squares[0].xcor() < -290 or snake.squares[0].ycor() > 290 or snake.squares[0].ycor() < -270:
        score.reset()
        snake.reset()
        #playsound("Game_over.wav")

    #Collision with itself
    for sq in snake.squares[1:]:
        if snake.squares[0].distance(sq) < 10:
            score.reset()
            snake.reset()
            #playsound("Game_over.wav")





screen.exitonclick()