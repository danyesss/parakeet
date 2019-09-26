import turtle
import time

turtle.speed(0)
turtle.shape('turtle')
#n =int(input())
n = 20
m = 4
a = 40
b = 48
for i in range(n):
	for j in range(m):
		turtle.forward(a/m + (i*m + j)*(b - a)/m)
		turtle.left(360/m)
time.sleep(4)	