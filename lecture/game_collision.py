import os.path
import pygame

# pygame.display.init()
WIDTH, HEIGHT = 600, 600
FPS = 60
RED = (250, 0, 0)
BLUE = (0, 0, 250)
GREEN = (0, 250, 0)
YELLOW = (0, 260, 250)

win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("MyFirsGame")
clock = pygame.time.Clock()

class Ship():
    def __init__(self, path) -> None:
        # self.img = pygame.image.load(os.path.join("assets", "3B.png")).convert_alpha()
        self.img = pygame.image.load(path).convert_alpha()
        self.rect = self.img.get_rect()
        self.mask = pygame.mask.from_surface(self.img)

class Bullet():
    def __init__(self) -> None:
        self.img = pygame.Surface((10,10))
        self.rect = self.img.get_rect()
        self.img.fill(RED)
        self.mask = pygame.mask.from_surface(self.img)

    def update(self, colour):
        pos = pygame.mouse.get_pos()
        self.rect.center = (pos)
        self.img.fill(colour)

ship = Ship(os.path.join("assets", "3B.png"))
bullet = Bullet()
run = True
moving = False
x, y, x1, y1 = 0,0,0,0
while run:
    clock.tick(FPS)
    win.fill((0, 0, 0))
    win.blit(ship.img, ship.rect)

    if ship.mask.overlap(bullet.mask, (bullet.rect.center[0] - ship.rect.x,
                                        bullet.rect.center[1] - ship.rect.y)):
        bullet.update(GREEN)
    else:
        bullet.update(RED)

    win.blit(bullet.img, bullet.rect)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        # if event.type == pygame.MOUSEBUTTONDOWN:
        #     # check if mouse pointer is in square
        #     if x1 <= event.pos[0] <= x1 + 50 and y1 <= event.pos[1] <= y1 + 50:
        #         moving = True
        #         # determine the distance to the top left corner of the square
        #         x, y = event.pos[0] - x1, event.pos[1] - y1
        # if event.type == pygame.MOUSEBUTTONUP:
        #     moving = False
        # if event.type == pygame.MOUSEMOTION:
        #     if moving:
        #         # set the coordinates of the top left corner of the square
        #         x1, y1 = event.pos[0] - x, event.pos[1] - y
        # win.fill((0, 0, 0))
        # pygame.draw.rect(win, (255, 0, 0), ((x1, y1), (50, 50)))
        # pygame.display.flip()
    pygame.display.update()
pygame.quit()
