import turtle
import time

turtle.speed(0)
turtle.shape('turtle')
#n =int(input())
n = 15
m = 30
a = 10
b = 11
for i in range(n):
	for j in range(m):
		turtle.forward(a/m + (i*m + j)*(b - a)/m)
		turtle.left(360/m)
time.sleep(4)	