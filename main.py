from turtle import Screen
from my_turtule import MyTurtle
import time
from car import Car
import random


my_turtle = MyTurtle()

# make car
rand_y = random.sample(range(-5, 5), 8)
print("Rand Y Position: ", rand_y)
car_list = []
for car in range(8):
    car = Car(rand_y[car] * 40)
    car_list.append(car)

screen = Screen()
screen.setup(width=800, height=600)
screen.tracer(0)

screen.onkey(my_turtle.go_up, "Up")
screen.onkey(my_turtle.go_down, "Down")


screen.listen()
new_car = Car(random.randint(-250, 250))
game_is_on = True
while game_is_on:
    # for i in range(8):
    #     car_list[i].move()
    new_car.move()
    if new_car.xcor == -350:
        new_car = Car(random.randint(-250, 250))

    time.sleep(0.1)
    screen.update()  # Perform a TurtleScreen update. To be used when tracer is turned off.

screen.exitonclick()
