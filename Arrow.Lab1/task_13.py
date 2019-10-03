import turtle
import time
import math

turtle.speed(0)
turtle.shape('turtle')

num = 50
a = 600
for i in range(num*2):
	turtle.forward(a)
	turtle.left(180 - 180/num)
time.sleep(4)	