import os.path
import pygame
from pygame.math import Vector2

WIDTH, HEIGHT = 600, 600
FPS = 60
pygame.display.init()
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("MyFirsGame")
clock = pygame.time.Clock()

img = pygame.image.load(os.path.join("assets", "3B.png"))
img = pygame.transform.scale(img, (img.get_width() / 2, img.get_height() / 2))

def event_key(win):
    run = True
    img_pose = pygame.math.Vector2(30, 30)
    img_rect = pygame.Rect(img_pose.x, img_pose.y, img.get_width(), img.get_height())
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        key_pressed = pygame.key.get_pressed()
        if key_pressed[pygame.K_LEFT] and img_rect.x > 0:
            img_rect.x -= 1
        if key_pressed[pygame.K_RIGHT] and img_rect.x + img_rect.height < win.get_width():
            img_rect.x += 1
        if key_pressed[pygame.K_UP] and img_rect.y > 0:
            img_rect.y -= 1
        if key_pressed[pygame.K_DOWN] and img_rect.y + img_rect.width < win.get_height():
            img_rect.y += 1
        if key_pressed[pygame.K_d] and img_rect.x + img_rect.height < win.get_width():
            img_rect.x += 5

        draw_window_event(win, img_rect)

    pygame.quit()
def event_mouse(win):
    run = True
    moving = False
    x, y, x1, y1 = 0,0,0,0
    while run:
        clock.tick(FPS)
        win.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                # check if mouse pointer is in square
                    if x1 <= event.pos[0] <= x1 + 50 and y1 <= event.pos[1] <= y1 + 50:
                        moving = True
                        # determine the distance to the top left corner of the square
                        x, y = event.pos[0] - x1, event.pos[1] - y1
            if event.type == pygame.MOUSEBUTTONUP:
                moving = False
            if event.type == pygame.MOUSEMOTION:
                if moving:
                    # set the coordinates of the top left corner of the square
                    x1, y1 = event.pos[0] - x, event.pos[1] - y
            win.fill((0, 0, 0))
            pygame.draw.rect(win, (255, 0, 0), ((x1, y1), (50, 50)))
            pygame.display.flip()

    pygame.quit()

def draw_window_event(win, img_rect):
    win.fill((0, 0, 0))
    win.blit(img, (img_rect.x, img_rect.y))
    pygame.display.update()

if __name__ == "__main__":
    event_key(win)
    # event_mouse(win)
