import turtle
from math import gcd

# cote = int(input("Nombre de cotes? "))

# for i in range(cote):
#    turtle.forward(100)
#    turtle.left(360/cote)
# turtle.done

b = int(input("Nombre de branches? "))
inc = (b - 1) // 2

while gcd(b, inc) > 1:
    inc = inc - 1
if inc == 1:
    print("Impossible de dessiner une etoile a", b, "branches en une seule fois")
else:
    angle = 180 - (b - 2 * inc) * 180 / b
    for i in range(b):
        turtle.forward(100)
        turtle.left(angle)
    turtle.done
