import pygame,sys
from triangleMaths import *

BLACK = (0,0,0)
WIDTH,HEIGHT = 800,800
WINDOW = pygame.display.set_mode((WIDTH,HEIGHT))
clock = pygame.time.Clock()

def update(triangle):
	WINDOW.fill(BLACK)
	triangle.run()
	triangle.draw(WINDOW)
	pygame.display.update()

def main():
	triangle = Triangle(WIDTH,HEIGHT)
	while True:
		#clock.tick(60)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()

		update(triangle)

if __name__ == "__main__":
	main()