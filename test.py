import turtle
turtle.hideturtle()
turtle.right(45)
turtle.dot(10, 'red')
def arrow(size):
    for i in range (12):
        turtle.color('green')
        turtle.forward(size)
        turtle.dot(10, 'blue')
        turtle.right(10*i)
        turtle.goto(0,0)

turtle(arrow(400))

turtle.done()