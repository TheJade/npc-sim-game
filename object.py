import os
import math
import pygame
import random


class Object(pygame.sprite.Sprite):
    def __init__(self, width, height, image_path=os.path.join("assets", "assets\Medieval_Castle_Asset_Pack\Tiles\brick_1.png"), x_speed=0, y_speed=0, seed=123, screen_width=960, screen_height=640):
        """
        Create a platform sprite. Note that these platforms are designed to be very wide and not very tall.

        It is required that the width is greater than or equal to the height. It is recommended to make height 50 or less.
        Best visual effects are when the width is a multiple of the height.

        Args:
            x: The x coordinate of the platform
            y: The y coordinate of the platform
            width: The width of the platform. Must be greater than or equal to the height
            height: The height of the platform. Recommended to be 50 or less.
        """
        super().__init__()
        self.image = self.create_image(image_path, width, height)
        self.rect = self.image.get_rect()
        self.rect.x = screen_width
        self.rect.y = random.randrange(screen_height/2)+height + 50

        self.x_speed = x_speed
        self.y_speed = y_speed

    def create_image(self, image_location, width, height):
        tile_image = pygame.image.load(image_location).convert_alpha()
        # The tile is a square and the height is expected to be smaller than the width
        tile_width = height
        tile_height = height
        tile_image = pygame.transform.scale(tile_image, (tile_width, tile_height))

        # The self.image attribute expects a Surface, so we can manually create one and "blit" the tile image onto the surface (i.e. paint an image onto a surface).
        # We use list comprehension to quickly make the blits_data list of tuples (each tuple has the tile image, and the X and Y coordinates)
        # Don't know what list comprehension is? Go look it up on the Internet. That's what all professional software engineers do ;)
        image = pygame.Surface((width, height))
        blits_data = [
            (tile_image, (tile_width * i, 0))
            for i in range(math.ceil(width / tile_width))
        ]
        image.blits(blits_data)

        return image

    def update(self):
        self.move(self.x_speed, self.y_speed)

    def move(self, x_change, y_change):
        self.rect.x += x_change
        self.rect.y += y_change
        
        if self.rect.x < 0:
            self.kill
