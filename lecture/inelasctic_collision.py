import pygame
import sys
import math

# Initialize Pygame
pygame.init()

# Ustawienia okna
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Elastic Reflection Simulation (Zero-G)")

# Kolory
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

FPS = 60

class Ball():
    def __init__(self, pose, color, speed) -> None:
        self.ball_radius = 20
        self.ball_color = color
        self.ball_pos = pose
        self.ball_speed = speed 

    def update_position(self):
        self.ball_pos += self.ball_speed

    def check_collision(self):
        if self.ball_pos.x + self.ball_radius > WIDTH or self.ball_pos.x - self.ball_radius < 0:
            self.ball_speed.x *= -1  # Reverse direction in x-axis

        if self.ball_pos.y + self.ball_radius > HEIGHT or self.ball_pos.y - self.ball_radius < 0:
            self.ball_speed.y *= -1  # Reverse direction in y-axis

# Main loop
clock = pygame.time.Clock()

red_ball = Ball(pygame.math.Vector2(30, 50), RED, pygame.math.Vector2(0,0))
black_ball = Ball(pygame.math.Vector2(300, 150), BLACK, pygame.math.Vector2(-3,4))

def check_ball_collision(ball_red, ball_black):
    distance = math.sqrt((red_ball.ball_pos.x - black_ball.ball_pos.x) ** 2 + (red_ball.ball_pos.y - black_ball.ball_pos.y) ** 2)
    if distance < red_ball.ball_radius + black_ball.ball_radius:
        # Calculate new velocities after collision
        new_ball_speed_x = (red_ball.ball_speed.x + black_ball.ball_speed.x) / 2
        new_ball_speed_y = (red_ball.ball_speed.y + black_ball.ball_speed.y) / 2

        black_ball.ball_speed = pygame.math.Vector2(new_ball_speed_x, new_ball_speed_y)


def draw_window(screen, red_ball, black_ball):
    screen.fill(WHITE)
    pygame.draw.circle(screen, red_ball.ball_color, red_ball.ball_pos, red_ball.ball_radius)
    pygame.draw.circle(screen, black_ball.ball_color, black_ball.ball_pos, black_ball.ball_radius)
    pygame.display.flip()

while True:
    # screen.fill(WHITE)
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    key_pressed = pygame.key.get_pressed()
    if key_pressed[pygame.K_LEFT]:
        red_ball.ball_speed.x -= 0.1
    if key_pressed[pygame.K_RIGHT]:
        red_ball.ball_speed.x += 0.1
    if key_pressed[pygame.K_UP]:
        red_ball.ball_speed.y -= 0.1
    if key_pressed[pygame.K_DOWN]:
        red_ball.ball_speed.y += 0.1
    
    black_ball.update_position()
    black_ball.check_collision()
    red_ball.update_position()
    red_ball.check_collision()
    check_ball_collision(red_ball, black_ball)
    draw_window(screen, red_ball, black_ball)

