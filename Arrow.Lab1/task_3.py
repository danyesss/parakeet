import turtle

turtle.speed(200)
turtle.shape('turtle')
n =int(input())
for i in range(n):
	turtle.forward(1000/n)
	turtle.left(360/n)