import pygame

class ObjectMap(pygame.sprite.Sprite):

    def __init__(self, row, cell, type, name=None, value=0) -> None:
        self.name = name
        self.type = type
        self.row = row
        self.cell = cell
        self.image = pygame.Surface((30,30))
        self.circle = pygame.draw.circle(self.image, (160,50,30), (15,15), 6)
        self.image.blit(self.circle)
        # self.image.fill((140,190,130))
        self.rect = self.image.get_rect()
        self.pose = pygame.math.Vector2(self.set_position(row, cell))
        self.rect.center = self.pose

    def update(self, offset) -> None:
        self.rect.x += offset.x
        self.rect.y += offset.y

    def set_position(self, row, cell):
        temp_pos = pygame.math.Vector2([0,0])
        temp_pos.x = cell * 30 + 15
        temp_pos.y = row * 30 + 15
        # temp_pos += self.player.global_offset
        return temp_pos