################################################################################
#                               Space battle                                   #
#                       Corey Stockton, Thomas Angew                           #
#                               CSCI 43700                                     #
#                                11/27/18                                      #
################################################################################
import pygame
from background import Background
from planet import Planet
from player import Player
from bullets import Bullets

def main():
    pygame.init()
    screen = pygame.display.set_mode((1600,900))
    pygame.display.set_caption("Space Battle")
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((255, 255, 255))
    screen.blit(background, (0, 0))

    #create a back drop image
    backdrop = Background()

    #create planet and players
    planet = Planet()

    #p1Bullets = Bullets()
    #p2Bullets = Bullets()

    player1 = Player()
    #player2 = Player(p2Bullets)

    player1.spawn()

    #group sprites
    backdropSprite = pygame.sprite.Group(backdrop)
    planetSprite = pygame.sprite.Group(planet)
    playerSprites = pygame.sprite.Group(player1) #,player2

    clock = pygame.time.Clock()
    keepGoing = True
    while keepGoing:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False

        #update sprites
        backdropSprite.update()
        planetSprite.update()
        playerSprites.update()

        #draw sprites
        backdropSprite.draw(screen)
        planetSprite.draw(screen)
        playerSprites.draw(screen)

        pygame.display.flip()

if __name__ == "__main__":
    main()
