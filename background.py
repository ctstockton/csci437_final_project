#background.py
import pygame

BACKGROUND_IMAGE = "images/background.jpg"
BACKGROUND_WIDTH = 1920
BACKGROUND_HEIGHT = 1080

class Background(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(BACKGROUND_IMAGE)
        self.image = self.image.convert_alpha()
        self.width = BACKGROUND_WIDTH
        self.height = BACKGROUND_HEIGHT
        self.rect = self.image.get_rect()
        self.center()

    def center(self):
        self.rect.center = (self.width/2, self.height/2)

    def update(self):
        self.center()
