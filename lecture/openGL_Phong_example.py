import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

sphere = gluNewQuadric()

# Funkcja inicjalizująca
def init():
    glClearColor(0.0, 0.0, 0.0, 1.0)
    glEnable(GL_DEPTH_TEST)
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glEnable(GL_COLOR_MATERIAL)

# Funkcja renderująca
def render():
    global sphere
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    
    # Ustawienie pozycji źródła światła
    light_position = [0.1, 2.0, 0.0, 1.0]
    glLightfv(GL_LIGHT0, GL_POSITION, light_position)

    # Ustawienie koloru obiektu
    glColor3f(1.0, 0.0, 0.0)

    # Włączenie i ustawienie właściwości materiału
    glMaterialfv(GL_FRONT, GL_AMBIENT, [0.1, 0.1, 0.1, 1.0])
    glMaterialfv(GL_FRONT, GL_DIFFUSE, [0.5, 0.5, 0.5, 1.0])
    glMaterialfv(GL_FRONT, GL_SPECULAR, [1.0, 1.0, 1.0, 1.0])
    glMaterialf(GL_FRONT, GL_SHININESS, 100.0)

    # Narysowanie obiektu (np. kuli)
    # glutSolidSphere(1.0, 50, 50)
    gluSphere(sphere, 0.5, 64, 8)
    pygame.display.flip()

# Funkcja główna
def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

    init()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        render()

if __name__ == "__main__":
    main()