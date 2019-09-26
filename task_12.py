import turtle
import time
import math
#t = turtle.Turtle()
turtle.speed(0)
turtle.shape('turtle')
#n =int(input())
r = 40/math.pi
n = 80
def circ (n, r, shape):
	for i in range(int(n/shape)):
		turtle.forward(2*math.pi*r/n)
		turtle.left(360/n)

# shape = '2' - half of circle
# spape = '1' - circle
r = 200
n = 60
turtle.width(2)
turtle.fillcolor('#FFFACD')
turtle.begin_fill()
circ(n, r, 1)	
turtle.end_fill()

turtle.penup()
turtle.goto(-r/2, r/1.5)
turtle.pendown()
turtle.right(90)
turtle.width(10)
turtle.color('#CD853F')
circ(n, r/2, 2)	

turtle.color('#000000')
turtle.width(3)

turtle.penup()
turtle.goto(-r/1.5+r/6, 2*r - r/1.5)
turtle.pendown()
turtle.fillcolor('#FFFAFA')
turtle.begin_fill()
circ(n, r/6, 1)	
turtle.end_fill()


turtle.penup()
turtle.goto(+r/1.5+r/6, 2*r - r/1.5)
turtle.pendown()
turtle.fillcolor('#FFFAFA')
turtle.begin_fill()
circ(n, r/6, 1)	
turtle.end_fill()

turtle.penup()
turtle.goto(0, r)
turtle.pendown()
turtle.width(25)
turtle.color('#CD853F')
turtle.backward(r/2)

turtle.penup()
turtle.goto(0, -r)
turtle.pendown()

time.sleep(4)	
