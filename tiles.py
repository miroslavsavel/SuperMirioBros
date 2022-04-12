import pygame

class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, size):      # position of tile and the size of tile are params
        super().__init__()
        self.image = pygame.Surface((size,size))
        self.image.fill('grey')
        self.rect = self.image.get_rect(topleft = pos)

        # pygame.draw.rect(DISPLAY, BLUE, (200, 150, 100, 50))