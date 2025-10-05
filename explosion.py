import pygame
class Explosion(pygame.sprite.Sprite):
    def __init__(self, center, size=None, duration = 200):
        super().__init__()
        img = pygame.image.load("imagenes/efecto_mosquito_muerto.png").convert_alpha()
        if size:  # p.ej. (128,128) o (192,192)
            img = pygame.transform.scale(img, size)
        self.image = img
        self.rect = self.image.get_rect(center=center)
        self.dead_at = pygame.time.get_ticks() + duration  # dura N ms

    def update(self):
        if pygame.time.get_ticks() >= self.dead_at:
            self.kill()
