import pygame

class complex:

    def __init__(self, r, i):
        self.r = r
        self.i = i
        
    def __add__(self, other):
        if type(other) != complex:
            return complex(self.r + other, self.i)
        return complex(self.r + other.r, self.i + other.i)
    
    def __sub__(self, other):
        if type(other) != complex:
            return complex(self.r - other, self.i)
        return complex(self.r - other.r, self.i - other.i)
    
    def __mul__(self, other):
        if type(other) != complex:
            return complex(self.r * other, self.i * other)
        return complex(self.r * other.r - self.i * other.i, (self.r * other.i) + (self.i * other.r))

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
    
    def __str__(self):
        if self.i < 0:
            return "(" +str(self.r)+str(self.i)+"i)"
        else:
            return "(" +str(self.r)+"+"+str(self.i)+"i)"
    
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
        for p in self.points:
            p.apply(function, numFrames)
        for f in range(numFrames):
            self.screen.fill((0,0,0))
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
        done = False
        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
            self.clock.tick(30)

    def addSquare(self, radius):
        i = -radius
        while i < radius + 0.1:
            self.points.append(point(complex(radius, i)))
            self.points.append(point(complex(-radius, i)))
            self.points.append(point(complex(i, radius)))
            self.points.append(point(complex(i, -radius)))
            i += 0.2

def y(x):
    return complex(x.i, x.r) / x

g = grid((25,25),25,complex)

g.points = []
for i in range(6):
    g.addSquare(i)



g.animate(y, time = 5, framerate = 30, radius = 0.5)