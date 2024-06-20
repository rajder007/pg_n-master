import pygame, os, random
from pygame.math import Vector2
import numpy as np

TILE_SIZE = np.array([32, 32])

global_offset = Vector2(0,0)

board_map = np.array([
    [7,3,3,3,3,3,8,7,3,3,8,0,0,0,0,0,7,3,3,3,3,3,3,3,3,3,8,0,0],
    [5,2,2,2,2,2,4,5,2,2,12,3,3,3,3,3,11,2,2,2,2,2,2,2,2,2,12,8,0],
    [5,2,2,2,2,2,4,5,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,12,8],
    [5,2,2,2,2,2,12,11,2,2,13,6,6,6,6,6,14,2,2,2,2,2,2,2,2,2,2,2,4],
    [5,2,2,2,2,2,2,2,2,2,4,0,0,0,0,0,5,2,2,2,2,2,2,2,2,2,2,2,4],
    [5,2,2,2,2,2,2,2,2,2,4,0,0,0,0,0,5,2,2,2,2,2,2,2,2,2,2,2,4],
    [5,2,2,2,2,2,2,2,2,2,4,0,0,0,0,0,5,2,2,2,2,2,2,2,2,2,2,2,4],
    [5,2,2,2,2,2,2,2,2,2,4,0,0,0,0,0,5,2,2,2,2,2,2,2,2,2,2,2,4],
    [5,2,2,2,13,14,2,2,2,2,4,0,0,0,0,0,10,6,6,6,6,6,6,6,6,6,6,6,9],
    [5,2,2,2,12,11,2,2,2,2,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [5,2,2,2,2,2,2,2,2,2,4,0,0,0,0,0,7,3,3,3,3,3,3,3,3,3,3,3,8],
    [5,2,2,2,2,2,2,2,2,2,4,0,0,0,0,0,5,2,2,2,2,2,2,2,2,2,2,2,4],
    [5,2,2,2,2,2,2,2,2,2,4,0,0,0,0,0,5,2,2,2,2,2,2,2,2,2,2,2,4],
    [5,2,2,2,2,2,2,2,2,2,4,0,0,0,0,0,5,2,2,2,2,2,2,2,2,2,2,2,4],
    [5,2,2,2,13,14,2,2,2,2,12,3,3,3,3,3,11,2,2,2,2,2,13,14,2,2,2,2,4],
    [5,2,2,2,4,5,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,12,11,2,2,2,2,4],
    [10,6,6,6,9,5,2,2,2,2,13,6,6,6,6,6,14,2,2,2,2,2,2,2,2,2,2,2,4],
    [0,0,0,0,0,5,2,2,2,2,4,0,0,0,0,0,5,2,2,2,2,2,2,2,2,2,2,2,4],
    [0,0,0,0,0,5,2,2,2,2,4,0,0,0,0,0,10,6,6,6,6,6,6,6,6,6,6,6,9],
    [0,0,0,0,0,10,6,6,6,6,9,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]])

class BoardMap:

    def determine_offset(self, mouse_pose, width, height):
        if mouse_pose[0] > 50 and mouse_pose[0] < (width - 50) and mouse_pose[1] > 0 and mouse_pose[1] < 50:
            return  Vector2(0,1) # górę
        if mouse_pose[0] > (width - 50) and mouse_pose[0] < width and mouse_pose[1] > 0 and mouse_pose[1] < 50:
            return  Vector2(-1,1) # prawo góra
        if mouse_pose[0] > (width - 50) and mouse_pose[0] < width and mouse_pose[1] > 50 and mouse_pose[1] < (height - 50):
            return  Vector2(-1,0) # prawo
        if mouse_pose[0] > (width - 50) and mouse_pose[0] < width and mouse_pose[1] > (height - 50) and mouse_pose[1] < height:
            return  Vector2(-1,-1) # prawo dół
        if mouse_pose[0] > 50 and mouse_pose[0] < (width-50) and mouse_pose[1] > (height - 50) and mouse_pose[1] < height:
            return  Vector2(0,-1) # dół
        if mouse_pose[0] > 0 and mouse_pose[0] < 50 and mouse_pose[1] > (height - 50) and mouse_pose[1] < height:
            return  Vector2(1,-1) # lewo dół
        if mouse_pose[0] > 0 and mouse_pose[0] < 50 and mouse_pose[1] > 50 and mouse_pose[1] < (height-50):
            return  Vector2(1,0) # lewo
        if mouse_pose[0] > 0 and mouse_pose[0] < 50 and mouse_pose[1] > 0 and mouse_pose[1] < 50:
            return  Vector2(1,1) # lewo góra
        return Vector2(0,0)
    
    def get_element_from_table(self, pos):
        temp_x = int(pos.x /TILE_SIZE[0])
        temp_y = int(pos.y /TILE_SIZE[1])
        # size = board_map.shape * tile_size
        if pos.x > -1 and pos.y > -1:
            print(" {} {} {} ".format(temp_y, temp_x, board_map[temp_y,temp_x]))
            return temp_y, temp_x, board_map[temp_y,temp_x]
        else:
            print(" poza obszarem")
            return None

class BoardTile(pygame.sprite.Sprite):
    def __init__(self, type, x, y) -> None:
        pygame.sprite.Sprite.__init__(self)
        if type == 1:
            self.image = pygame.Surface(TILE_SIZE)
            self.image.fill((0,220,0))
        elif type == 2:
            list_tile = ["kafel_1.png", "kafel_2.png", "kafel_3.png"]
            self.image = pygame.image.load(os.path.join("assets", "map", random.choice(list_tile)) )
            self.image = pygame.transform.rotate(self.image, random.choice([0, 90, 180, 270]))
        elif type == 3:     # ściana górna
            self.image = pygame.image.load(os.path.join("assets", "map", "wall_2.png" ))
        elif type == 4:     # ściana lewa
            self.image = pygame.image.load(os.path.join("assets", "map", "wall_4.png") )
        elif type == 5:     # ściana prawa
            self.image = pygame.image.load(os.path.join("assets", "map", "wall_8.png") )
        elif type == 6:     # ściana dolna
            self.image = pygame.image.load(os.path.join("assets", "map", "wall_6.png") )
        elif type == 7:     # narożniki
            self.image = pygame.image.load(os.path.join("assets", "map", "wall_1.png") )
        elif type == 8:
            self.image = pygame.image.load(os.path.join("assets", "map", "wall_3.png") )
        elif type == 9:     
            self.image = pygame.image.load(os.path.join("assets", "map", "wall_5.png") )
        elif type == 10:
            self.image = pygame.image.load(os.path.join("assets", "map", "wall_7.png") )
        elif type == 11:
            self.image = pygame.image.load(os.path.join("assets", "map", "wall_11.png") )
        elif type == 12:
            self.image = pygame.image.load(os.path.join("assets", "map", "wall_12.png") )
        elif type == 13:
            self.image = pygame.image.load(os.path.join("assets", "map", "wall_9.png") )
        elif type == 14:
            self.image = pygame.image.load(os.path.join("assets", "map", "wall_10.png") )
        
        self.rect = self.image.get_rect()
        self.rect.topleft = (x * TILE_SIZE[0], y * TILE_SIZE[1])
        
    def update(self, offset) -> None:
        self.rect.x += offset.x
        self.rect.y += offset.y