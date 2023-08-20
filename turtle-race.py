# Required modules
from turtle import *
from random import randint

# Set up the turtle graphics environment
speed(0)  # Set the maximum drawing speed
penup()
goto(-140, 140)  # Position the pen for labeling the racing track

# Draw the racing track with labels
for step in range(15):
    write(step, align='center')
    right(90)
    for num in range(8):
        penup()
        forward(10)
        pendown()
        forward(10)
    penup()
    backward(160)
    left(90)
    forward(20)

# Create the first player's turtle
player_1 = Turtle()
player_1.color('red')
player_1.shape('turtle')

# Position the first player's turtle at the starting line
player_1.penup()
player_1.goto(-160, 100)
player_1.pendown()

# Make the first player's turtle turn 360 degrees
for turn in range(10):
    player_1.right(36)

# Create the second player's turtle
player_2 = Turtle()
player_2.color('blue')
player_2.shape('turtle')

# Position the second player's turtle at the starting line
player_2.penup()
player_2.goto(-160, 70)
player_2.pendown()

# Make the second player's turtle turn 360 degrees
for turn in range(72):
    player_2.left(5)

# Create the third player's turtle
player_3 = Turtle()
player_3.shape('turtle')
player_3.color('green')

# Position the third player's turtle at the starting line
player_3.penup()
player_3.goto(-160, 40)
player_3.pendown()

# Make the third player's turtle turn 360 degrees
for turn in range(60):
    player_3.right(6)

# Create the fourth player's turtle
player_4 = Turtle()
player_4.shape('turtle')
player_4.color('orange')

# Position the fourth player's turtle at the starting line
player_4.penup()
player_4.goto(-160, 10)
player_4.pendown()

# Make the fourth player's turtle turn 360 degrees
for turn in range(30):
    player_4.left(12)

# Make the turtles run at random speeds for a number of turns
for turn in range(100):
    player_1.forward(randint(1, 5))
    player_2.forward(randint(1, 5))
    player_3.forward(randint(1, 5))
    player_4.forward(randint(1, 5))
