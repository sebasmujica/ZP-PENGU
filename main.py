import pygame, sys
from pygame_config import*
from config import*
from player import Bala, Player



pygame.init()
pygame.display.set_caption("MAXI EL EXTERMINADOR")

screen = pantalla_config()
clock = clock_config()
running = True

fondo = pygame.image.load("imagenes/fondo_noche.jpg").convert()
fondo = pygame.transform.scale(fondo,screen.get_size())

jug_img = pygame.image.load("imagenes/Subject.png").convert_alpha()
jug_img = pygame.transform.rotozoom(jug_img,0,0.5)
jug_rect = jug_img.get_rect()

player = Player(screen.get_rect())

while running:

    for event in pygame.event.get():
        #print(event)

        if event.type == pygame.QUIT:
            running = False

        player.handle_input()
        player.update()


    screen.blit(fondo,(0,0))
    player.draw(screen)



    pygame.display.flip()
    clock.tick(60)


pygame.quit()
sys.exit()

