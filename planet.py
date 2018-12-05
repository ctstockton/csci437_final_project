#planet.py
import pygame

PLANET_IMAGE = "images/planet.png"
PLANET_WIDTH = 256
PLANET_HEIGHT = 256

class Planet(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(PLANET_IMAGE)
        self.image = self.image.convert_alpha()
        self.width = PLANET_WIDTH
        self.height = PLANET_HEIGHT
        self.rect = self.image.get_rect()
        self.center()

    def center(self):
        self.rect.center = (self.width/2, self.height/2)

    def update(self):
        self.center()
