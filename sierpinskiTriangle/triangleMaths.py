import random,pygame

WHITE = (255,255,255)

class Vector:
	def __init__(self,x,y):
		self.x = x
		self.y = y

	def multi(self,val):
		self.x*=val
		self.y*=val

	def div(self,val):
		self.x/=val
		self.x/=val

	def add(self,vector):
		self.x+=vector.x
		self.y+=vector.y

	def sub(self,vector):
		self.x-=vector.x
		self.y-=vector.y

	def set(self,x,y):
		self.x = x
		self.y = y

	def reverse_vector(self):
		self.x = -self.x
		self.y = -self.y

	def normalise(self):
		mag = self.get_magnitude()
		self.x,self.y = self.x/mag,self.y/mag

	def distance(self,vector):
		return ((self.x-vector.x)**2 + (self.y-vector.x)**2)**0.5

	def get_magnitude(self):
		return ((self.x)**2 + (self.y)**2)**0.5

class Point:
	def __init__(self,x,y):
		self.pos = Vector(x,y)
		self.width = 3
		self.height = 3

	def draw(self,window):
		rect = pygame.Rect(self.pos.x,self.pos.y,self.width,self.height)
		rect.center = (self.pos.x,self.pos.y)
		pygame.draw.ellipse(window,WHITE,rect)

class Triangle:
	def __init__(self,swidth,sheight):
		self.org_pnts = [Point(swidth/2,sheight/10),Point(swidth/6,sheight-sheight/10),Point(swidth-swidth/6,sheight-sheight/10)]
		self.pnts = []
		for pnt in self.org_pnts:
			self.pnts.append(pnt)

		self.current_pnt = random.choice(self.org_pnts)

	def run(self):
		new_rand_pnt = random.choice(self.org_pnts)
		distance = Vector(self.current_pnt.pos.x-new_rand_pnt.pos.x,self.current_pnt.pos.y-new_rand_pnt.pos.y)
		distance.multi(0.5)
		new_pnt = Point(self.current_pnt.pos.x - distance.x,self.current_pnt.pos.y - distance.y)
		self.current_pnt = new_pnt
		self.pnts.append(new_pnt)


	def draw(self,window):
		for pnt in self.pnts:
			pnt.draw(window)