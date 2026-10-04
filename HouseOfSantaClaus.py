"""
This Python Skript draws the House of Santa Clause with Python turtle
"""

import math
import turtle

t = turtle.Turtle()

# Settings
t.hideturtle()  # Hide Turtle Arrow
t.speed(4)      # Setting Turtle Speed

# Calculation of the different Side lengths
straightLength = 500                                        # Defining the length of Line
diagonalLength = math.hypot(straightLength, straightLength) # Roof length is defined as Hypotenuse of the Lines 
houseHeight = straightLength * 1.5                          # Calculating the height of the House

# Go to the Starting Point for Drawing the House of Santa Clause
t.penup()                   # Make Turtle Arrow invisible
t.backward(straightLength / 2)
t.right(90)
t.forward(houseHeight / 2)
t.left(90)
t.pendown()                 # Make Turtle Arrow visible

# Drawing the House of Santa Cause
t.forward(straightLength)
t.left(135)
t.forward(diagonalLength)
t.right(135)
t.forward(straightLength)
t.right(135)
t.forward(diagonalLength)
t.right(135)
t.forward(straightLength)
t.right(45)
t.forward(diagonalLength / 2)
t.right(90)
t.forward(diagonalLength / 2)
t.right(45)
t.forward(straightLength)

# Keep Window open
turtle.mainloop()