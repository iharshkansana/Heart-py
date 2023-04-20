import turtle
import time

# Creating a turtle object(pen)
pen = turtle.Turtle()

# Defining a method to draw curve
def curve():
    for i in range(200):
        # Defining step by step curve motion
        pen.right(1)
        pen.forward(1)

# Defining method to draw a full heart
def heart():
    pen.fillcolor('black')
    pen.begin_fill()

    # Draw the left line
    pen.left(140)
    pen.forward(113)

    # Draw the left curve
    curve()
    pen.left(120)

    # Draw the right curve
    curve()

    # Draw the right line
    pen.forward(112)

    # Ending the filling of the color
    pen.end_fill()

# Defining method to write text
def txt():
    pen.up()
    pen.color('pink')
    pen.setpos(-22, 65)
    pen.write("Harsh", font=("Courier new", 12, "bold"))
    pen.setpos(-8, 85)
    pen.color('red')
    pen.write("❤️", font=("Courier new", 12, "bold"))
    pen.color('pink')
    pen.setpos(-35, 105)
    pen.write("SDBC", font=("Courier new", 12, "bold"))
    pen.down()

heart()
txt()
pen.ht()
time.sleep(50)
