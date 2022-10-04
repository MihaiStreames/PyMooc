import turtle

angle = 60
colors = ["black", "blue", "red"]

for i in range(3):
    turtle.begin_fill()
    color = colors[i]
    turtle.color(color)
    for j in range(4):
        angle = 180 - angle
        turtle.forward(100)
        turtle.right(angle)
    turtle.left(120)
    turtle.end_fill()
turtle.done