import pygame
from support import import_folder

class Player(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.import_character_assets()
        self.frame_index = 0
        self.animation_speed = 0.15
        # self.image = pygame.Surface((32,64))
        # self.image.fill('red')
        self.image = self.animations['idle'][self.frame_index]


        self.rect = self.image.get_rect(topleft = pos)

        # player movement
        self.direction = pygame.math.Vector2(0,0)
        self.speed = 8
        self.gravity = 0.8
        self.jump_speed = -16   # negative because I want to jump up

    """player animation"""
    def import_character_assets(self):
        # path to folder with animations
        character_path ='./graphics/character/'
        # there are folders for idle, run, jump etc..
        self.animations = {'idle':[], 'run':[],'jump':[],'fall':[]}

        for animation in self.animations.keys():
            full_path = character_path + animation
            self.animations[animation] = import_folder(full_path)

    def get_input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT]:
            self.direction.x = 1
            pass
        elif keys[pygame.K_LEFT]:
            self.direction.x = -1
            pass
        else:
            self.direction.x = 0
            pass
        if keys[pygame.K_SPACE]:
            self.jump()

    def apply_gravity(self):
        self.direction.y += self.gravity
        self.rect.y += self.direction.y

    """Method for counter acting gravity force"""
    def jump(self):
        self.direction.y = self.jump_speed

    def update(self):
        self.get_input()
        # self.rect.x += self.direction.x * self.speed  # separate because we want detect horizontal collisions
        # self.apply_gravity()  # moved to the level class