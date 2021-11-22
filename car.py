from turtle import Turtle

colors = ["red", "black", "blue", "green", "purple"]


class Car(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.hideturtle()
        self.shape("square")
        self.penup()
        self.color("black")
        self.shapesize(1, 3)
        self.goto(-400, 0)
        self.showturtle()

    def move(self):
        self.forward(5)
