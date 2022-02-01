# Créé par Quentin, le 31/01/2022 en Python 3.7
import pygame

pygame.init()

win = pygame.display.set_mode((500, 500))

pygame.display.set_caption("Jump Game")

x = 200
y = 200

width = 30
height = 40

isjump = False

v = 5
m = 1

run = True

while run:
    win.fill((0, 0, 0))

    pygame.draw.rect(win, (255, 0, 0), (x, y, width, height))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if isjump == False:
        if keys[pygame.K_UP]:
            isjump = True

    if isjump :
        F =(1 / 2)*m*(v**2)
        y-= F
        v = v-1
        if v<0:
            m =-1
        if v ==-6:
            isjump = False
            v = 5
            m = 1

    pygame.time.delay(50)

    pygame.display.update()
pygame.quit()
