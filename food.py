from turtle import Turtle
from random import choice
class Food:
    def __init__(self):
        self.ball = Turtle("circle")
        self.ball.color("red")
        self.ball.shapesize(0.6, 0.6, 0.5)
        self.pos = self.create_food()

    def create_food(self):
        COORDINATES = []
        for num in range(-280, +280, 10):
            COORDINATES.append(num)
        x = choice(COORDINATES)
        y = choice(COORDINATES)
        self.ball.teleport(x, y)
        return (x,y)
    def delete_food(self):
        self.ball.hideturtle()
