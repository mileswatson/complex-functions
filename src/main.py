
class complex:

    def __init__(self, r, i):
        self.r = r
        self.i = i

    def __add__(self, other):
        return complex(self.r + other.r, self.i + other.i)
    
    def __sub__(self, other):
        return complex(self.r - other.r, self.i - other.i)
    
    def __mul__(self, other):
        return complex(self.r * other.r - self.i * other.i, (self.r * other.i) + (self.i * other.r))

    def __truediv__(self, other):
        x = self * complex(other.r,-other.i)
        div = (other.r * other.r) + (other.i * other.i)
        return complex(x.r/div, x.i/div)
    
    def __str__(self):
        if self.i < 0:
            return "(" +str(self.r)+str(self.i)+"i)"
        else:
            return "(" +str(self.r)+"+"+str(self.i)+"i)"

class point:

    def __init__(self, obj):
        self.domain = obj
        self.range = obj
    
    def __str__(self):
        return str(self.domain) + "->" + str(self.range)
    
    def apply(self, function):
        self.range = function(self.domain)
    
    def reposition(self):
        self.domain = self.range

class grid:

    def __init__(self, size, obj):
        self.centre = (size[0]//2,size[1]//2)
        self.points = []
        for x in range(size[0]):
            for y in range(size[1]):
                self.points.append(point(obj(x-self.centre[0],y-self.centre[1])))
    
    def apply(self, function):
        for p in self.points:
            p.apply(function)


def function(p):
    return p * p + complex(1,0)

g = grid((5,3), complex)

g.apply(function)

for p in g.points:
    print(p)