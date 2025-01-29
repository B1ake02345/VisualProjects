from multiprocessing import current_process
import pygame
pygame.font.init()
import sys
import math
import random
import globals
globals.initialise()

WIDTH, HEIGHT = 1366, 766
window = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
FONT = pygame.font.SysFont("comicsans",20)
colours = ([216,191,216],[221,160,221],[238,130,238],[218,112,214],[255,0,255],[186,85,211],[147,112,219],[138,43,226],[148,0,211],[153,50,204],[139,0,139],[128,0,128],[75,0,130])
#colours = ([21,52,80],[41,64,82],[68,114,148],[143,188,219],[244,214,188],[248,228,204])
#colours = ([242,194,203],[217,132,155],[191,122,160],[242,208,167],[242,203,189])
current_colour = random.choice(colours)
next_colour = random.choice(colours)

class Button:
        def __init__(self,x,y,width,height,image):
                self.pos = [x,y]
                self.image = pygame.transform.scale(pygame.image.load(image),(width,height))
                self.rect = self.image.get_rect(center=self.pos)

        def check_clicked(self,mx,my,clicked):
                if self.rect.collidepoint(mx,my) and clicked:
                        return 1

                window.blit(self.image,self.rect)

class Point:
        def __init__(self,start_t):
                self.t1 = start_t
                self.t2 = start_t-math.pi
                self.pnt1 = get_coords(self.t1)
                self.pnt2 = get_coords(self.t2)
        def next_point(self):
                self.t1 += math.pi/2048
                self.t2 -= math.pi/2048
                self.pnt1 = get_coords(self.t1)
                self.pnt2 = get_coords(self.t2)
        def draw(self,colour):
                self.next_point()
                pygame.draw.rect(window,(255,255,255),pygame.Rect(self.pnt1,(2,2)))
                pygame.draw.rect(window,(255,255,255),pygame.Rect(self.pnt2,(2,2)))
                pygame.draw.line(window,tuple(colour),self.pnt1,self.pnt2)

def get_coords(t):
        return (683*math.cos(globals.multipliers[0]*t)+683,384*math.sin(globals.multipliers[1]*t)*math.cos(globals.multipliers[2]*t)+384)
        #return (683+683*(1/100*(math.cos(globals.multipliers[0]*t))**9*(math.cos(5*t))**10+1/4*math.sin(2*t)*(1-1/2*(math.sin(10*t))**2)*(1-(math.cos(globals.multipliers[1]*t)*math.cos(3*t))**8)),
        #        384+384*(math.sin(globals.multipliers[2]*t)*(1-1/5*(math.sin(10*t))**2*(1/2+(math.sin(2*t))**2))))

def change_colour():
        global next_colour
        current_index = 0
        completed = False
        for i in range(3):
                if current_colour[i] < next_colour[i]:
                        current_colour[i] += 1
                        completed=False
                elif current_colour[i] > next_colour[i]:
                        current_colour[i] -= 1
                        completed=False
                else:
                        completed=True

        if completed:
                next_colour = random.choice(colours)

def editors():
        global points
        mx,my = pygame.mouse.get_pos()
        clicked = pygame.mouse.get_pressed()[0]
        for i in range(3):
                add_btn = Button(400+(i-1)*250,700,44,44,"sprites/add_btn.png")
                m = FONT.render(f"multiplier {str(i)}",1,(255,255,255))
                m_rect = m.get_rect(center=(480+(i-1)*250,1000))
                sub_btn = Button(560+(i-1)*250,700,44,44,"sprites/sub_btn.png")
                if add_btn.check_clicked(mx,my,clicked) == 1:
                        globals.multipliers[i] += 1

                if sub_btn.check_clicked(mx,my,clicked) == 1:
                        globals.multipliers[i] -= 1

                window.blit(m,m_rect)

        add_btn = Button(900,700,44,44,"sprites/add_btn.png")
        l = FONT.render("lines",1,(255,255,255))
        l_rect = l.get_rect(center=(980,700))
        sub_btn = Button(1060,700,44,44,"sprites/sub_btn.png")
        if add_btn.check_clicked(mx,my,clicked) == 1:
                points.append(Point(points[-1].t1+globals.distance))
                globals.lines += 1
        if sub_btn.check_clicked(mx,my,clicked) == 1:
                points.pop()
                globals.lines -= 1

        window.blit(l,l_rect)

        add_btn = Button(1200,700,44,44,"sprites/add_btn.png")
        d = FONT.render("distance",1,(255,255,255))
        d_rect = d.get_rect(center=(1280,700))
        sub_btn = Button(1360,700,44,44,"sprites/sub_btn.png")
        if add_btn.check_clicked(mx,my,clicked) == 1:
                globals.distance += 0.0001
                points = [Point(i*globals.distance) for i in range(globals.lines)]
        if sub_btn.check_clicked(mx,my,clicked) == 1:
                globals.distance -= 0.0001
                points = [Point(i*globals.distance) for i in range(globals.lines)]

        window.blit(d,d_rect)

        

points = [Point(i*globals.distance) for i in range(globals.lines)]

def main():
        hidden = False
        while 1:
                clock.tick(60)
                for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                                pygame.quit()
                                sys.exit()
                        if event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_SPACE:
                                        hidden = not hidden

                window.fill((0,0,0))
                change_colour()
                if not hidden:
                        editors()
                
                for p in points:
                        p.draw(current_colour)
                        
                pygame.display.update()

if __name__ == "__main__":
    main()
