import pygame
from tiles import Tile
from player import Player
from settings import tile_size

class Level:
    def __init__(self, level_data, surface_to_draw):
        # level setup
        self.display_surface = surface_to_draw
        self.setup_level(level_data)
        self.world_shift = 0

    def setup_level(self, layout):  #layout will be lvel_data
        self.tiles = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()
        for row_index,row in enumerate(layout):
            for col_index,cell in enumerate(row):
                x = col_index * tile_size
                y = row_index * tile_size
                if cell == 'X':
                    tile = Tile((x,y),tile_size)    #position is tuple!
                    self.tiles.add(tile)
                if cell == 'P':
                    player_sprite = Player((x, y))  # position is tuple!
                    self.player.add(player_sprite)

    def run(self):
        # update tiles
        self.tiles.update(self.world_shift)    # scroll entire level to the right
        self.tiles.draw(self.display_surface)

        #update player
        self.player.update()
        self.player.draw(self.display_surface)
        pass