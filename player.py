import os
import pygame

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 800
 
class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, img_path, scale_to=(0,0)):
        super().__init__()
 
        self.scale_to = scale_to
        self.img_path = img_path

        path = os.getcwd() + img_path
        self.img_list = os.listdir(path)

        self.image_num = 0
        self.image = pygame.image.load(os.getcwd()+self.img_path+'/'+self.img_list[0])
        self.animate()
        
        self.rect = self.image.get_rect()
 
        self.rect.x = x
        self.rect.y = y
 
        self.move_speed = 5
        self.speed_y = 0
        self.gravity = 0.6
        
        self.can_jump = True
 
    def update(self):
        # Make the player fall due to gravity
        self.fall()
        if self.rect.x < 200:
            self.kill()
            print("YOU ARE DEAD")
 
    def move(self, x_change, y_change):
        self.rect.x += x_change
        self.rect.y += y_change

        # LOOPS THE SCREEN
        if self.rect.x > SCREEN_WIDTH:
            self.rect.x = 0
        elif self.rect.x < 0:
            self.rect.x = SCREEN_WIDTH

        if self.rect.y > SCREEN_HEIGHT:
            self.rect.y = 0
        elif self.rect.y < 0:
            self.rect.y = SCREEN_HEIGHT
        
    def teleport(self, x, y):
        self.rect.x = x
        self.rect.y = y
 
    def fall(self):
        self.move(0, self.speed_y)
        self.speed_y += self.gravity
 
    def jump(self):
        if not self.can_jump:
            return
        self.speed_y = -15
        self.can_jump = False
 
    def on_platform_collide(self, platform):
        # Need to set self.rect.y explicitly to avoid having the player clip through the floor
        # Note a new bug surfaces - players jumping from the underside will teleport to the top. This is left for students to solve if they want
        self.rect.y = platform.rect.y - self.rect.height
        
 
        self.speed_y = 0
        self.can_jump = True

    def on_object_collide(self, object):
        if self.rect.y-20 < object.rect.y - self.rect.height:
            self.rect.y = object.rect.y - self.rect.height
        elif self.rect.x-20 < object.rect.x - self.rect.width:
            self.rect.x = object.rect.x - self.rect.width
        self.speed_y = 0
        self.can_jump = True

    def animate(self):
        self.image = pygame.image.load(os.getcwd()+self.img_path+'/'+self.img_list[self.image_num])
        if self.scale_to[0] != 0:
            self.image = pygame.transform.scale(self.image, self.scale_to)
        self.image_num = (self.image_num + 1) % len(self.img_list)