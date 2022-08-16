import math
import turtle

tur = turtle.Turtle()

t = 0;
a = 1;

def draw_grid():
    tur.penup()
    tur.goto(-100, 0)
    tur.pendown()
    tur.goto(100, 0)
    tur.penup()
    tur.goto(0, 100)
    tur.pendown()
    tur.goto(0, -100)
    tur.penup()

draw_grid()

while t < (100):
    tur.pendown()
    
    x = math.cos(t) * t * a
    y = math.sin(t) * t * a
    
    tur.goto(x, y)
    print(str(x) + " " + str(y) + " " + str(t))
    
    t += 0.1
