# Créé par Quentin, le 31/01/2022 en Python 3.7
import pygame

pygame.init()
win = pygame.display.set_mode((500, 500))

playerX = 250
playerY = 250
vel_x = 10
vel_y = 10
jump = False

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_a] and playerX > 0:
        playerX -= vel_x
    elif keys[pygame.K_d] and playerX < 500:
        playerX += vel_x

    if jump == False and keys[pygame.K_SPACE]:
        jump = True
    elif jump == True:
        playerY -= vel_y * 4
        vel_y -= 1
        if vel_y < -10:
            jump = False
            vel_y = 10

    win.fill((0, 0, 0))
    pygame.draw.circle(win, (255, 255, 255), (int(playerX), int(playerY)), 15)
    pygame.display.update()
    pygame.time.delay(30)

pygame.quit()

