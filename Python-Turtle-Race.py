
import turtle

##change shape to an arrow to look like turtle 
turtle.shape('turtle')
##speed can be zero to ten;
turtle.speed(0)
##turtle moving and not leaving a line behind
turtle.penup()
##move turtle to the right and up on x,y coordintors
turtle.goto(350,150)
##move turtle down
turtle.pendown()
turtle.goto(350,-150)
#make turtle disappear at the end
turtle.hideturtle()

## add more turtles
Ross = turtle.Turtle()
Lauren = turtle.Turtle()
Scout = turtle.Turtle()
##change shape from arrow to turtle
Ross.shape('turtle')
Lauren.shape('turtle')
Scout.shape('turtle')

#change colors of turtles from black
Ross.color("blue")
Lauren.color("green")
Scout.color("purple")

#turtles start to move to starting positions and remove lines
Ross.penup()
Lauren.penup()
Scout.penup()
Ross.goto(-350,100)
Lauren.goto(-350, - 100)
Scout.goto(-350, 0)

Ross.pendown()
Lauren.pendown()
Scout.pendown()

#turtles move to finish line on right
Ross.forward(700)
Lauren.forward(700)
Scout.forward (700)

turtle.done()