from turtle import Screen, Turtle
import time
from random import randint
from snake import Snake
from food import Food
from scoreboard import Scoreboard

#Setting Up
screen = Screen()
screen.bgcolor("black")
screen.setup(600,600)
screen.title("Snake Adventure")
screen.tracer(0)
#Creating Snake
snake = Snake()
score = Scoreboard()

#KEYBOARD FUNCTIONS
screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Right", fun=snake.right)
screen.onkey(key="Left", fun=snake.left)
screen.listen()

#CHECK FOOD
def check_food():
    global food
    for i in range(int(snake.segments[0].pos()[0] -20), int(snake.segments[0].pos()[0] + 20)):
        for j in range(int(snake.segments[0].pos()[1] -20), int(snake.segments[0].pos()[1] + 20)):
            if food.pos == (i, j):
                score.increase_score()
                food.delete_food()
                food = Food()
                snake.grow()



#WORKING #WORKING #WORKING #WORKING #WORKING #WORKING #WORKING #WORKING #WORKING #WORKING #WORKING #WORKING #WORKING
game_is_on = True

#create food
food = Food()

while game_is_on:
    time.sleep(0.1)
    screen.tracer(0)

    snake.move()



    screen.update()


    # Check if food eaten
    check_food()


    # Check Body Hit
    for i in range(1, len(snake.segments)):
        if snake.segments[0].distance(snake.segments[i]) < 10:
            game_is_on = False



    #Check Wall Hit
    if (snake.segments[0].xcor() > 270 or snake.segments[0].xcor() < -270 or snake.segments[0].ycor() > 270 or
            snake.segments[0].ycor() < -270):
        game_is_on = False

    if game_is_on == False:
        over = Scoreboard()
        over.gameover()
        if score.score > score.highscore:
            with open("Data.txt", mode = "w") as data:
                data.write(f"{score.score}")


screen.exitonclick()
