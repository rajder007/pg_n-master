import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

camera_x, camera_y, camera_z = 0,0,0
mouse_x, mouse_y, yaw, pitch = 0,0,0,0
# Inicjalizacja kamer
def init_camera(display):
    glMatrixMode(GL_PROJECTION)
    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
    glTranslatef(0.0, 0.0, -5)

# Obsługa klawiszy do przesuwania kamery
def handle_keys():
    global camera_x, camera_y, camera_z

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        camera_x += 0.1
    if keys[pygame.K_RIGHT]:
        camera_x -= 0.1
    if keys[pygame.K_UP]:
        camera_y -= 0.1
    if keys[pygame.K_DOWN]:
        camera_y += 0.1
    if keys[pygame.K_w]:
        camera_z += 0.1
    if keys[pygame.K_s]:
        camera_z -= 0.1

# Obsługa myszy do obracania kamery
def handle_mouse():
    global yaw, pitch, mouse_x, mouse_y

    x, y = pygame.mouse.get_pos()
    dx = x - mouse_x
    dy = y - mouse_y
    mouse_x = x
    mouse_y = y

    sensitivity = 0.1
    yaw += dx * sensitivity
    pitch += dy * sensitivity

    # Ograniczenie ruchu kamery w pionie
    if pitch > 90:
        pitch = 90
    elif pitch < -90:
        pitch = -90

    # Ustawienie rotacji kamery
    glRotatef(pitch, 1, 0, 0)
    glRotatef(yaw, 0, 1, 0)

# Renderowanie sceny
def render_scene():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    glTranslatef(camera_x, camera_y, camera_z)

    handle_mouse()  # Obsługa myszy do obracania kamery

    glBegin(GL_TRIANGLES)
    glColor3f(1.0, 0.0, 0.0)
    glVertex3f(0.0, 1.0, 0.0)
    glColor3f(0.0, 1.0, 0.0)
    glVertex3f(-1.0, -1.0, 0.0)
    glColor3f(0.0, 0.0, 1.0)
    glVertex3f(1.0, -1.0, 0.0)
    glEnd()

# Główna pętla programu
def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

    init_camera(display)

    yaw = 0
    pitch = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        handle_keys()

        render_scene()
        pygame.display.flip()
        pygame.time.wait(10)

if __name__ == "__main__":
    main()