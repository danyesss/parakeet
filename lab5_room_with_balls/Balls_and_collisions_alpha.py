from tkinter import *
from random import randrange as rnd, choice

import time
import numpy as np
root = Tk()
X_max = 800
Y_max = 800
V_max = min(X_max, Y_max)/8
R_max = min(X_max, Y_max)/10
k = 1000000
k0 = k * 100000
N = 15
canv = Canvas(root,width=X_max, height=Y_max,bg='white')
canv.pack(fill=BOTH,expand=1)
#
colors = ['red','orange','yellow','green','blue']
#
class Coor:
	def __init__(self, x=0, y=0):
		self.x = x
		self.y = y
	def __mul__(self, c):
		return Coor(self.x * c,  self.y * c)
	def __add__(self, point):
		return Coor(self.x + point.x, self.y + point.y)    
	def show(self):
		print("[%s; %s]" % (self.x, self.y))
        
class Ball:
	global X_max, Y_max, R_max, k, k0
	def __init__(self):
		self.r = rnd(30,50)
		[Rx, Ry] = [rnd(R_max,X_max-R_max),rnd(R_max,Y_max-R_max)]
		self.R = Coor(Rx, Ry)
		[vx, vy] = [10*(rnd(int(V_max))-V_max/2),10*(rnd(int(V_max))-V_max/2)]
		self.v = Coor(vx, vy)
		[ax, ay] = [0, 0]
		self.a = Coor(ax, ay)
		self.a_coll = Coor()
		self.a_guk = Coor()
		self.clr = choice(colors);
		self.circ = canv.create_oval(self.R.x-self.r,self.R.y-self.r,self.R.x+self.r,self.R.y+self.r,fill = self.clr , width=0)
		root.after(int(50),update)
	def flying(self, dt=0.2):
		self.a = self.a_guk + self.a_coll
		dv = self.a * dt
		self.v = self.v + dv			
		dR = self.v * dt
		self.R = self.R + dR			
		canv.delete(self.circ)
		self.circ = canv.create_oval(self.R.x-self.r,self.R.y-self.r,self.R.x+self.r,self.R.y+self.r,fill = self.clr , width=0)
	def wall(self, dt=0.2):
		x = self.R.x
		y = self.R.y		
		a_guk = Coor()
		if abs(x-X_max/2)> X_max/2 - self.r:
			a_guk = a_guk + Coor(np.sign(-X_max/2+x)*k*(X_max/2 - self.r - abs(X_max/2-x)), 0)
		if abs(y-Y_max/2)> Y_max/2 -self.r:
			a_guk = a_guk + Coor(0, np.sign(-Y_max/2+y)*k*(Y_max/2 - self.r - abs(Y_max/2-y)))
		self.a_guk = a_guk
	def collision(self, j, dt=0.2):
		x = self.R.x
		y = self.R.y
		bll = ball[j]
		xj = bll.R.x
		yj = bll.R.y	
		dx = x - xj
		dy = y - yj
		rij = np.sqrt(dx**2 + dy**2)
		a_coll = Coor()
		if rij <= self.r + bll.r:
			F = k0*(self.r + bll.r - rij)/(self.r + bll.r)/(self.r**2)
			n = Coor(dx/rij, dy/rij)
			a_coll = n * F
		self.a_coll = self.a_coll + a_coll
def update():
	dt = 0.002/N
	for i in range(N):
		ball[i].flying(dt)
	
	for i in range(N):	
		ball[i].wall(dt)
		ball[i].a_coll = Coor()
		for j in range(N):
			if i != j:
				ball[i].collision(j, dt)
	root.after(11*N, update)
ball = []
for i in range(N):
	ball.append(Ball())	
root.after(1, update)
mainloop()