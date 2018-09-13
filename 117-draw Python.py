#e2.1Drawpython.py
import turtle
turtle.setup(650,350,150,150)
turtle.penup()
turtle.fd(-250)
turtle.pendown()
turtle.pensize(20)
turtle.pencolor("pink")
turtle.seth(-40)
for i in range(4):
    turtle.pencolor("grey")
    turtle.circle(40,80)
    turtle.pencolor("pink")
    turtle.circle(-40,80)
turtle.pencolor("grey")
turtle.circle(40,80/2)
turtle.fd(40)
turtle.pencolor("pink")
turtle.circle(16,180)
turtle.fd(40*2/3)
    
