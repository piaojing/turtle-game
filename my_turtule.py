from turtle import Turtle


class MyTurtle(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.hideturtle()
        self.penup()
        self.shape("turtle")
        # self.shapesize(5, 1)
        self.color("black")
        self.goto(0, -270)
        self.showturtle()
        self.setheading(90)

    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
