import turtle
import random
import time
from turtle import Turtle

#Screen
screen = turtle.Screen()
screen.title("CatchTheTurtle")
screen.bgpic("Adsız.gif")
screen.addshape("giphy.gif")




#Variables

score = 0
TurtleTime = 15
turtle_list = []

ScreenHeight = screen.window_height() / 2

Score_y = ScreenHeight * 0.8
Timer_y = ScreenHeight * 0.7

grid_size = 15



#Score Table
score_turtle = turtle.Turtle()
score_turtle.hideturtle()
score_turtle.penup()
score_turtle.setpos(0, Score_y)
score_turtle.write(" Score = ", move=False, align="center", font=("Verdana", 20, "normal"))


x_coordinates = [-20 ,-10 , 0 ,10 ,20]
y_coordinates = [-20, -15, -10, -5, 0]




time_turtle = turtle.Turtle()
time_turtle.hideturtle()
time_turtle.penup()
time_turtle.setpos(0, Timer_y)
time_turtle.write(f" Time =  {TurtleTime}", move=False, align="center", font=("Verdana", 20, "normal"))

def mouse_click(x,y):
    global TurtleTime
    global score_turtle
    global score
    if TurtleTime > 0:
        score += 1
        score_turtle.clear()
        score_turtle.write(f" Score = {score} ", move=False, align="center", font=("Verdana", 20, "normal"))
    else:
        score_turtle.write(" ", move=False, align="center", font=("Verdana", 20, "normal"))

def main_turtle_setup(x, y):



   t = turtle.Turtle()
   t.penup()
   t.shape("turtle")
   t.shapesize(2,2)
   t.color("green")
   t.setpos(x * grid_size,y * grid_size)
   turtle_list.append(t)
   t.onclick(mouse_click)

def turtle_position():
    for x in x_coordinates:
        for y in y_coordinates:
            main_turtle_setup(x,y)

def hide_turtles():
    for t in turtle_list:
        t.hideturtle()

def show_turtles():
    if TurtleTime > 0:
        hide_turtles()
        global n
        n = random.choice(turtle_list)
        n.showturtle()
        screen.ontimer(show_turtles, 500)
    elif score > 5:
        score_turtle.clear()
        hide_turtles()
        score_turtle.write("Kazandınız Tebrikler ! ", move=False, align="center", font=("Verdana", 20, "normal"))
    else:
        score_turtle.clear()
        hide_turtles()
        score_turtle.write(" Kaybettiniz ", move=False, align="center", font=("Verdana", 20, "normal"))



def timer():
    global TurtleTime
    if TurtleTime > 0:
        TurtleTime -= 1
        time_turtle.clear()
        time_turtle.write(f" Time =  {TurtleTime}", move=False, align="center", font=("Verdana", 20, "normal"))
        screen.ontimer(timer, 1000)
    else:
        time_turtle.clear()
        time_turtle.write(f"Süre Bitti", move=False, align="center", font=("Verdana", 20, "normal"))











turtle.tracer(0)
turtle_position()
show_turtles()
timer()
turtle.tracer(1)





turtle.mainloop()