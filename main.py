from turtle import Screen
from my_turtule import MyTurtle
import time
from car import Car

my_turtle = MyTurtle()
car = Car()

screen = Screen()
screen.setup(width=800, height=600)
screen.tracer(0)

screen.onkey(my_turtle.go_up, "Up")
screen.onkey(my_turtle.go_down, "Down")


screen.listen()

game_is_on = True
while game_is_on:
    car.move()
    time.sleep(0.1)
    screen.update()  # Perform a TurtleScreen update. To be used when tracer is turned off.

screen.exitonclick()
