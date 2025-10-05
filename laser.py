import pygame

class Laser(pygame.sprite.Sprite):
    def __init__(self,posicion,speed,altura) -> None:
        super().__init__()
        self.image = pygame.image.load(str("imagenes/Muni.png"))
        self.image = pygame.transform.scale(self.image, (80,80))
        self.rect = self.image.get_rect(center = posicion)
        self.speed = speed
        self.altura = altura

    def update(self) -> None:
        self.rect.y -= self.speed
