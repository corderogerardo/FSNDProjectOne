import turtle

def draw_square(some_turtle) :
    for i in range(1,5):
        some_turtle.forward(20)
        some_turtle.right(30)

def draw_art() :
    window = turtle.Screen()
    window.bgcolor("red")
    gerardo = turtle.Turtle()
    gerardo.color("green")
    gerardo.shape("turtle")
    gerardo.speed(10)
    for i in range(1,37) :
        draw_square(gerardo)
        gerardo.right(10)
        gerardo.circle(100)

    #marie = turtle.Turtle()
    #marie.color("blue")
    #marie.shape("arrow")
    #marie.speed(1)
    #marie.circle(100)

    window.exitonclick()

draw_art()
