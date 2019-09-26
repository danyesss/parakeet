import turtle
import time
import math

turtle.speed(1000)
turtle.shape('turtle')
#n =int(input())
r = 30
def circ (num, r, d):
	n = num
	for i in range(n):
		turtle.forward(2*math.pi*r/n)
		if d == 0:
			turtle.left(360/n)
		else:
			turtle.right(360/n)

for i in range(3):
	circ(100, r, 0)
	circ(100, r, 1)
	turtle.left(360/3)
time.sleep(4)	