import os
import pygame

class Background(pygame.sprite.Sprite):
    def __init__(self, image_file, location, scale_to=(0,0), x_speed=0, y_speed=0, reset_x=-1000):
        pygame.sprite.Sprite.__init__(self)  #call Sprite initializer
        img = pygame.image.load(image_file)
        if scale_to[0] != 0:
            img = pygame.transform.scale(img, scale_to)
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = location

        self.x_speed = x_speed
        self.y_speed = y_speed

        self.reset_x = reset_x

    def update(self):
        self.move(self.x_speed, self.y_speed)

    def move(self, x_change, y_change):
        self.rect.x += x_change
        self.rect.y += y_change
        
        if self.rect.x < self.reset_x:
            self.rect.x = abs(self.reset_x)