import os
import pygame

class Enemy(pygame.sprite.Sprite):
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

    def animate(self):
        self.image = pygame.image.load(os.getcwd()+self.img_path+'/'+self.img_list[self.image_num])
        if self.scale_to[0] != 0:
            self.image = pygame.transform.scale(self.image, self.scale_to)
        self.image_num = (self.image_num + 1) % len(self.img_list)