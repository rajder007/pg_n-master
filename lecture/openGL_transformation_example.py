import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

# Inicjalizacja kamer
def init_camera(display):
    glMatrixMode(GL_PROJECTION)
    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
    glTranslatef(0.0, 0.0, -5)

# Renderowanie sceny
def render_scene(rotation_angle):
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    
    # Wykonanie translacji
    glTranslatef(0.0, 0.5, -5)
    
    # Wykonanie rotacji wokół osi Y
    glRotatef(rotation_angle, 0, 1, 1)
    
    # Rysowanie trójkąta
    glBegin(GL_TRIANGLES)
    glColor3f(1.0, 0.0, 0.0)
    glVertex3f(0.0, 1.0, 0.0)
    glColor3f(0.0, 1.0, 0.0)
    glVertex3f(-1.0, -1.0, 0.0)
    glColor3f(0.0, 0.0, 1.0)
    glVertex3f(1.0, -1.0, 0.0)
    glEnd()


def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

    init_camera(display)

    rotation_angle = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        rotation_angle += 1

        render_scene(rotation_angle)
        pygame.display.flip()
        pygame.time.wait(10)

if __name__ == "__main__":
    main()