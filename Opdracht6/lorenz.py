import numpy
from scipy import integrate

class Lorenz:
    
    def __init__(self, in_state, sigma=10, rho=28, beta=8/3):
        self.in_state = in_state
        self.sigma = sigma
        self.rho = rho
        self.beta = beta
        
    def f(self, y, t):
        y=[y[0],y[1],y[2]]
        return self.sigma*(y[1]-y[0]),y[0]*(self.rho-y[2])-y[1],y[0]*y[1]-self.beta*y[2]
        
    def solve(self, T, dt):
        tijdstippen = []
        t = 0
        while t <= T:
            tijdstippen.append(t)
            t += dt
        return integrate.odeint(self.f,self.in_state,tijdstippen)
