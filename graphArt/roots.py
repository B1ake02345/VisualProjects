import pygame
import sys
import random
import math
import copy

WIDTH, HEIGHT = 500, 500
window = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
#colours = ([216,191,216],[221,160,221],[238,130,238],[218,112,214],[255,0,255],[186,85,211],[147,112,219],[138,43,226],[148,0,211],[153,50,204],[139,0,139],[128,0,128],[75,0,130])
colours = ([0,0,255],[0,0,236])
lines = []

def make_line(start):
        angle = math.radians(random.randint(35,145))
        speed = random.randint(15,20)
        next_point = [start[0]+speed*math.cos(angle),start[1]-speed*math.sin(angle)]
        lines.append({"coords":[start,next_point],"colour":random.choice(colours)})
        if len(lines)%50!=0:
                make_line(next_point)

def build():
        for i in range(25):
                start = [random.randint(240,260),500]
                make_line(start)

def profile_pic():
        for l in reversed(lines):
                for p in l["coords"]:
                        if ((p[0]-250)**2+(p[1]-250)**2)**0.5 > 125:
                                lines.remove(l)
                                break
                

def main():
        global lines
        build()
        #profile_pic()
        while 1:
                clock.tick(30)
                for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                                pygame.quit()
                                sys.exit()
                        if event.type == pygame.MOUSEBUTTONDOWN:
                                lines = []
                                build()
                                #profile_pic()

                window.fill((0,0,0))
                for l in lines:
                        pygame.draw.line(window,l["colour"],l["coords"][0],l["coords"][1])
                pygame.display.update()

        
if __name__ == "__main__":
        main()
