from OpenGL.GLUT import *
from OpenGL.GL import *
from OpenGL.GLU import *
import draw
from operator import add
import geometry
import numpy as np
import math

src_center = []
src_euler_angles = []
dest_center = []
dest_euler_angles = []

src_q = []
dest_q = []

t = 0
tm = 1

animation_ongoing = False
camera_param = 0

def string2floats(str):
    return list(map(float, str.split()))


def read_centers_angles_t(path):
    global src_center
    global dest_center
    global src_euler_angles
    global dest_euler_angles
    global tm
    with open(path, "r") as f:
        src_center = string2floats(f.readline())
        src_euler_angles = string2floats(f.readline())
        dest_center = string2floats(f.readline())
        dest_euler_angles = string2floats(f.readline())
        tm = string2floats(f.readline())[0]


def on_keyboard(key, x, y):
    global animation_ongoing, camera_param
    global t
    if key == b'\x1b':
        sys.exit()
    elif key == b'g':
        if not animation_ongoing:
            animation_ongoing = True
            glutTimerFunc(20, on_timer, 0)
    elif key == b's':
        animation_ongoing = False
    elif key == b'r':
        t = 0
        glutPostRedisplay()


def init():
    global src_q
    global dest_q
    glClearColor(0.7, 0.7, 0.7, 0)
    glEnable(GL_DEPTH_TEST)
    glLineWidth(2)
    read_centers_angles_t("data.txt")

    src_q = geometry.eulerAngles2quaternion(src_euler_angles[0], 
                                src_euler_angles[1], 
                                src_euler_angles[2])
    dest_q = geometry.eulerAngles2quaternion(dest_euler_angles[0], 
                                dest_euler_angles[1], 
                                dest_euler_angles[2])


def on_display():
    global t, tm
    global src_q, dest_q
    global camera_param
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    
    glLoadIdentity()
    gluLookAt(13, 13, 13,
        0, 0, 0,
        0, 1, 0)

    draw.coordinate_axes(10)

    direction_vec = map(lambda x, y: y - x, src_center, dest_center)
    param_position = [x[1] * (t / tm) + x[0] for x in zip(src_center, direction_vec)]

    qs = geometry.slerp(src_q, dest_q, t, tm)
    rotation_axis, angle = geometry.Q2AxisAngle(qs)

    p, phi = geometry.Q2AxisAngle(dest_q)

    draw.octahedron(param_position, rotation_axis, angle)
    draw.octahedron(dest_center, p, phi)

    glutSwapBuffers()


def on_reshape(w, h):
    glViewport(0, 0, w, h)

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(60, w / float(h), 1, 50)
    glMatrixMode(GL_MODELVIEW)


def on_timer(value):
    global t, tm
    global animation_ongoing
    if value != 0:
        return
    
    if t < tm:
        t += 0.01

    glutPostRedisplay()

    if animation_ongoing:
        glutTimerFunc(20, on_timer, 0)


def set_callbacks():
    glutDisplayFunc(on_display)
    glutKeyboardFunc(on_keyboard)
    glutReshapeFunc(on_reshape)


def main():

    glutInit()
    glutInitDisplayMode(GLUT_RGB|GLUT_DEPTH|GLUT_DOUBLE)
    glutInitWindowSize(600, 600)
    glutCreateWindow("test")

    set_callbacks()
    init()

    glutMainLoop()


if __name__ == "__main__":
    main()