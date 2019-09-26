import turtle
import time
import math

turtle.speed(0)
turtle.shape('turtle')
#n =int(input())
def polygon (num, r):
	a = 2*r/math.tan((90 - 180/num)/180*math.pi)
	for i in range(num):
		turtle.forward(a)
		turtle.left(360/num)
	turtle.right(360/num)
r =  20
N = 20
#turtle.forward(50)
for i in range(N):
	polygon(i+3, r)
	d_r = r/30
	r = r/math.sin((90 - 180/(i+3))/180*math.pi) + d_r
	turtle.penup()
	turtle.right(90 - 180/(i+3))
	turtle.forward(r/math.sin((90 - 180/(i+4))/180*math.pi) - (r-d_r))
	turtle.left(90 + 180/(i+4))
	turtle.pendown()

time.sleep(4)