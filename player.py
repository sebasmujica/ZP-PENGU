import pygame

VEL_JUG = 20
COOLDOWN = 300
INVENCIBLE = 1200

class Bala:
    def __init__(self, x, y):
        self.img = pygame.image.load(str("imagenes/bala.png")).convert_alpha()
        self.rect = self.img.get_rect(midbottom=(x, y))
        self.vel_y = -9

    def update(self):
        self.rect.y += self.vel_y

    def draw(self, screen):
        screen.blit(self.img, self.rect)

    def fuera_de_pantalla(self):
        return self.rect.bottom < 0


class Player:
    def __init__(self, screen_rect: pygame.Rect) -> None:
        self.img = pygame.image.load("imagenes/Subject.png").convert_alpha()
        self.img = pygame.transform.rotozoom(self.img,0,0.5)
        self.rect = self.img.get_rect(midbottom=(screen_rect.centerx, screen_rect.bottom - 20))
        self.vel = VEL_JUG
        self.vidas = 3
        self.ultimo_disparo = -9999
        self.invencible_hasta = 0
        self.bala_activa = None
        self.screen_rect = screen_rect

    def handle_input(self):
        keys = pygame.key.get_pressed()
        dx  = (keys[pygame.K_RIGHT] or keys[pygame.K_d]) - (keys[pygame.K_LEFT] or keys[pygame.K_a])
        self.rect.x += dx * VEL_JUG
        self.rect.clamp_ip(self.screen_rect)

        ahora = pygame.time.get_ticks()
        if keys[pygame.K_SPACE] and self.bala_activa is None:
            if (ahora - self.ultimo_disparo) >= COOLDOWN:
                #Se crea una bala en la parte superior central del jugador
                self.bala_activa = Bala(self.rect.centerx, self.rect.top)
                self.ultimo_disparo = ahora

    def update(self):
        # actualizar bala si existe
        if self.bala_activa:
            self.bala_activa.update()
            if self.bala_activa.fuera_de_pantalla():
                self.bala_activa = None

    def draw(self, screen):
        # efecto simple: parpadear si invencible
        ahora = pygame.time.get_ticks()
        if ahora < self.invencible_hasta:
            # dibuja 1 frame sí / 1 no
            if (ahora // 100) % 2 == 0:
                screen.blit(self.img, self.rect)
        else:
            screen.blit(self.img, self.rect)

        if self.bala_activa:
            self.bala_activa.draw(screen)

    def recibir_daño(self):
        ahora = pygame.time.get_ticks()
        if ahora >= self.invencible_hasta:  # no recibe daño si invencible
            self.vidas -= 1
            self.invencible_hasta = ahora + INVENCIBLE