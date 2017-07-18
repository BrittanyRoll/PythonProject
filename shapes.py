from turtle import *
import math

# Name your Turtle.
t = Turtle()


# Set Up your screen and starting position.
setup(500,300)
x_pos = -250
y_pos = -150
#t.setposition(x_pos, y_pos)
sides = int(input("How many sides should I draw?"))
### Write your code below:
def makeShapes ():
    counter=0
    while counter < sides:
        pendown()
        forward(30)
        right(360/sides)
        counter = counter + 1
    penup()

def repeatShapes ():
    answer = int(input("how many times?"))
    counter2 = 0
    while counter2 < answer:
        makeShapes()
        left (360/sides*2)
        counter2 = counter2 +=

repeatShapes()



# Close window on click.
exitonclick()
