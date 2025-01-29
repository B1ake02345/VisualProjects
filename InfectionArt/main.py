import pygame
import sys
import random

grid_size = [50,50]
swidth,sheight = 500,500
cell_size = [swidth/grid_size[0],sheight/grid_size[1]]
window = pygame.display.set_mode((swidth,sheight))
clock = pygame.time.Clock()

game_ticks = 1
point = [random.randint(0,grid_size[1]-1),random.randint(0,grid_size[0]-1)]

grid = []
waitfors = []

class WaitFor:
    def __init__(self,duration,function):
        self.duration = duration
        self.function = function
        self.initiated_tick = game_ticks
    
    def update(self):
        if game_ticks-self.initiated_tick>=self.duration:
            self.function()
            return -1

class Cell:
    def __init__(self,x,y):
        self.position = [x,y]
        self.infected = False
        self.contagious = False

    def infect(self):
        self.infected = True
        waitfors.append(WaitFor(1,self.set_contagious_true))
        waitfors.append(WaitFor(3,self.set_contagious_false))

    def set_contagious_true(self):
        self.contagious = True

    def set_contagious_false(self):
        self.contagious = False

    def contaminate(self):
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        for direction in directions:
            try:
                cell = grid[self.position[0]+direction[0]][self.position[1]+direction[1]]
                if not cell.infected:
                    if random.random() < 0.7:
                        cell.infect()
                        cell.contagious = False
            except:
                pass

    def draw(self):
        if self.infected and not self.contagious:
            if random.random() > 0.995:
                colour = (187,80,152)
            else:
                colour = (122,81,151)
        elif self.infected:
            colour = (83,68,169)
        else:
            colour = (0,0,0)

        pygame.draw.rect(window,colour,pygame.Rect([self.position[0]*cell_size[0],self.position[1]*cell_size[1]],cell_size))

def generate_grid():
    for i in range(grid_size[1]):
        grid.append([])
        for j in range(grid_size[0]):
            grid[i].append(Cell(i,j))

def main():
    global game_ticks
    generate_grid()
    for i in range(20):
        grid[random.randint(0,grid_size[1]-1)][random.randint(0,grid_size[0]-1)].infect()

    while 1:
        clock.tick(12)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        for w in reversed(waitfors):
            if w.update() == -1:
                waitfors.remove(w)
                del w

        window.fill((0,0,0))
        for row in grid:
            for v in row:
                if v.contagious:
                    v.contaminate()

                v.draw()

        pygame.display.update()

        game_ticks += 1

if __name__ == "__main__":
    main()

