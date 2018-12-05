################################################################################
#                               Space battle                                   #
#                       Corey Stockton, Thomas Angew                           #
#                               CSCI 43700                                     #
#                                11/27/18                                      #
################################################################################
import pygame
from planet import Planet
from player import Player

def main():
    pygame.init()
    screen = pygame.display.set_mode((1920,1080))
    pygame.display.set_caption("Space Battle")
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((255, 255, 255))
    screen.blit(background, (0, 0))

    #create planet and players
    planet = Planet()

    player1 = Player()
    player2 = Player()

    #group sprites
    planetSprite = pygame.Sprite.group(planet)
    playerSprites = pygame.Sprite.group(player1,player2)

    clock = pygame.time.Clock()
    keepGoing = True
    while keepGoing:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False
                
        #update sprites
        planetSprite.update()
        playerSprites.update()

        #draw sprites
        planetSprite.draw(screen)
        playerSprites.draw(screen)

if __name__ == "__main__":
    main()
