import turtle
col=[ "red","blue","green","orange","yellow","purple"]
t=turtle.Turtle()
screen=turtle.Screen()
screen.bgcolor('black')
t.speed(500)
for i in range(200):
        t.color(col[i%6])
        t.forward(i*1.5)
        t.left(59)
        t.width(3)
turtle.exitonclick()
