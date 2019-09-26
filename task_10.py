import turtle
import time
import math

turtle.speed(0)
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
num = 20
a = 100
for i in range(num):
	circ(100, r+a*i/num, 0)
	circ(100, r+a*i/num, 1)
time.sleep(4)	