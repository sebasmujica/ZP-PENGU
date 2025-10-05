
import pygame


class Avion(pygame.sprite.Sprite):
    def __init__(self) -> None:
        super().__init__()
        self.image = pygame.image.load("imagenes/avion_narco.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (80,80))
        self.rect = self.image.get_rect(center = (0,100))
        self.speed = 5
    
    def update(self) -> None:
        self.rect.x += self.speed
