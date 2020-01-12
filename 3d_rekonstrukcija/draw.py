from OpenGL.GL import *


def slika2_reconstructed_cubes(ps):

    glColor3f(1, 0, 0)
    glBegin(GL_LINES)
    # tea box
    glVertex3f(ps[0][0], ps[0][1], ps[0][2])
    glVertex3f(ps[1][0], ps[1][1], ps[1][2])
    
    glVertex3f(ps[1][0], ps[1][1], ps[1][2])
    glVertex3f(ps[2][0], ps[2][1], ps[2][2])

    glVertex3f(ps[2][0], ps[2][1], ps[2][2])
    glVertex3f(ps[3][0], ps[3][1], ps[3][2])
    
    glVertex3f(ps[3][0], ps[3][1], ps[3][2])
    glVertex3f(ps[0][0], ps[0][1], ps[0][2])
    
    glVertex3f(ps[0][0], ps[0][1], ps[0][2])
    glVertex3f(ps[4][0], ps[4][1], ps[4][2])
    
    glVertex3f(ps[3][0], ps[3][1], ps[3][2])
    glVertex3f(ps[7][0], ps[7][1], ps[7][2])
    
    glVertex3f(ps[2][0], ps[2][1], ps[2][2])
    glVertex3f(ps[6][0], ps[6][1], ps[6][2])

    glVertex3f(ps[1][0], ps[1][1], ps[1][2])
    glVertex3f(ps[5][0], ps[5][1], ps[5][2])

    glVertex3f(ps[5][0], ps[5][1], ps[5][2])
    glVertex3f(ps[6][0], ps[6][1], ps[6][2])

    glVertex3f(ps[6][0], ps[6][1], ps[6][2])
    glVertex3f(ps[7][0], ps[7][1], ps[7][2])

    glVertex3f(ps[7][0], ps[7][1], ps[7][2])
    glVertex3f(ps[4][0], ps[4][1], ps[4][2])

    glVertex3f(ps[4][0], ps[4][1], ps[4][2])
    glVertex3f(ps[5][0], ps[5][1], ps[5][2])

    # phone box
    glColor3f(0, 1, 0)
    glVertex3f(ps[8][0], ps[8][1], ps[8][2])
    glVertex3f(ps[9][0], ps[9][1], ps[9][2])

    glVertex3f(ps[9][0], ps[9][1], ps[9][2])
    glVertex3f(ps[10][0], ps[10][1], ps[10][2])

    glVertex3f(ps[10][0], ps[10][1], ps[10][2])
    glVertex3f(ps[11][0], ps[11][1], ps[11][2])

    glVertex3f(ps[11][0], ps[11][1], ps[11][2])
    glVertex3f(ps[8][0], ps[8][1], ps[8][2])

    glVertex3f(ps[8][0], ps[8][1], ps[8][2])
    glVertex3f(ps[12][0], ps[12][1], ps[12][2])

    glVertex3f(ps[9][0], ps[9][1], ps[9][2])
    glVertex3f(ps[13][0], ps[13][1], ps[13][2])
    
    glVertex3f(ps[10][0], ps[10][1], ps[10][2])
    glVertex3f(ps[14][0], ps[14][1], ps[14][2])
    
    glVertex3f(ps[11][0], ps[11][1], ps[11][2])
    glVertex3f(ps[15][0], ps[15][1], ps[15][2])
    
    glVertex3f(ps[15][0], ps[15][1], ps[15][2])
    glVertex3f(ps[12][0], ps[12][1], ps[12][2])

    glVertex3f(ps[12][0], ps[12][1], ps[12][2])
    glVertex3f(ps[13][0], ps[13][1], ps[13][2])

    glVertex3f(ps[13][0], ps[13][1], ps[13][2])
    glVertex3f(ps[14][0], ps[14][1], ps[14][2])

    glVertex3f(ps[14][0], ps[14][1], ps[14][2])
    glVertex3f(ps[15][0], ps[15][1], ps[15][2])

    # wazabi box
    glColor3f(0, 0, 1)
    glVertex3f(ps[16][0], ps[16][1], ps[16][2])
    glVertex3f(ps[17][0], ps[17][1], ps[17][2])

    glVertex3f(ps[17][0], ps[17][1], ps[17][2])
    glVertex3f(ps[18][0], ps[18][1], ps[18][2])

    glVertex3f(ps[18][0], ps[18][1], ps[18][2])
    glVertex3f(ps[19][0], ps[19][1], ps[19][2])

    glVertex3f(ps[19][0], ps[19][1], ps[19][2])
    glVertex3f(ps[16][0], ps[16][1], ps[16][2])

    glVertex3f(ps[16][0], ps[16][1], ps[16][2])
    glVertex3f(ps[20][0], ps[20][1], ps[20][2])

    glVertex3f(ps[17][0], ps[17][1], ps[17][2])
    glVertex3f(ps[21][0], ps[21][1], ps[21][2])

    glVertex3f(ps[18][0], ps[18][1], ps[18][2])
    glVertex3f(ps[22][0], ps[22][1], ps[22][2])

    glVertex3f(ps[19][0], ps[19][1], ps[19][2])
    glVertex3f(ps[23][0], ps[23][1], ps[23][2])

    glVertex3f(ps[20][0], ps[20][1], ps[20][2])
    glVertex3f(ps[23][0], ps[23][1], ps[23][2])

    glVertex3f(ps[20][0], ps[20][1], ps[20][2])
    glVertex3f(ps[21][0], ps[21][1], ps[21][2])

    glVertex3f(ps[22][0], ps[22][1], ps[22][2])
    glVertex3f(ps[21][0], ps[21][1], ps[21][2])

    glVertex3f(ps[22][0], ps[22][1], ps[22][2])
    glVertex3f(ps[23][0], ps[23][1], ps[23][2])


    glEnd()

