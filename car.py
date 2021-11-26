from turtle import Turtle
import random

colors = ["red", "black", "blue", "green", "purple"]


class Car(Turtle):
    def __init__(self, y_pos) -> None:
        super().__init__()
        self.hideturtle()
        self.shape("square")
        self.penup()
        self.color(random.choice(colors))
        self.shapesize(1, random.randrange(3, 5, 1))
        self.goto(random.randrange(-420, -800, -50), y_pos)
        self.showturtle()

    def move(self):
        self.forward(5)
