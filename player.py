#planet.py
import pygame
import random
import math
from bullets import Bullets
from turret import Turret

PLAYER_IMAGE = "images/pixel-tank.png"
PLAYER_WIDTH = 256
PLAYER_HEIGHT = 256

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.imageMaster = pygame.image.load(PLAYER_IMAGE)
        self.imageMaster = pygame.image.load(PLAYER_IMAGE)
        self.imageMaster = self.imageMaster.convert_alpha()
        self.image = self.imageMaster
        self.width = PLAYER_WIDTH
        self.height = PLAYER_HEIGHT
        self.rect = self.image.get_rect()
        self.x = 10
        self.y = 10
        self.planetRadius = 300
        self.angle = 0
        self.turretAngle = self.angle + 90
        self.turret = Turret()
        #self.bullets[5] = bullets

        self.hitPoints = 10

        self.degSpeed = 0
        self.planet_position_angle_deg = 0

    def spawn(self):
        #generate a place on the planet
        spawnDeg = random.random()*360
        self.planet_position_angle_deg = spawnDeg
        #use angle to set x and y position
        self.x = self.planetRadius*math.cos(spawnDeg)+(1600/2)
        self.y = self.planetRadius*math.sin(spawnDeg)+(900/2)
        #use angle to set angle of sprite
        self.image = pygame.transform.rotate(self.imageMaster, spawnDeg)
        #use angle of sprite to set angle of turret

    def setPlayerPos(self):
        self.x = self.planetRadius*math.cos(self.planet_position_angle_deg)+(1600/2)
        self.y = self.planetRadius*math.sin(self.planet_position_angle_deg)+(900/2)

    def setPlayerAngle(self):
        dx = self.rect.centerx - 1600/2
        dy = self.rect.centery - 900/2
        try:
            imgAngle = math.atan(dy/dx)
        except:
            print("Can't divide by zero.")
            imgAngle = 0
        self.image = pygame.transform.rotate(self.imageMaster, imgAngle)
        self.rect = self.image.get_rect()

    def update(self):
        #use radians to determine where the player is
        self.planet_position_angle_deg += .005
        self.setPlayerPos()
        self.setPlayerAngle()
        #use radians to determine the player's angle

        #use player's angle to set the angle of the turret

        self.rect.center = (self.x, self.y)
'''
    def fire(self):
        #checks array of bullets to find a hidden bullet
        for bullet in bullets:
            #fires a hidden bullet
            if(bullet.isHidden):
                bullet.fire(self.x, self.y, self.turretAngle)

    #def checkCollision(self):
        #check the array of bullets
'''
