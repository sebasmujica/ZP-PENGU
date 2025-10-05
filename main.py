import pygame, sys
from pygame_config import*
from config import*
from player import Jugador, Laser
from mosquito import Mosquito
from explosion import Explosion
from avion import Avion


pygame.init()
pygame.display.set_caption("EL EXTERMINADOR")

screen = pantalla_config()
clock = clock_config()
running = True

fondo = pygame.image.load("imagenes/fondo_nivel_1.png").convert()
fondo = pygame.transform.scale(fondo,screen.get_size())

jugador = Jugador(screen_rect= screen.get_rect())

todos = pygame.sprite.GroupSingle()
todos.add(jugador)

grupo_mosquito = pygame.sprite.Group()

# Evento que se dispara cada 2 segundo
SPAWN_MOSQUITO = pygame.USEREVENT + 1 #EL +1 es para darle un ID unico al evento
pygame.time.set_timer(SPAWN_MOSQUITO, 2000)

grupo_explosion = pygame.sprite.Group()

grupo_avion = pygame.sprite.Group()

SPAWN_AVION = pygame.USEREVENT + 2
pygame.time.set_timer(SPAWN_AVION,10000)

while running:

    for event in pygame.event.get():
        #print(event)

        if event.type == pygame.QUIT:
            running = False
        elif event.type == SPAWN_MOSQUITO:
            mosquito = Mosquito()
            grupo_mosquito.add(mosquito)
        elif event.type ==  SPAWN_AVION:
            avion = Avion()
            grupo_avion.add(avion)


    #Updating
    todos.update()
    grupo_mosquito.update()
    grupo_explosion.update()
    grupo_avion.update()


    #Detecta colision
    hits = pygame.sprite.groupcollide(todos.sprite.lasers_group,grupo_mosquito, True,True)
    for _,enemigos_tocados in hits.items():
        for enemigo in enemigos_tocados:
            grupo_explosion.add(Explosion(
                enemigo.rect.center,
                size=(100,100)
            ))


    #Dibujar
    screen.blit(fondo,(0,0))
    todos.draw(screen)
    todos.sprite.lasers_group.draw(screen)
    grupo_avion.draw(screen)
    grupo_mosquito.draw(screen)
    grupo_explosion.draw(screen)


    pygame.display.flip()
    clock.tick(60)


pygame.quit()
sys.exit()