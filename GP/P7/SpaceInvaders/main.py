import pygame
import random
# Initialize Pygame
pygame.init()

# Creating a display window
screen = pygame.display.set_mode((800, 600))

# Setting window title
pygame.display.set_caption("Space Invaders")

# To use any image in pygame you have to load it first
icon = pygame.image.load("ufo.png")
player_img = pygame.image.load("player.png")

# Setting the icon of the window
pygame.display.set_icon(icon)

# Player co-ordinates
playerX = 360
playerY = 500
playerX_change=0
#adding enemy
enemyImg=pygame.image.load("enemy.png")
enmyX=random.randint(0,800)
enmyY=random.randint(50,150)
enemyX_change=4
enemyX_change=40
#bullet
# ready - you
# Rendering player image inside the game window
#fire -the bullet is corrently moving
bulletImg=pygame.image.load("bullet.png")
bulletX=0
bulletY=480
culletX_change=0
bulletY_change=10

def player(x, y):
  screen.blit(player_img, (x, y))
playerX_change = 0
playerY_change = 0

# Hold the window from not closing
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Checking if any keys are pressed
        if event.type == pygame.KEYDOWN:
            # Checking if the key is left or right
            if event.key == pygame.K_RIGHT:
                playerX_change += 0.3
            if event.key == pygame.K_LEFT:
                playerX_change -= 0.3

            if event.key == pygame.K_UP:
                playerY_change -= 0.3
            if event.key == pygame.K_DOWN:
                playerY_change += 0.3
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_LEFT:
                playerX_change=0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                playerY_change = 0
    # Setting the window background
    screen.fill((24, 40, 95))
    playerX += playerX_change
    playerY += playerY_change
    player(playerX, playerY)

    # Updating the changes

