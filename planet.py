#planet.py
import pygame

PLANET_IMAGE = "images/planet3.png"
PLANET_WIDTH = 600
PLANET_HEIGHT = 600

class Planet(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(PLANET_IMAGE)
        self.image = self.image.convert_alpha()
        self.width = PLANET_WIDTH
        self.height = PLANET_HEIGHT
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
        self.rect = self.image.get_rect()
        self.center()


    def center(self):
        self.rect.center = (1600/2, (900/2)+10)

    def update(self):
        self.center()
