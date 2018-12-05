#planet.py
import pygame
import random
import math
from bullet import bullet

PLAYER_IMAGE = "images/"
PLAYER_WIDTH = 256
PLAYER_HEIGHT = 256

class Player(pygame.sprite.Sprite):
    def __init__(self, bullets):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(PLAYER_IMAGE)
        self.image = self.image.convert_alpha()
        self.width = PLAYER_WIDTH
        self.height = PLAYER_HEIGHT
        self.rect = self.image.get_rect()
        self.x = 10
        self.y = 10
        self.angle = 0
        self.turretAngle = self.angle + 90
        self.center()
        self.bullets[5] = bullets

        self.CWspeed = 0
        self.startRad = 0
        self.planet_position_angle_deg = 0

    def spawn(self):
        #generate a place on the planet
        spawnDeg = random.random()*360
        #use the spawn degrees for angle on the planet

        #use angle to set x and y position

        #use angle to set angle of sprite

        #use angle of sprite to set angle of turret


    def fire(self):
        #checks array of bullets to find a hidden bullet
        for bullet in bullets:
            #fires a hidden bullet
            if(bullet.isHidden):
                bullet.fire(self.x, self.y, self.turretAngle)

    def checkCollision(self):
        #check the array of bullets

    def

    def update(self):
        #use radians to determine where the player is

        #use radians to determine the player's angle

        #use player's angle to set the angle of the turret
        self.rect.center = (self.x, self.y)
