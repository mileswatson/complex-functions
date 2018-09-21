import pygame

class complex:

    def __init__(self, r, i):
        self.r = r
        self.i = i
        
    def __add__(self, other):
        if type(other) != complex:
            return complex(self.r + other, self.i)
        return complex(self.r + other.r, self.i + other.i)
    
    def __radd__(self, other):
        return complex(self.r + other, self.i)
    
    def __sub__(self, other):
        if type(other) != complex:
            return complex(self.r - other, self.i)
        return complex(self.r - other.r, self.i - other.i)
    
    def __rsub__(self, other):
        return complex(other - self.r, self.i)
    
    def __mul__(self, other):
        if type(other) != complex:
            return complex(self.r * other, self.i * other)
        return complex(self.r * other.r - self.i * other.i, (self.r * other.i) + (self.i * other.r))

    def __rmul__(self, other):
        return complex(self.r * other, self.i * other)

    def __truediv__(self, other):
        if type(other) != complex:
            if other == 0:
                other = 0.000001
            return complex(self.r / other, self.i / other)
        x = self * complex(other.r,-other.i)
        div = (other.r * other.r) + (other.i * other.i)
        if div == 0:
            div = 0.000001
        return complex(x.r/div, x.i/div)
    
    def __rtruediv__(self, other):
        return complex(other, 0) / self
    
    def __abs__(self):
        return complex((self.r**2 + self.i**2)**0.5,0)
    
    def __str__(self):
        if self.i < 0:
            return "(" +str(self.r)+str(self.i)+"i)"
        else:
            return "(" +str(self.r)+"+"+str(self.i)+"i)"
    
    def __int__(self):
        return int(self.r)
    
    def __float__(self):
        return float(self.r)
    
    def __lt__(self, other):
        if type(other) != complex:
            return (self.r**2 + self.i**2)**0.5 < other
        return (self.r**2 + self.i**2)**0.5 < (other.r**2 + other.i**2)**0.5
    
    def __le__(self, other):
        if type(other) != complex:
            return (self.r**2 + self.i**2)**0.5 <= other
        return (self.r**2 + self.i**2)**0.5 <= (other.r**2 + other.i**2)**0.5
    
    def __eq__(self, other):
        if type(other) != complex:
            other = complex(other, 0)
        return self.r == other.r and self.i == other.i
    
    def __ne__(self, other):
        if type(other) != complex:
            other = complex(other, 0)
        return self.r != other.r or self.i != other.i
    
    def __ge__(self, other):
        if type(other) != complex:
            return (self.r**2 + self.i**2)**0.5 >= other
        return (self.r**2 + self.i**2)**0.5 >= (other.r**2 + other.i**2)**0.5
    
    def __gt__(self, other):
        if type(other) != complex:
            return (self.r**2 + self.i**2)**0.5 < other
        return (self.r**2 + self.i**2)**0.5 < (other.r**2 + other.i**2)**0.5
    
    def get(self):
        return (self.r, self.i)

class point:

    def __init__(self, pos):
        self.domain = pos
        self.range = pos
        self.interval = self.domain - self.range
    
    def __str__(self):
        return str(self.domain) + "->" + str(self.range)
    
    def apply(self, function, numFrames):
        self.range = function(self.domain)
        if type(self.range) != complex:
            self.range = complex(self.range, 0)
        self.interval = (self.range - self.domain) / numFrames
    
    def move(self):
        self.domain = self.domain + self.interval

class grid:

    def __init__(self, size, scale, obj):
        self.scale = scale
        self.size = (size[0]*scale,size[1]*scale)
        self.centre = (size[0]//2,size[1]//2)
        self.points = []
        for x in range(size[0]):
            for y in range(size[1]):
                self.points.append(point(obj(x-self.centre[0],y-self.centre[1])))
        self.centre = (self.centre[0]*scale+10,self.centre[1]*scale+10)
        pygame.init()
        self.screen = pygame.display.set_mode(self.size)
        self.clock = pygame.time.Clock()

    def animate(self, function, time = 1, framerate = 30, radius = 1):
        numFrames = time * framerate
        done = False
        for p in self.points:
            p.apply(function, numFrames)
        f = 0
        while f < numFrames and not done:
            self.screen.fill((0,0,0))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
            pygame.draw.line(self.screen,(128,128,128),(0,self.centre[1]),(self.size[0],self.centre[1]))
            pygame.draw.line(self.screen,(128,128,128),(self.centre[0],0),(self.centre[0],self.size[1]))
            for p in self.points:
                p.move()
                pos = p.domain.get()
                pos = (round(pos[0]*self.scale)+self.centre[0],self.centre[1]-round(pos[1]*self.scale))
                pygame.draw.circle(self.screen,(75, 150, 255),pos,2)
            pygame.display.flip()
            self.clock.tick(framerate)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    break
            #print(f)
            f += 1
        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
            self.clock.tick(30)
        
    def __repr__(self):
        return "complex({self.r}, {self.i})"

    def addSquare(self, radius):
        i = -radius
        while i < radius + 0.1:
            self.points.append(point(complex(radius, i)))
            self.points.append(point(complex(-radius, i)))
            self.points.append(point(complex(i, radius)))
            self.points.append(point(complex(i, -radius)))
            i += 0.2

g = grid((13,13),50,complex)

g.points = []
for i in range(5):
    g.addSquare(i)

i = complex(0,1)



def f(z):
    return z / complex(z.i, z.r)

g.animate(f, time = 5, framerate = 30, radius = 1)