from typing import Any
import pygame
from config import*
from laser import Laser  # Importing Laser from laser.py
VEL_JUG = 20
COOLDOWN = 300
INVENCIBLE = 1000

class Jugador(pygame.sprite.Sprite):
    def __init__(self, screen_rect: pygame.Rect, *groups) -> None:
        super().__init__(*groups)
        self.screen_rect = screen_rect
        self.image = pygame.image.load(str("imagenes/jugador.png")).convert_alpha()
        self.image = pygame.transform.scale(self.image, (80, 80))
        self.rect = self.image.get_rect(midbottom = (ANCHO_PANTALLA/2,ALTO_PANTALLA))
        self.vel = 5
        self.lasers_group = pygame.sprite.Group()
        self.laser_ready = True
        self.laser_time = 0
        self.laser_delay = 500
        self.vidas = 3
        self.inv_hasta = 0 

    def get_user_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and self.laser_ready:
            self.laser_ready = False
            laser = Laser(self.rect.center,5, ALTO_PANTALLA)
            self.lasers_group.add(laser)
            self.laser_time = pygame.time.get_ticks()
        dx = (keys[pygame.K_d])-(keys[pygame.K_a])
        self.rect.x += dx * VEL_JUG

    def update(self):
        self.get_user_input()
        self.rect.clamp_ip(self.screen_rect)
        self.lasers_group.update()
        self.recharge_laser()

    def recharge_laser(self):
        if not self.laser_ready:
            current_time = pygame.time.get_ticks()
            if current_time - self.laser_time >= self.laser_delay:
                self.laser_ready = True

    def recibir_daño(self):
        ahora = pygame.time.get_ticks()
        if ahora >= self.inv_hasta:
            self.vidas -= 1
            self.inv_hasta = ahora + INVENCIBLE

    def esta_invensible(self):
        return pygame.time.get_ticks()< self.inv_hasta