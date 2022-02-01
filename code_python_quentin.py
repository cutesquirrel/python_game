import pygame
import time
import random

from PIL import Image

# preparation PIL pour lire pixel du fond1.bmp

im = Image.open('fond_GNG.bmp')
pixel_fond = im.load()

# terrain de jeu

surface = pygame.display.set_mode((700, 710))
pygame.display.set_caption("Ghosts'n Goblins")

# acteurs graphiques

hero_gauche = pygame.image.load('hero2.png')
hero_droite = pygame.image.load('hero3.png')
fond = pygame.image.load('fond_GNG.bmp')
super = pygame.image.load('super.png')
echec = pygame.image.load('echec.png')
mechant1 = pygame.image.load('dragon1.png')
mechant2 = pygame.image.load('dragon2.png')
zombie1 = pygame.image.load('zombie1.png')
zombie2 = pygame.image.load('zombie2.png')


speed = [2, 2]

# sous fonctions


def victoire():
    surface.blit(super, (350, 355))
    pygame.display.update()


def defaite():
    surface.blit(echec, (350, 355))
    pygame.display.update()

# fonction principale


def principal():
    flag = False
    n = 0
    run = True

    isjump = False
    vInit = 8
    v = vInit
    mInit = 1
    m = mInit

    x, y = 10, 39
    x_mvt, y_mvt = 0, 0
    # depart mechant
    xm, ym = 350, 300
    # deplacements mechant
    xm_mvt, ym_mvt = 1, 0
    sens = 'right'

    # on compte les touches appuyees pour pouvoir sauter en meme temps qu'on avance.
    nbTouchesAppuyees = 0

    while run:

        # temps de repos/rafraichissement de 10ms
        time.sleep(0.01)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            # on relache la touche
            if event.type == pygame.KEYUP:
                nbTouchesAppuyees -= 1
                if (nbTouchesAppuyees == 0):
                    x_mvt = 0

            # appui sur touche
            if event.type == pygame.KEYDOWN:
                nbTouchesAppuyees += 1
                if event.key == pygame.K_LEFT:
                    x_mvt = -1
                    sens = 'left'
                if event.key == pygame.K_RIGHT:
                    x_mvt = 1
                    sens = 'right'
                if event.key == pygame.K_UP:
                    isjump = True


        if (isjump):
            F = (1 / 2)*m*(v**2)
            # saut = y diminue puisqu'on monte.
            y -= F
            # print (F, y)
            # au depart, ça monte à v=5, puis la vitesse diminue.

            v -= 1
            # jusqu'à avoir une vitesse negative (redescente).
            if v < 0:
                # on inverse le sens et le calcul du Y du coup.
                m = -1 * mInit
            # fin du saut
            if v == (-1 * vInit):
                isjump = False
                v = vInit
                m = mInit

            pygame.time.delay(10)



        # correction du deplacement si besoin

        # le mechant reste dans le terrain mais traverse les murs !!!
        if (xm < 10) or (xm > 260):
            xm -= xm_mvt

        # pixel defaite (pics)
        if (pixel_fond[x, y+65] == (153, 153, 153)):
            defaite()
            time.sleep(2)
            x, y = 10, 45
            xm, ym = 350, 300
            xm_mvt, ym_mvt = 1, 0

        # pixel victoire (porte)
        if (pixel_fond[x+65, y] == (85, 128, 124)):
            victoire()
            time.sleep(2)
            x, y = 10, 45
            xm, ym = 350, 300
            xm_mvt, ym_mvt = 1, 0

        # platformes vertes (juste le trait)
        if (pixel_fond[x, y+65] == (118, 139, 80)):
            y_mvt = 0
        else:
            y_mvt = 1

        # si collision mechant = defaite
        if (abs(x-xm) < 20) and (abs(y-ym) < 15):
            defaite()
            time.sleep(2)
            x, y = 10, 10
            xm, ym = 350, 300
            xm_mvt, ym_mvt = 1, 0



        # deplacement hero
        x += x_mvt
        y += y_mvt

        # deplacement mechant
        xm += xm_mvt

        # pour que le mechant change de tete et deplacement au bout de 30 x 10 = 300ms
        n += 1
        # 30x10ms=300ms histoire de faire alterner mechant1 et mechant2
        if n > 30:
            n = 0
            # inversion du flag= True/False toutes les 300ms
            flag = not(flag)

        # affichages des acteurs graphiques
        surface.blit(fond, (0, 0))

        if (sens == 'left'):
            surface.blit(hero_droite, (x, y))
        else:
            surface.blit(hero_gauche, (x, y))

        # faire alternner mechant1 et mechant2
        if (flag):
            surface.blit(mechant1, (xm, ym))
        else:
            surface.blit(mechant2, (xm, ym))

        # rafraichissement
        pygame.display.update()


principal()
pygame.quit()
quit()
