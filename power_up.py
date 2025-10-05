import pygame, random


class PowerUp(pygame.sprite.Sprite):
    def __init__(self) -> None:
        super().__init__()
        self.image = pygame.image.load("imagenes/repelente.png").convert_alpha()
        self.image = pygame.transform.scale(self.image,(80,80))

        # 📍 Zona visible del fondo
        self.limite_izq = 256
        self.limite_der = 1024


        # 🎯 Nacimiento dentro del rango del fondo (no en el aire lateral)
        pos_x = random.randint(self.limite_izq + 50, self.limite_der - 50)
        pos_y = random.randint(-150, -50)
        self.rect = self.image.get_rect(center=(pos_x, pos_y))

        # 🔄 Movimiento random
        self.velocidad_y = random.randint(2, 5)
        self.velocidad_x = random.choice([-1, 1]) * random.uniform(1, 2)

    def update(self):
        self.rect.y += self.velocidad_y
        self.rect.x += int(self.velocidad_x)

        # 🔁 Rebote lateral solo dentro del fondo visible
        if self.rect.left <= self.limite_izq or self.rect.right >= self.limite_der:
            self.velocidad_x *= -1

