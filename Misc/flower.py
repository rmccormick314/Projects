import math
import turtle

tur = turtle.Turtle()
tur.penup()
turtle.bgcolor("black")
tur.pencolor("blue")

t = 0

while t < 50:
    x = math.cos(t) * t
    y = math.sin(t) * t
    tur.goto(x, y)
    tur.pendown()
    tur.goto(0,0)
    tur.penup()
    t += 1

t = 0
tur.pencolor("purple")
while t < 50:
    x = math.cos(t) * math.exp(t*0.07)
    y = math.sin(t) * math.exp(t*0.05)
    tur.pendown()
    tur.goto(x, y)
    t += 0.2
    