def reconstructed_cubes(ps):

    glColor3f(0, 0, 1)
    glBegin(GL_LINES)
    # iscrtavanje manje kutije
    # prava 1 - 2
    glVertex3f(ps[0][0], ps[0][1], ps[0][2])
    glVertex3f(ps[1][0], ps[1][1], ps[1][2])

    # 2 - 3
    glVertex3f(ps[1][0], ps[1][1], ps[1][2])
    glVertex3f(ps[2][0], ps[2][1], ps[2][2])
    
    # 3 - 4
    glVertex3f(ps[2][0], ps[2][1], ps[2][2])
    glVertex3f(ps[3][0], ps[3][1], ps[3][2])

    # 4 - 1
    glVertex3f(ps[3][0], ps[3][1], ps[3][2])
    glVertex3f(ps[0][0], ps[0][1], ps[0][2])

    # 1 - 5
    glVertex3f(ps[0][0], ps[0][1], ps[0][2])
    glVertex3f(ps[4][0], ps[4][1], ps[4][2])
   
    # 2 - 6
    glVertex3f(ps[1][0], ps[1][1], ps[1][2])
    glVertex3f(ps[5][0], ps[5][1], ps[5][2])

    # 3 - 7
    glVertex3f(ps[2][0], ps[2][1], ps[2][2])
    glVertex3f(ps[6][0], ps[6][1], ps[6][2])

    # 4 - 8
    glVertex3f(ps[3][0], ps[3][1], ps[3][2])
    glVertex3f(ps[7][0], ps[7][1], ps[7][2])

    # 5 - 6
    glVertex3f(ps[4][0], ps[4][1], ps[4][2])
    glVertex3f(ps[5][0], ps[5][1], ps[5][2])

    # 7 - 6
    glVertex3f(ps[6][0], ps[6][1], ps[6][2])
    glVertex3f(ps[5][0], ps[5][1], ps[5][2])

    # 8 - 7
    glVertex3f(ps[6][0], ps[6][1], ps[6][2])
    glVertex3f(ps[7][0], ps[7][1], ps[7][2])

    # 5 - 8
    glVertex3f(ps[4][0], ps[4][1], ps[4][2])
    glVertex3f(ps[7][0], ps[7][1], ps[7][2])
    glEnd()

    glColor3f(0, 1, 0)
    glBegin(GL_LINES)

    # velika kocka
    # 10 - 9
    glVertex3f(ps[9][0], ps[9][1], ps[9][2])
    glVertex3f(ps[8][0], ps[8][1], ps[8][2])

    # 9 - 13
    glVertex3f(ps[12][0], ps[12][1], ps[12][2])
    glVertex3f(ps[8][0], ps[8][1], ps[8][2])

    # 13 - 14
    glVertex3f(ps[12][0], ps[12][1], ps[12][2])
    glVertex3f(ps[13][0], ps[13][1], ps[13][2])

    # 14 - 10
    glVertex3f(ps[9][0], ps[9][1], ps[9][2])
    glVertex3f(ps[13][0], ps[13][1], ps[13][2])

    # 14 - 15
    glVertex3f(ps[14][0], ps[14][1], ps[14][2])
    glVertex3f(ps[13][0], ps[13][1], ps[13][2])

    # 10 - 11
    glVertex3f(ps[9][0], ps[9][1], ps[9][2])
    glVertex3f(ps[10][0], ps[10][1], ps[10][2])

    # 9 - 12
    glVertex3f(ps[8][0], ps[8][1], ps[8][2])
    glVertex3f(ps[11][0], ps[11][1], ps[11][2])


    # 13 - 16
    glVertex3f(ps[12][0], ps[12][1], ps[12][2])
    glVertex3f(ps[15][0], ps[15][1], ps[15][2])

    # 15 - 16
    glVertex3f(ps[14][0], ps[14][1], ps[14][2])
    glVertex3f(ps[15][0], ps[15][1], ps[15][2])

    # 15 - 11
    glVertex3f(ps[14][0], ps[14][1], ps[14][2])
    glVertex3f(ps[10][0], ps[10][1], ps[10][2])

    # 11 -12 
    glVertex3f(ps[11][0], ps[11][1], ps[11][2])
    glVertex3f(ps[10][0], ps[10][1], ps[10][2])

    # 16 -12 
    glVertex3f(ps[11][0], ps[11][1], ps[11][2])
    glVertex3f(ps[15][0], ps[15][1], ps[15][2])
    glEnd()