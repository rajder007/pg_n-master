import os.path
import pygame

WIDTH, HEIGHT = 600, 600
FPS = 60
pygame.display.init()
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Firs Game")
clock = pygame.time.Clock()
run = True

def draw_figure(win):
    pygame.draw.rect(win, (255, 0, 0), (100, 100, 50, 50), border_radius=20)
    pygame.draw.circle(win, (255, 250, 0), (160, 200), 50)
    pygame.draw.polygon(win, (0, 0, 255), [[200, 50], [320, 60], [290, 200]])
    pygame.draw.line(win, (0, 200, 0), (100, 300), (250, 290), 2)
    pygame.draw.line(win, (0, 200, 0), (250, 290), (320, 200), 2)
    pygame.draw.line(win, (0, 200, 0), (320, 200), (330, 100), 2)

def add_background(win, background):
    win.blit(background, (0,0))

def add_img():
    img = pygame.image.load(os.path.join("assets", "3B.png")).convert_alpha()
    img = pygame.transform.scale(img, (img.get_width()/2, img.get_height()/2))
    img = pygame.transform.rotate(img, 120)
    
    return img

def draw_window(win, back_img, img):
    win.fill((0, 60, 60))
    # draw_figure(win)
    add_background(win, back_img)
    
    win.blit(img, (WIDTH/2, HEIGHT/2))

    pygame.display.update()

def get_info_about_window():
    print("wielkość okna: {}".format(pygame.display.get_window_size()) )
    print("Informacje o oknach: {}".format(pygame.display.get_wm_info()))
    print("infromacje o rozdzielczości ekranów:") 
    print(pygame.display.get_desktop_sizes())
    print("informacje ogólne: ")
    print(pygame.display.Info())

img = add_img()
background = pygame.image.load(os.path.join( "assets", "Nebula1.png"))

get_info_about_window()

while run:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    draw_window(win, background, img)
    # sprawdzanie ile astreoid jest stworzonych

pygame.quit()
