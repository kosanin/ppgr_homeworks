from OpenGL.GLUT import *
from OpenGL.GL import *
from OpenGL.GLU import *
import draw
import math
import numpy as np
import reconstruction

points = []
alpha = 0
beta = 0
r = 500
centroid = []


def init():
    global points, centroid
    glClearColor(0.7, 0.7, 0.7, 0)
    glEnable(GL_DEPTH_TEST)
    glLineWidth(3)

    # racunanje fundamentalne matrice
    local_points = reconstruction.read_two_camera_points("data/init_tacke_slika2.txt")
    k1 = list(map(lambda x : x[0], local_points.values()))
    k2 = list(map(lambda x : x[1], local_points.values()))
    f = reconstruction.fundamental_matrix(k1, k2)
    f1 = reconstruction.normalized_fundamental_matrix(f)

    # rekonstrukcija 3D koordinata
    local_points = reconstruction.read_two_camera_points("data/test.txt")
    points = reconstruction.triangulation(local_points, f1)

    # z koordinata je znatno manja od ostalih, pa je skaliramo za 400
    for p in points:
        p[2] *= 400

    # with open("rekonstruisane_koordinate.txt", "w+") as f:
    #     id = 1
    #     for p in points:
    #         f.write('%d %s\n' % (id, p))
    #         id += 1

    # dobijeni objekat transliramo za -centroid
    centroid = np.mean(points, axis=0)


def on_keyboard(key, x, y):
    global alpha, beta, r
    if key == b'\x1b':
        sys.exit()
    elif key == b'd':
        alpha += 0.03
        glutPostRedisplay()
    elif key == b'a':
        alpha -= 0.03
        glutPostRedisplay()
    elif key == b'w':
        r -= 4
        glutPostRedisplay()
    elif key == b's':
        r += 4
        glutPostRedisplay()

def on_display():
    global points
    global r, alpha, beta
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    
    glLoadIdentity()
    gluLookAt(
            r * math.cos(alpha), 
            r, 
            r * math.sin(alpha),
        0, 0, 0,
        0, 1, 0)

    glTranslatef(-centroid[0], -centroid[1], -centroid[2])
    glRotatef(180, 1, 1, 1)
    draw.slika2_reconstructed_cubes(points)

    glutSwapBuffers()

def on_reshape(w, h):
    glViewport(0, 0, w, h)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(60, w / float(h), 1, 2000)
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
