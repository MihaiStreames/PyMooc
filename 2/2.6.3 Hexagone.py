from math import pi, sin, cos
import turtle

# Calcul

long = float(input())

print(long * cos(0), long * sin(0))
print(long * cos(pi / 3), long * sin(pi / 3))
print(long * cos((2 * pi) / 3), long * sin(pi / 3))
print(long * cos((3 * pi) / 3), long * sin(0))
print(long * cos((-2 * pi) / 3), long * sin(-pi / 3))
print(long * cos((-1 * pi) / 3), long * sin(-pi / 3))

# exit()

# Dessin

turtle.begin_fill()
turtle.forward(100)
turtle.right(120)
turtle.forward(100)
turtle.right(60)
turtle.forward(100)
turtle.right(120)
turtle.forward(100)
turtle.end_fill()

turtle.begin_fill()
turtle.color("blue")
turtle.right(60)
turtle.forward(100)
turtle.left(120)
turtle.forward(100)
turtle.left(60)
turtle.forward(100)
turtle.left(120)
turtle.forward(100)
turtle.end_fill()

turtle.begin_fill()
turtle.color("red")
turtle.right(60)
turtle.forward(100)
turtle.right(120)
turtle.forward(100)
turtle.right(60)
turtle.forward(100)
turtle.right(120)
turtle.forward(100)
turtle.end_fill()

turtle.done()
