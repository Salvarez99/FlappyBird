import initPygame
import pygame
import Player

def start(game):
    """Background"""
    game.backgroundSurface = pygame.image.load("Assets/Background/Background1.png").convert_alpha()
    game.scaledBackground = pygame.transform.scale(game.backgroundSurface, (400,720))
    
    """Groups"""
    game.player = pygame.sprite.GroupSingle()
    game.player.add(Player.Player())
    pass

def update(game, screen, keys, events):
    screen.blit(game.scaledBackground, (0,0))
    game.player.draw(screen)
    game.player.update(game)
    pass

if '__main__' == __name__:
    screensize = (400,720)
    game = initPygame.InitPyGame(screensize, "Flappy Bird")
    game.onStart(start)
    game.gameloop(update)

    pass