import turtle

def draw_art():
    window = turtle.Screen()
    window.bgcolor("pink")

    angie = turtle.Turtle()
    angie.shape("turtle")
    angie.color("red")
    angie.speed(5)

    for i in range(0,36):
        angie.right(10)
        angie.circle(100)

    window.exitonclick()

draw_art()
