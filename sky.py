import turtle
import time
import random 
t=turtle.Turtle()
screen=turtle.Screen()
t.hideturtle()

screen.title("Night Sky")
screen.screensize(800,500,bg="black")
t.pencolor("springgreen")
#t.speed(1)
def make_star():
 for i in range(5):
     t.pendown()
     t.forward(15)
     #time.sleep(2)
     t.right(144)
screen.colormode(255)
while True:
        x=random.randint(-400,250)
        y=random.randint(-400,250)
        r=random.randint(0,255)
        b=random.randint(0,255)
        g=random.randint(0,255)
        t.pencolor(r,b,g)
        t.penup()
        t.goto(x,y)
        make_star()
turtle.done()
