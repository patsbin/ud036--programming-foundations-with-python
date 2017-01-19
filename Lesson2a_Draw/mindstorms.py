import turtle

def draw_square():
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.shapesize(5,5,1)
    brad.color("yellow")
    brad.speed(2)

    for i in range(0,4):
        brad.forward(100)
        brad.right(90)

def draw_circle():
    angie = turtle.Turtle()
    angie.shape("arrow")
    angie.color("blue")
    angie.circle(100)


def draw_triangle():
    eddie = turtle.Turtle()
    eddie.color("green")

    for i in range(0,3):
        eddie.forward(150)
        eddie.right(120)


window = turtle.Screen()
window.bgcolor("red")

draw_square()
draw_circle()
draw_triangle()

window.exitonclick()
