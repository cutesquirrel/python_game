# le hero doit aller chercher le cube bleu = (0,0,255)
# sans pouvoir passer sur un pixel noir = (0,0,0)

# sans se faire toucher par le mechant qui traverse les murs
#  mais reste dans le terrain

#  bibliotheques

import pygame
import time
import random

from PIL import Image

# preparation PIL pour lire pixel du fond1.bmp

im = Image.open('fond1.bmp')
pixel_fond = im.load()

# terrain de jeu

surface = pygame.display.set_mode((300,300))
pygame.display.set_caption("Merci le prof !")

# acteurs graphiques

hero=pygame.image.load('hero2.png')
fond=pygame.image.load('fond1.bmp')
super=pygame.image.load('super.png')
echec=pygame.image.load('echec.png')
mechant1=pygame.image.load('dragon1.png')
mechant2=pygame.image.load('dragon2.png')

# sous fonctions

def victoire():
    surface.blit(super,(50,50))
    pygame.display.update()

def defaite():
    surface.blit(echec,(50,50))
    pygame.display.update()

# fonction principale

def principal():

    flag=False
    n=0
    game_over=False

    x,y=10,10                                               # hero en 10,10
    x_mvt,y_mvt=0,0
    xm,ym=random.randint(10,200),random.randint(50,200)     # placement aleatoire du mechant
    xm_mvt,ym_mvt=1,0

    while not game_over:

        time.sleep(0.01)                    # temps de repos/rafraichissement de 10ms
        n+=1                                # pour que le mechant change de tete et deplacement au bout de 30 x 10 = 300ms
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                game_over=True

            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_LEFT:
                    x_mvt=-1
                if event.key==pygame.K_RIGHT:
                    x_mvt=1
                if event.key==pygame.K_UP:
                    y_mvt=-1
                if event.key==pygame.K_DOWN:
                    y_mvt=1
            if event.type==pygame.KEYUP:
                x_mvt=0
                y_mvt=0



        x+=x_mvt        # deplacement hero
        y+=y_mvt



        xm+=xm_mvt      # deplacement mechant
        ym+=ym_mvt

        # correction du deplacement si besoin

        if (xm<10) or (xm>260) or (ym<10) or (ym>260):      # le mechant reste dans le terrain mais traverse les murs !!!
            xm-=xm_mvt
            ym-=ym_mvt

        if (pixel_fond[x+20,y]==(0,0,0)) and (x_mvt==1):    # interdiction deplacement si pixel=noir
            x-=x_mvt
            y-=y_mvt
        if (pixel_fond[x,y]==(0,0,0)) and (x_mvt==-1):      # interdiction deplacement si pixel=noir
            x-=x_mvt
            y-=y_mvt
        if (pixel_fond[x,y+20]==(0,0,0)) and (y_mvt==1):    # interdiction deplacement si pixel=noir
            x-=x_mvt
            y-=y_mvt
        if (pixel_fond[x,y]==(0,0,0)) and (y_mvt==-1):      # interdiction deplacement si pixel=noir
            x-=x_mvt
            y-=y_mvt
        if (pixel_fond[x+20,y+20]==(0,0,0)) and (x_mvt==1):  # interdiction deplacement si pixel=noir
            x-=x_mvt
            y-=y_mvt
        if (pixel_fond[x,y+20]==(0,0,0)) and (x_mvt==-1):    # interdiction deplacement si pixel=noir
            x-=x_mvt
            y-=y_mvt

        if (pixel_fond[x+10,y]==(0,0,255)):                 # toucher  pixel=BLEU = victoire
            victoire()
            time.sleep(2)
            x,y=10,10
            xm,ym=10,220
            xm_mvt,ymmvt=1,0

        if (abs(x-xm)<20) and (abs(y-ym)<15):                   # si collision mechant = defaite
            defaite()
            time.sleep(2)
            x,y=10,10
            xm,ym=random.randint(10,200),random.randint(50,200)
            xm_mvt,ymmvt=1,0

        # affichages des acteurs graphiques

        surface.blit(fond,(0,0))
        surface.blit(hero,(x,y))

        if n>30:                                # 30x10ms=300ms histoire de faire alternner mechant1 et mechant2
            n=0
            flag=not(flag)                          # inversion du flag= True/False toutes les 300ms
            xm_mvt=(random.randint(0,1)*2)-1        #  deplacement  -1  ou +1
            ym_mvt=(random.randint(0,1)*2)-1        # le deplacement du mechant change aleatoirement toutes les 300ms

        if(flag):                               # faire alternner mechant1 et mechant2
            surface.blit(mechant1,(xm,ym))
        else:
            surface.blit(mechant2,(xm,ym))

        pygame.display.update()                 # rafraichissement

principal()
pygame.quit()
quit()