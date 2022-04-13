import pygame
from tiles import Tile
from settings import tile_size

class Level:
    def __init__(self, level_data, surface_to_draw):
        self.display_surface = surface_to_draw
        self.setup_level(level_data)

    def setup_level(self, layout):  #layout will be lvel_data
        self.tiles = pygame.sprite.Group()
        for row_index,row in enumerate(layout):
            for col_index,cell in enumerate(row):
                if cell == 'X':
                    x = col_index * tile_size
                    y = row_index * tile_size
                    tile = Tile((x,y),tile_size)    #position is tuple!
                    self.tiles.add(tile)

    def run(self):
        self.tiles.update(1)    # scroll entire level to the right
        self.tiles.draw(self.display_surface)
        pass