import pygame, os

# # Algorytm detekcji kolizji AABB 
# class AABB:
#     def __init__(self, x, y, width, height):
#         self.x = x
#         self.y = y
#         self.width = width
#         self.height = height
    
#     # Metoda do sprawdzania kolizji z innym AABB
#     def collides_with(self, other):
#         return (self.x < other.x + other.width and
#                 self.x + self.width > other.x and
#                 self.y < other.y + other.height and
#                 self.y + self.height > other.y)


# kolory zdefiniwean globalnie
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

class Ship():
    def __init__(self, path, width, height) -> None:
        self.img = pygame.image.load(path).convert_alpha()
        # self.img = pygame.transform.rotate(self.img, 30)
        self.rect = self.img.get_rect()
        self.rect.x = width / 2 - self.rect.centerx
        self.rect.y = height / 2 - self.rect.centery

    def update(self, angle):
        self.img = pygame.transform.rotate(self.img, angle)
        self.rect = self.img.get_rect()

class Bullet():
    def __init__(self) -> None:
        self.img = pygame.Surface((10,10))
        self.rect = self.img.get_rect()
        self.img.fill(RED)
        
    def update(self, colour):
        pos = pygame.mouse.get_pos()
        self.rect.center = (pos)
        self.img.fill(colour)

    def collides_with(self, other):
        return (self.rect.x < other.rect.x + other.rect.width and 
                self.rect.x + self.rect.width > other.rect.x and
                self.rect.y < other.rect.y + other.rect.height and 
                self.rect.y + self.rect.width > other.rect.y)
    

pygame.init()
width, height = 600, 600
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("AABB Algorithm")
clock = pygame.time.Clock()
run = True
fps = 60

def draw_window(win, ship, bullet):
    win.fill(WHITE)
    win.blit(ship.img, ship.rect)
    win.blit(bullet.img, bullet.rect)
    points = [ship.rect.topleft, ship.rect.topright, 
              ship.rect.bottomright, ship.rect.bottomleft]
    pygame.draw.polygon(win, RED, points, 2)
    pygame.display.update()


ship = Ship(os.path.join("assets", "ship.png"), width, height)
bullet = Bullet()

while run:
    clock.tick(fps)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    # key_pressed = pygame.key.get_pressed()
    # if key_pressed[pygame.K_LEFT]:
    #     ship.update(5)
    # if key_pressed[pygame.K_RIGHT]:
    #     ship.update(-5)


    if bullet.collides_with(ship):
        bullet.update(GREEN)
    else:
        bullet.update(RED)
    draw_window(win, ship, bullet)

pygame.quit()
