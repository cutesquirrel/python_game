import pygame
import time
import random

from PIL import Image

# preparation PIL pour lire pixel du fond1.bmp

im = Image.open('fond_GNG.bmp')
pixel_fond = im.load()

# terrain de jeu

surface = pygame.display.set_mode((700,710))
pygame.display.set_caption("Ghosts 'n Goblins")

# acteurs graphiques

hero1=pygame.image.load('hero2.png')
hero2=pygame.image.load('hero3.png')
fond=pygame.image.load('fond_GNG.bmp')
super=pygame.image.load('super.png')
echec=pygame.image.load('echec.png')
mechant1=pygame.image.load('dragon1.png')
mechant2=pygame.image.load('dragon2.png')
zombie1=pygame.image.load('zombie1.png')
zombie2=pygame.image.load('zombie2.png')

# sous fonctions

def victoire():
    surface.blit(super,(350,355))
    pygame.display.update()

def defaite():
    surface.blit(echec,(350,355))
    pygame.display.update()

# fonction principale

def principal():

    flag=False
    n=0
    run=True

    isjump = False
    v = 5
    m = 1

    x,y=10,45
    x_mvt,y_mvt=0,0
    xm,ym=350,300
    xm_mvt,ym_mvt=1,0

    while run:

        time.sleep(0.01)                    # temps de repos/rafraichissement de 10ms
        n+=1                                # pour que le mechant change de tete et deplacement au bout de 30 x 10 = 300ms
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run=False
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_LEFT:
                    x_mvt=-1
                if event.key==pygame.K_RIGHT:
                    x_mvt=1
                if event.key==pygame.K_UP:
                    if isjump == False:
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

                    pygame.time.delay(10)

            if event.type==pygame.KEYUP:
                x_mvt=0



        x+=x_mvt        # deplacement hero



        xm+=xm_mvt      # deplacement mechant

        # correction du deplacement si besoin

        if (xm<10) or (xm>260):      # le mechant reste dans le terrain mais traverse les murs !!!
            xm-=xm_mvt

        if (pixel_fond[x,y+65]==(153,153,153)):
            defaite()
            time.sleep(2)
            x,y=10,45
            xm,ym=350,300
            xm_mvt,ym_mvt=1,0

        if (pixel_fond[x+65,y]==(85,128,124)):                 # toucher  pixel= porte = victoire
            victoire()
            time.sleep(2)
            x,y=10,45
            xm,ym=350,300
            xm_mvt,ym_mvt=1,0

        if (pixel_fond[x,y+65]==(118,139,80)):
            y_mvt=0
        else:
            y_mvt=1

        if (abs(x-xm)<20) and (abs(y-ym)<15):                   # si collision mechant = defaite
            defaite()
            time.sleep(2)
            x,y=10,10
            xm,ym=350,300
            xm_mvt,ym_mvt=1,0

        # affichages des acteurs graphiques

        surface.blit(fond,(0,0))
        surface.blit(hero1,(x,y))

        if n>30:                                # 30x10ms=300ms histoire de faire alternner mechant1 et mechant2
            n=0
            flag=not(flag)                          # inversion du flag= True/False toutes les 300ms

        if(flag):                               # faire alternner mechant1 et mechant2
            surface.blit(mechant1,(xm,ym))
        else:
            surface.blit(mechant2,(xm,ym))

        pygame.display.update()                 # rafraichissement


principal()
pygame.quit()
quit()