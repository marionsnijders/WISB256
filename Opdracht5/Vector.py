class Vector:
    
    
    def __init__(self, n=0, m=0):
        if type(m) == float or type(m) == int:
            self.vector = [m] * n
        if type(m) == list:
            if n == len(m):
                self.vector = m
        
    def __str__(self):
        for i in range(0, len(self.vector)):
            self.vector[i] = str(self.vector[i])
        return '\n'.join(self.vector)
        
    def lincomb(self, other, alpha, beta):
        lijst = [0] * len(self.vector)
        for i in range(0, len(self.vector)):
            self.vector[i] = float(self.vector[i])
            other.vector[i] = float(other.vector[i])
            lijst[i] = alpha * self.vector[i] + beta * other.vector[i]
        a = Vector(len(self.vector), lijst)
        return a
        
    def scalar(self, alpha):
        lijst = [0] * len(self.vector)
        for i in range(0, len(self.vector)):
            lijst[i] = float(self.vector[i]) * alpha
        a = Vector(len(self.vector), lijst)
        return a
        
    def inner(self, other):
        som = 0
        for i in range(0, len(self.vector)):
            self.vector[i] = float(self.vector[i])
            other.vector[i] = float(other.vector[i])
            som = som + (self.vector[i] * other.vector[i])
        return som
        
    def norm(self):
        import math
        som = 0
        for i in range(0, len(self.vector)):
            self.vector[i] = float(self.vector[i])
            a = (self.vector[i])**2
            som = som + a
        return math.sqrt(som)
        
    