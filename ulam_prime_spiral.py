'''
Ulam Spiral of Prime numbers. Here a spiral is formed with the prime numbers. 
'N' is the total number of natural numbers below which the prime numbers are highlighted.
programmed by Sayantan Biswas 
'''

# Importing the Turtle graphics library
import turtle as t

# Function to check if a number is prime
def prime_check(a):
    if a == 1:
        return False  # Not prime
    else:
        for j in range(2, a+1):
            if a % j == 0:
                break

        if j < a:
            return False  # Not prime 
        else:
            return True  # Prime

# Initializing the Turtle
pen = t.Turtle()

i = 1
N = 1000  # Total number of natural numbers 
num = 0

# Setting up the Turtle graphics
t.bgcolor("Black")
pen.color("White")
t.speed(200)

# Loop to generate Ulam Spiral
while num <= N:
    # Moving right and highlighting prime numbers
    for j in range(i):
        pen.penup()
        num = num + 1
        if prime_check(num) == True:
            pen.dot()  # Place a dot for prime numbers
        if num > N:
            break
        pen.forward(10)

    pen.left(90)

    # Moving up and highlighting prime numbers
    for k in range(i):
        pen.penup()
        num = num + 1
        if prime_check(num) == True:
            pen.dot()  # Place a dot for prime numbers
        if num > N:
            break
        pen.forward(10)

    pen.left(90)

    i = i + 1

# Hiding the Turtle
pen.hideturtle()

# Completing the drawing
t.done()
