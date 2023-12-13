from OpenGL.GLUT import *  
from OpenGL.GL import *  
from OpenGL.GLU import *
from math import cos, sin, pi, sqrt
import numpy as np

class ball:
    def __init__(self, mass, pos):
        self.mass = mass
        self.pos = pos
        self.Gconstant = 10000
        self.BallGConstant = 100
        self.velocity = np.array([0.0, 0.0], dtype = float)
        self.gravity = self.Gconstant/sqrt(self.pos[0]**2 + self.pos[1]**2)
        self.acceleration = np.negative(self.pos/np.linalg.norm(self.pos) * self.gravity)

    def draw(self, res = 1):
        glColor3f(0.0, 0.0, 1.0)
        glBegin(GL_POINTS)
        glVertex2f(self.pos[0], self.pos[1])
        glEnd()
    
    def calcpos(self, bs, dt):
        self.gravity = self.Gconstant/sqrt(self.pos[0]**2 + self.pos[1]**2) #this is for the black hole in the middle
        self.acceleration = np.negative(self.pos/np.linalg.norm(self.pos) * self.gravity)
        for i in bs:
            self.gravity = self.BallGConstant/sqrt((i.position[0]-self.pos[0])**2 + (i.position[1]-self.pos[1])**2)# this is for the interparticular gravity
            self.acceleration += ((i.position-self.pos)/np.linalg.norm(i.position-self.pos) * self.gravity)
        self.velocity += self.acceleration*dt
        self.pos += self.velocity*dt
        
    
    def dist(self):
        return np.sqrt(self.pos.dot(self.pos))
    
    @property
    def position(self):
        return self.pos
    


        
