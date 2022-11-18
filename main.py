# Created by Schulich Ignite Flare and students of Schulich Ignite

import sys
import os
import pygame
from platforms import Platform
from player import Player
from enemy import Enemy
from background import Background

"""
SETUP section - preparing everything before the main loop runs
"""
pygame.init()

# Global constants
SCALE = 2 # helps with screen sizing

SCREEN_WIDTH = 1920 / SCALE
SCREEN_HEIGHT = 1280 / SCALE
FRAME_RATE = 30

PLATFORM_HEIGHT = 100 / SCALE

# Useful colors 
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

SkyBackGround = Background(os.getcwd()+r'\assets\Medieval_Castle_Asset_Pack\Background\layer_1.png', 
                            location=[0,0], 
                            scale_to=(SCREEN_WIDTH, SCREEN_HEIGHT-PLATFORM_HEIGHT))
CityBackGround1 = Background(os.getcwd()+r'\assets\Medieval_Castle_Asset_Pack\Background\layer_2.png', 
                            location=[0,100], 
                            scale_to=(SCREEN_WIDTH+1, SCREEN_HEIGHT-PLATFORM_HEIGHT-100),
                            x_speed = -1,
                            reset_x=-(SCREEN_WIDTH))
CityBackGround2 = Background(os.getcwd()+r'\assets\Medieval_Castle_Asset_Pack\Background\layer_2.png', 
                            location=[SCREEN_WIDTH,100], 
                            scale_to=(SCREEN_WIDTH+1, SCREEN_HEIGHT-PLATFORM_HEIGHT-100),
                            x_speed = -1,
                            reset_x=-(SCREEN_WIDTH))


# Creating the screen and the clock
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
screen.set_alpha(0)  # Make alpha bits transparent
clock = pygame.time.Clock()

# Platforms sprite group
platforms = pygame.sprite.Group()

platforms.add(Platform(0, SCREEN_HEIGHT-PLATFORM_HEIGHT, SCREEN_WIDTH+1, PLATFORM_HEIGHT, 
                        image_path=os.getcwd()+r'\assets\Medieval_Castle_Asset_Pack\Tiles\floor_tile_3.png',
                        x_speed=-2,
                        reset_x=-SCREEN_WIDTH))

platforms.add(Platform(SCREEN_WIDTH, SCREEN_HEIGHT-PLATFORM_HEIGHT, SCREEN_WIDTH+1, PLATFORM_HEIGHT, 
                        image_path=os.getcwd()+r'\assets\Medieval_Castle_Asset_Pack\Tiles\floor_tile_3.png',
                        x_speed=-2,
                        reset_x=-SCREEN_WIDTH))
                        

enemies = pygame.sprite.Group()
enemies.add(Enemy(750, 410))

# Create the player sprite and add it to the players sprite group
player = Player(400, 500, scale_to=(PLATFORM_HEIGHT*2, PLATFORM_HEIGHT*2))
players = pygame.sprite.Group()
players.add(player)

while True:
    """
    EVENTS section - how the code reacts when users do things
    """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # When user clicks the 'x' on the window, close our game
            pygame.quit()
            sys.exit()
        
    # Keyboard events
    keys_pressed = pygame.key.get_pressed()
    if keys_pressed[pygame.K_UP] or keys_pressed[pygame.K_w]:
        player.jump()
    if keys_pressed[pygame.K_LEFT] or keys_pressed[pygame.K_a]:
        player.move(-player.move_speed, 0)
    if keys_pressed[pygame.K_RIGHT] or keys_pressed[pygame.K_d]:
        player.move(player.move_speed, 0)
    if keys_pressed[pygame.K_DOWN] or keys_pressed[pygame.K_s]:
        pass  # Now that we have platforms, there's no reason to make the player move down.
 
    # Mouse events
    mouse_pos = pygame.mouse.get_pos()  # Get position of mouse as a tuple representing the
    # (x, y) coordinate
 
    mouse_buttons = pygame.mouse.get_pressed()
    if mouse_buttons[0]:  # If left mouse pressed
        player.teleport(mouse_pos[0], mouse_pos[1])
    if mouse_buttons[2]:  # If right mouse pressed
        pass  # Replace this line
 
    """
    UPDATE section - manipulate everything on the screen
    """
    
    players.update()
    enemies.update()
    platforms.update()
    CityBackGround1.update()
    CityBackGround2.update()


    hit_platforms = pygame.sprite.spritecollide(player, platforms, False)
    for platform in hit_platforms:
        player.on_platform_collide(platform)

    if len(hit_platforms) == 0:
        player.can_jump = False

    """
    DRAW section - make everything show up on screen
    """
    screen.fill(BLACK)  # Fill the screen with one colour

    screen.blit(SkyBackGround.image, SkyBackGround.rect)
    screen.blit(CityBackGround1.image, CityBackGround1.rect)
    screen.blit(CityBackGround2.image, CityBackGround2.rect)
    
    platforms.draw(screen)
    players.draw(screen)
    enemies.draw(screen)

    pygame.display.flip()  # Pygame uses a double-buffer, without this we see half-completed frames
    clock.tick(FRAME_RATE)  # Pause the clock to always maintain FRAME_RATE frames per second
