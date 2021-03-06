# sierpinski using any coordinates of screen

import pygame
black = (0,0,0)
screen = pygame.display.set_mode((1000,1000))
screen.fill(black)

def midpoint(x,y):
	midx = (x[0] + y[0])/2.0
	midy = (x[1] + y[1])/2.0
	return (midx,midy)
	#line_draw(screen,(x1,y1),(x2,y2))
#	centrx = x2
#	centry = y2
def tri(screen,red,x,y,z):
	red = (255,0,0)
	pygame.draw.polygon(screen,red,(x,y,z),0)

def sierp(screen,red,x,y,z,deep):

	if(deep <=0):
		tri(screen,red,x,y,z)
	else:
		a = midpoint(x,y)
		b = midpoint(x,z)
		c = midpoint(y,z)
		
		sierp(screen,red,x,a,b,deep-1)	
		sierp(screen,red,y,a,c,deep-1)
		sierp(screen,red,z,b,c,deep-1)
def main():
	wt = 1000
	ht = 1000
	pygame.init()
	white = (255,255,255) 
	sierp(screen,white,(300,50),(0,350),(600,350),3)

	pygame.display.update()
	wait = raw_input("press any key to quit...")
	pygame.quit()

main()		
