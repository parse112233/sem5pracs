import pygame

pygame.init()
screen=pygame.display.set_mode((600, 600))
running=True
pygame.display.set_caption("Space Shooter")
icon=pygame.image.load("gameicon.jpg")
pygame.display.set_icon(icon)

playerImg=pygame.image.load("ufo.png")
playerX=300
playerY=500
change_x=0
def player(playerX,playerY):
    screen.blit(playerImg,(playerX,playerY))
while running:
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:
                change_x=-0.5
            if event.key==pygame.K_RIGHT:
                change_x=0.5
        if event.type==pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key==pygame.K_RIGHT:
                change_x=0
    playerX+=change_x
    if playerX<=0:
        playerX=0
    elif playerX>=550:
        playerX=550
    player(playerX,playerY)
    pygame.display.update()
