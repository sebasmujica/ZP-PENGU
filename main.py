import pygame, sys
from pygame_config import*
from config import*
from player import Jugador, Laser
from mosquito import Mosquito
from explosion import Explosion
from avion import Avion, Avion_IAE
from power_up import PowerUp


pygame.init()
pygame.display.set_caption("EL EXTERMINADOR")

screen = pantalla_config()
clock = clock_config()
running = True

fondo = pygame.image.load("imagenes/fondo_nivel_1.png").convert()
fondo = pygame.transform.scale(fondo,screen.get_size())

jugador = Jugador(screen_rect= screen.get_rect())

grupo_jugador = pygame.sprite.GroupSingle()
grupo_jugador.add(jugador)

grupo_mosquito = pygame.sprite.Group()
grupo_power_up = pygame.sprite.Group()

# Evento que se dispara cada 2 segundo
spaw_mosquito_time = 2000
SPAWN_MOSQUITO = pygame.USEREVENT + 1 #EL +1 es para darle un ID unico al evento
pygame.time.set_timer(SPAWN_MOSQUITO, spaw_mosquito_time)

AUMENTAR_SPAWN_TIME = pygame.USEREVENT + 4
pygame.time.set_timer(AUMENTAR_SPAWN_TIME,15000)

grupo_explosion = pygame.sprite.Group()

grupo_avion = pygame.sprite.Group()

SPAWN_AVION = pygame.USEREVENT + 2
pygame.time.set_timer(SPAWN_AVION,10000)

SPAWN_AVION_IAE = pygame.USEREVENT + 3
pygame.time.set_timer(SPAWN_AVION_IAE,16000)

SUBIR_NIVEL = pygame.USEREVENT + 5
pygame.time.set_timer(SUBIR_NIVEL,10000)

SPAWN_POWER_UP = pygame.USEREVENT + 6
pygame.time.set_timer(SPAWN_POWER_UP,20000)


def dibujar_vidas(surface, vidas):
    fuente = pygame.font.SysFont(None, 28)
    txt = fuente.render(f"Vidas: {vidas}", True, (235, 235, 235))
    surface.blit(txt, (10, 10))

def dibujar_score(surface, score):
    fuente = pygame.font.SysFont(None, 28)
    txt = fuente.render(f"Score: {score}", True, (235,235,235))
    surface.blit(txt, (10, 30))

def dibujar_nivel(surface, nivel):
    fuente = pygame.font.SysFont(None, 28)
    txt = fuente.render(f"Nivel: {nivel}", True, (235,235,235))
    surface.blit(txt, (10, 50))



score = 1000
nivel_actual = 1

while running:
    j = grupo_jugador.sprite

    for event in pygame.event.get():
        #print(event)

        if event.type == pygame.QUIT:
            running = False
        elif event.type == SPAWN_MOSQUITO:
            for nivel in range(nivel_actual):
                mosquito = Mosquito()
                grupo_mosquito.add(mosquito)
        elif event.type ==  SPAWN_AVION:
            avion = Avion()
            grupo_avion.add(avion)
        elif event.type == SPAWN_AVION_IAE:
            avion = Avion_IAE()
            grupo_avion.add(avion)
        elif event.type == AUMENTAR_SPAWN_TIME:
            if spaw_mosquito_time > 0:
                spaw_mosquito_time -= 200
            else:
                spaw_mosquito_time = 1500
            print(spaw_mosquito_time)
        elif event.type == SUBIR_NIVEL:
            nivel_actual += 1
        elif event.type == SPAWN_POWER_UP:
            power_up = PowerUp()
            grupo_power_up.add(power_up)




    #Updating
    grupo_jugador.update()
    grupo_mosquito.update()
    grupo_explosion.update()
    grupo_avion.update()
    grupo_power_up.update()


    #Detecta colision
    hits = pygame.sprite.groupcollide(grupo_jugador.sprite.lasers_group,grupo_mosquito, True,True)
    for _,enemigos_tocados in hits.items():
        for enemigo in enemigos_tocados:
            score += 25
            grupo_explosion.add(Explosion(
                enemigo.rect.center,
                size=(100,100)
            ))
    
    if j:
        hit = pygame.sprite.spritecollide(j, grupo_mosquito, True, collided=pygame.sprite.collide_mask) 
        hit_power_up = pygame.sprite.spritecollide(j, grupo_power_up, True, collided=pygame.sprite.collide_mask) 
        if hit and not j.esta_invensible():
            j.recibir_daño()
        elif hit_power_up:
            j.laser_delay -= 50
            print("delay reducido", j.laser_delay)

    if j and j.vidas <= 0 or score <= 0:
        running = False

    for mosquito in grupo_mosquito:
        if mosquito.rect.top > ALTO_PANTALLA:
            score -= 50
            mosquito.kill()

    #Dibujar
    screen.blit(fondo,(0,0))

    if j and j.esta_invensible():
        if(pygame.time.get_ticks() // 100)%2 == 0:
            grupo_jugador.draw(screen)
    else:
        grupo_jugador.draw(screen)

    grupo_jugador.sprite.lasers_group.draw(screen)
    grupo_avion.draw(screen)
    grupo_power_up.draw(screen)
    grupo_mosquito.draw(screen)
    grupo_explosion.draw(screen)

    if j:
        dibujar_vidas(screen,j.vidas)
        dibujar_score(screen,score)
        dibujar_nivel(screen,nivel_actual)


    pygame.display.flip()
    clock.tick(60)


pygame.quit()
sys.exit()