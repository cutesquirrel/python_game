import pygame
import time

from PIL import Image

im = Image.open('fond1.bmp')
pixel_fond = im.load()

surface = pygame.display.set_mode((300,300))
pygame.display.set_caption("Merci le prof !")


hero=pygame.image.load('hero.png')
fond=pygame.image.load('fond1.bmp')
super=pygame.image.load('super.png')

def victoire():
    surface.blit(super,(50,50))
    pygame.display.update()

def principal():

    global game_over
    game_over=False

    x,y=10,10
    x_mvt,y_mvt=0,0

    while not game_over:
        time.sleep(0.01)
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



        x+=x_mvt
        y+=y_mvt

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

        surface.blit(fond,(0,0))
        surface.blit(hero,(x,y))

        pygame.display.update()

principal()
pygame.quit()
quit()