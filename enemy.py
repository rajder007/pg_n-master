import pygame, math, random
from board_map import *
from hero import Hero

class Enemy(Hero):

    def __init__(self, x, y, player, name):
        super().__init__(x, y, name)
        self.speed = 1.5
        self.player = player
        self.get_enemy_img(name)

    # def move(self, type):
    #     if type != None:
    #         if type == "attac":
    #             dx = self.player.pose.x - self.rect.centerx
    #             dy = self.player.pose.y - self.rect.centery
    #             distance = math.sqrt(dx**2 + dy**2)
    #             if distance < 50:
    #                 self.speed = 2
    #             else:
    #                 self.speed = 0
    #             if distance != 0:
    #                 dx /= distance
    #                 dy /= distance
    #             self.rect.centerx += dx * self.speed
    #             self.rect.centery += dy * self.speed
    #         elif type == "run":
    #             if self.dest_pos.distance_to(self.pose) < 0.5:
    #                 # założenie że przeciwnik ucieka w  losowym kierunku
    #                 self.action = random.randint(0,8)
    #                 match self.action:
    #                     case 0:
    #                         if board_map[self.row-1, self.cell-1] == 2:
    #                             self.dest_pos = self.set_position(self.row-1, self.cell-1)
    #                     case 1:
    #                         if board_map[self.row-1, self.cell] == 2:
    #                             self.dest_pos = self.set_position(self.row-1, self.cell)
    #                     case 2:
    #                         if board_map[self.row-1, self.cell+1] == 2:
    #                             self.dest_pos = self.set_position(self.row-1, self.cell+1)
    #                     case 3:
    #                         if board_map[self.row, self.cell+1] == 2:
    #                             self.dest_pos = self.set_position(self.row, self.cell+1)
    #                     case 4:
    #                         if board_map[self.row+1, self.cell+1] == 2:
    #                             self.dest_pos = self.set_position(self.row+1, self.cell+1)
    #                     case 5:
    #                         if board_map[self.row+1, self.cell] == 2:
    #                             self.dest_pos = self.set_position(self.row+1, self.cell)
    #                     case 6:
    #                         if board_map[self.row+1, self.cell] == 2:
    #                             self.dest_pos = self.set_position(self.row+1, self.cell-1)
    #                     case 7:
    #                         if board_map[self.row+1, self.cell] == 2:
    #                             self.dest_pos = self.set_position(self.row, self.cell)


    def get_enemy_img(self, name):
        width, height = 16, 16
        enemy_img_pos = { "enemy_1": 0, "enemy_2": 1, "enemy_3": 2, "mag": 3}
        img = pygame.image.load( os.path.join("assets", "objects", "Dungeon_Character_2.png") )
        image = pygame.Surface((width, height), pygame.SRCALPHA).convert_alpha()
        image.blit(img, (0,0), ((enemy_img_pos[name] * width), 0, width, height))
        image.set_colorkey()
        self.image = image

    def check_distance(self):
        dx = self.player.pose.x - self.rect.centerx
        dy = self.player.pose.y - self.rect.centery
        return math.sqrt(dx**2 + dy**2)
    
    def interaction(self):
        distance = self.check_distance()
        if distance < 50:
            match self.behavior:
                case "agressive":
                    self.move("attac")
                case "passive":
                    self.move("run")
        else:
            self.move(None)