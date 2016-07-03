import turtle

def draw_square():
    window = turtle.Screen()
    window.bgcolor("red")
    
    hare = turtle.Turtle()
    hare.shape("turtle")
    hare.color("white")
    hare.speed(2)
    hare.forward(100)
    hare.right(90)
    hare.forward(100)
    hare.right(90)
    hare.forward(100)
    hare.right(90)
    hare.forward(100)
    hare.right(90)
    window.exitonclick()
    
    
    
draw_square()