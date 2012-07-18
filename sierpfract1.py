import pygame
import math
black = (0,0,0)
screen = pygame.display.set_mode((1000,1000))
screen.fill(black)
angle = 0
#global angle
#def centerscreen(wt=500,ht=500):
#	x = (wt/2)
#	y = (ht/2)
#	return (x,y)
#centrx = 650/2
#centry = 650/2
#def init_angle(angle):
#	global angle
#	return (angle)
	
#def coordinates(centrx,centry):
	#global centrx
	#global centry
x1 = 500/2
y1 = 500/2
#	start = x1 , y1
x2 = x1 + 300

y2 = y1 + 300
#	end = x2, y2
a = (x1,y1)
b = (x2,y2)
	#return (a,b)
def midpoint(a,b):
	x = (a[0] + b[0])/2.0
	y = (a[1] + b[1])/2.0
	return (x,y)
def tri(screen,color,a,b,c):
	pygame.draw.polygon(screen,color,(a,b,c),0)
def sierp(screen,color,a,b,c,deep):
	
	if(deep <= 0):
		tri(screen,color,a,b,c)
	else:
		ab = midpoint(a,b)
		ac = midpoint(a,c)
		bc = midpoint(b,c)
		
		sierp(screen,color,a,ab,ac,deep-1)
		sierp(screen,color,b,ab,bc,deep-1)
		sierp(screen,color,c,ac,bc,deep-1)

def main():
	wt = 650
	ht = 650
	pygame.init()
#	black = pygame.Color(0,0,0)
#	screen = pygame.display.set_mode((wt,ht))
#	screen.fill(black)
	global a
	global b
	white = (255,255,255)
	#centrx = 650/2
	#centry = 650/2
	#coordinates(centrx,centry)
	sierp(screen,white,a,b,(150,300),3)
	pygame.display.update()
	wait = raw_input("press any key to quit...")
	pygame.quit()

main()		
