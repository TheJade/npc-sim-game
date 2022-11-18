import os
import pygame

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 800
 
class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, scale_to=(0,0)):
        super().__init__()
 
        img = pygame.image.load(r'C:\Users\Jade\Documents\GitHub\flare\jades game\npc sim\assets\Lively_NPCs_v3.0\individual sprites\medieval\elder\elder_1.png')
        if scale_to[0] != 0:
            img = pygame.transform.scale(img, scale_to)
        self.image = img
        
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