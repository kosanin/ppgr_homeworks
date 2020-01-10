from OpenGL.GLUT import *
from OpenGL.GL import *
from OpenGL.GLU import *
import draw
import math
import reconstruction

points = []
alpha = 0
beta = 0
r = 700

def init():
    global points
    glClearColor(0.7, 0.7, 0.7, 0)
    glEnable(GL_DEPTH_TEST)
    glLineWidth(2)

    local_points = reconstruction.read_two_camera_points("init_tacke.txt")
    k1 = list(map(lambda x : x[0], local_points.values()))
    k2 = list(map(lambda x : x[1], local_points.values()))
    f = reconstruction.fundamental_matrix(k1, k2)

    local_points = reconstruction.read_two_camera_points("slika1_input_points.txt")
    points = reconstruction.triangulation(local_points, f)
    for p in points:
        p[2] = 200
    



def on_keyboard(key, x, y):
    global alpha, beta
    if key == b'\x1b':
        sys.exit()
    elif key == b'd':
        alpha += 0.03
        glutPostRedisplay()
    elif key == b'a':
        alpha -= 0.03
        glutPostRedisplay()
    elif key == b'w':
        beta += 0.03
        glutPostRedisplay()
    elif key == b's':
        beta -= 0.03
        glutPostRedisplay()

def on_display():
    global points
    global r, alpha, beta
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    
    glLoadIdentity()
    gluLookAt(
            r * math.sin(alpha) * math.cos(beta), 
            r * math.sin(alpha) * math.sin(beta), 
            r * math.cos(alpha),
        0, 0, 0,
        0, 1, 0)

    draw.coordinate_axes(1000)
    glTranslatef(-491, -1, 0)    
    draw.reconstructed_cubes(points)
    glutSwapBuffers()


def on_reshape(w, h):
    glViewport(0, 0, w, h)

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(60, w / float(h), 1, 1000)
    glMatrixMode(GL_MODELVIEW)


def set_callbacks():
    glutDisplayFunc(on_display)
    glutKeyboardFunc(on_keyboard)
    glutReshapeFunc(on_reshape)


def main():
    
    glutInit()
    glutInitDisplayMode(GLUT_RGB|GLUT_DEPTH|GLUT_DOUBLE)
    glutInitWindowSize(600, 600)
    glutCreateWindow("3D rekonstrukcija")

    init()
    set_callbacks()


    glutMainLoop()

if __name__ == "__main__":
    main()
