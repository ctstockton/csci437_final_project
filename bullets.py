#bullets.py
import pygame

#BULLET_IMAGE = "images/"

class Bullets(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(BULLET_IMAGE)
        self.image = self.image.convert_alpha()
        self.rect = self.image.get_rect()
