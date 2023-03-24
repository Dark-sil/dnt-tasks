import turtle
import random

turtle.setworldcoordinates(-2000,-2000,2000,2000)

def draw_football(x,y,tilt,radius):
    list1 = [0, 1, 2, 3,]
    color = ["red","green","blue","yellow"]
    turtle.up()
    turtle.goto(x,y)
    turtle.down()
    turtle.fillcolor(color[random.choice(list1)])
    turtle.begin_fill()
    turtle.seth(tilt-45)
    turtle.circle(radius,90)
    turtle.left(90)
    turtle.circle(radius,90)
    turtle.end_fill()
    
myWin = turtle.Screen()

for tilt in range(0,200,30): 
    draw_football(0,0,tilt,1000)

myWin.exitonclick()