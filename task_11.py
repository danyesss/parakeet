import turtle
import time
import math

turtle.speed(0)
turtle.shape('turtle')
#n =int(input())
r = 30
n = 80
def circ (n, r):
	for i in range(int(n/2)):
		turtle.forward(2*math.pi*r/n)
		turtle.right(360/n)
num = 4
a = 40
circ(n, r)	
for i in range(num-1):
	circ(n/4, r/4) 
	circ(n, r)	
time.sleep(3)	