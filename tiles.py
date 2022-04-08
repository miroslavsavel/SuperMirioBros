import pygame

class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, size):
        super().__init__()
        self.image = pygame.Surface((size,size))
        self.rect

        pygame.draw.rect(DISPLAY, BLUE, (200, 150, 100, 50))