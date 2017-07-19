from turtle import *
import math

# Name your Turtle.
t = Turtle()


# Set Up your screen and starting position.
setup(500,300)
x_pos = -250
y_pos = -150
#t.setposition(x_pos, y_pos)
sides = int(input("How many sides should I draw? I you want to see a cool pattern only enter 3, 4, or 6."))
### Write your code below:
def makeShapes ():
    counter=0
    while counter <= sides:
        pendown()
        forward(30)
        left(360/sides)
        counter = counter + 1
    penup()

def repeatShapes ():
    answer = int(input("how many times?"))
    counter2 = 0
    while counter2 < answer:
        makeShapes()
        left (((sides-2)*180)/sides)
        counter2 += 1

#ef drawCircle (radius, extent, steps):
    #import turtle
    #turtle.speed(0)
    #pendown()
    #forward(radius)
    #while steps < steps + 1:
        #steps = 0
        #right(extent)
        #forward(steps)
        #steps += steps




    # Name your Turtle.
repeatShapes()

#drawCircle(30, 180, 20)




# Close window on click.
exitonclick()
