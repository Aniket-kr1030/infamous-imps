import pygame
from config import *

class Life(pygame.sprite.Sprite):
    def __init__(self, game, x,y):
        self.game = game
        self._layer = PLAYER_LAYER
        self.groups =  self.game.all_sprites, self.game.pickups
        pygame.sprite.Sprite.__init__(self,self.groups)
        self.x = x*TILE_SIZE
        self.y = y*TILE_SIZE
        self.width = TILE_SIZE
        self.height = TILE_SIZE
        self.image = pygame.Surface([self.width, self.height])
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y =  self.y

