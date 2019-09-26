import turtle
import time

turtle.speed(0)
turtle.shape('turtle')
#n =int(input())
n = 10
q = 10
a = 30
for i in range(n):
	for j in range(4):
		turtle.forward(2*i*q + a)
		turtle.left(90)
	turtle.right(90)
	turtle.penup()
	turtle.forward(q)
	turtle.left(90)
	turtle.backward(q)
	turtle.pendown()
time.sleep(4)	