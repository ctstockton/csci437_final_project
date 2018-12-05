#planet.py
import pygame
import random
import math

PLAYER_IMAGE = "images/"
PLAYER_WIDTH = 256
PLAYER_HEIGHT = 256

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(PLAYER_IMAGE)
        self.image = self.image.convert_alpha()
        self.width = PLAYER_WIDTH
        self.height = PLAYER_HEIGHT
        self.rect = self.image.get_rect()
        self.x = 10
        self.y = 10
        self.center()

        self.CWspeed = 0
        self.startRad = 0
        self.maxRad = 1 #change this later
        self.

    def spawn(self):
        spawnRad = random.randrange(0, 2*PI, .01)

    def update(self):
        self.rect.center = (self.x, self.y)
