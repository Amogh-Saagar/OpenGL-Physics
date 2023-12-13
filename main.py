from OpenGL.GLUT import *  
from OpenGL.GL import *  
from OpenGL.GLU import *
from math import pi, sin, cos
import numpy as np
from datetime import datetime
from objects import ball
global LastTime
LastTime = datetime.now()
global BallList
BallList = []
numberOfBalls = 50
for i in range(numberOfBalls):
    b = ball(1, np.random.rand(2)*300)
    BallList.append(b)
def Myinit():
    glClearColor(0.0, 0.0, 0.0, 1.0) #bg is black
    glPointSize(5.0) # point is 1 pixel
    glMatrixMode(GL_PROJECTION) 
    glLoadIdentity()
    gluOrtho2D(-780, 780, -420, 420)
    glutFullScreen()
	
def display():
    global LastTime
    dt = (datetime.now() - LastTime).total_seconds()
    if dt > 0.03:
        global BallList
        print(len(BallList))
        glClearColor(0.0, 0.0, 0.0, 1.0 )
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        LastTime = datetime.now()
        for i in BallList:
            tosend = BallList.copy()
            tosend.remove(i)
            i.calcpos(tosend, dt)
            i.draw()
            if i.dist() >1000:
                BallList.remove(i)
        glutSwapBuffers()

glutInit()
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
glutInitWindowSize(500, 500)
glutCreateWindow(b"OpenGL Window")
Myinit()
glutDisplayFunc(display)
glutIdleFunc(display)
glutMainLoop()
