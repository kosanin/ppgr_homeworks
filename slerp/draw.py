from OpenGL.GL import *
from OpenGL.GLUT import glutWireOctahedron
import math

def coordinate_axes(size):
    glBegin(GL_LINES)
    glColor3f(1,0,0)
    glVertex3f(0,0,0)
    glVertex3f(size,0,0)
    
    glColor3f(0,1,0)
    glVertex3f(0,0,0)
    glVertex3f(0,size,0)
    
    glColor3f(0,0,1)
    glVertex3f(0,0,0)
    glVertex3f(0,0,size)
    glEnd()

def octahedron(center, p, phi):
    glPushMatrix()
    glTranslatef(center[0], center[1], center[2])
    glRotatef(phi * 180 / math.pi, p[0], p[1], p[2])
    glutWireOctahedron()
    coordinate_axes(2)
    glPopMatrix()