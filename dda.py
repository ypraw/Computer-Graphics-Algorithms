#  test.py on  artificialIntelligence Project
__author__ = " Ypraw "
__date__ = "May 6, 2017  21.46 "

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *


def initFun():
    glClearColor(1.0, 1.0, 1.0, 0.0)
    glColor3f(1.0, 1.0, 1.0)
    glPointSize(1.0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(-640.0, 640.0, -480.0, 480.0)


def AlgDDA():
    # tentukan titik awal dan akhir
    x1 = 0
    y1 = 0
    x2 = 80
    y2 = 40
    x = x1
    y = y1

    # hitung dx dan dy
    dx = x2 - x1
    dy = y2 - y1

    # hitung steps
    if (abs(dx) > abs(dy)):
        steps = abs(dx)
    else:
        steps = abs(dy)

    # hitung perubahan nilai x (x_inc) dan y (y_inc)
    x_inc = dx / steps
    y_inc = dy / steps

    # gambar titik awal
    glBegin(GL_POINTS)
    glVertex2i(x, y)  # gambar titik awal

    # perulangan untuk menggambar titik-titik
    for k in range(0, steps):
        x += x_inc
        y += y_inc
        print("koordinat perubahan-", k + 1, "(", x, ";", y, ")")
        glVertex2i(round(x), round(y))  # gambar titik

    glEnd()
    glFlush()


if __name__ == '__main__':
    glutInit()
    glutInitWindowSize(640, 480)
    glutCreateWindow('Algoritma DDA')
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGBA)
    glutDisplayFunc(AlgDDA)
    initFun()
    glutMainLoop()
