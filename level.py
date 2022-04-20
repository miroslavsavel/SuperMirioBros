import pygame
from tiles import Tile
from player import Player
from settings import tile_size
from settings import screen_width
#todo generate level string dynamically
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

    def scroll_x(self):
        player = self.player.sprite
        player_x = player.rect.centerx
        direction_x = player.direction.x

        # left side of the screen
        if player_x < screen_width / 4 and direction_x < 0:
            self.world_shift = 8
            player.speed = 0
        elif player_x > screen_width - (screen_width / 4) and direction_x > 0:
            self.world_shift = -8
            player.speed = 0
        else:
            self.world_shift = 0
            player.speed = 8

    def horizontal_movement_collision(self):
        player = self.player.sprite
        player.rect.x += player.direction.x * player.speed

        # look for collisions with all tiles
        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(player.rect):    # checking collision on the rect around sprite
                # figure out what direction is player moving
                if player.direction.x < 0: # we are moving right
                    player.rect.left = sprite.rect.right
                elif player.direction.x > 0:
                    player.rect.right = sprite.rect.left

    def vertical_movement_collision(self):
        player = self.player.sprite
        player.apply_gravity()

        # look for collisions with all tiles
        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(player.rect):    # checking collision on the rect around sprite
                # figure out if player moving up
                if player.direction.y > 0: # we are moving up
                    player.rect.bottom = sprite.rect.top
                    player.direction.y = 0
                elif player.direction.y < 0:    #player if moving down
                    player.rect.top = sprite.rect.bottom
                    player.direction.y = 0


    def run(self):
        # update tiles
        self.tiles.update(self.world_shift)    # scroll entire level to the right
        self.tiles.draw(self.display_surface)
        self.scroll_x()

        #update player
        self.player.update()
        self.horizontal_movement_collision()
        self.vertical_movement_collision()
        self.player.draw(self.display_surface)

        pass

