import turtle
import time

turtle.speed(0)
turtle.shape('turtle')
#n =int(input())
n = 10
a = 50
for i in range(n):
	turtle.forward(a)
	turtle.stamp()
	turtle.backward(a)
	turtle.left(360/n)
turtle.shape('classic')
time.sleep(4)	