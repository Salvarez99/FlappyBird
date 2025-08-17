import initPygame
import pygame
import Player

def start(game):
    """Background"""
    game.backgroundSurface = pygame.image.load("Assets/Background/Background1.png").convert_alpha()
    game.scaledBackground = pygame.transform.scale(game.backgroundSurface, (400,720))
    
    """Text"""
    game.Font = pygame.font.Font("./Pixeltype.ttf", 50)
    game.startTextSurface = game.Font.render("Press space to start!", False, (0,0,0))
    game.startTextRect = game.startTextSurface.get_rect(center=(200,400))
    """Groups"""
    game.player = pygame.sprite.GroupSingle()
    game.player.add(Player.Player(game))

    game.active = False
    pass

def update(game, screen, keys, events):

    screen.blit(game.scaledBackground, (0,0))
    game.player.draw(screen)

    if game.active:
        game.player.update(game)
    else:
        screen.blit(game.startTextSurface, game.startTextRect)
        
        if game.isKeyPressed(pygame.K_SPACE) or game.isMouseButtonDown(1):
            game.active = True
        pass
    pass

if '__main__' == __name__:
    screensize = (400,720)
    game = initPygame.InitPyGame(screensize, "Flappy Bird")
    game.onStart(start)
    game.gameloop(update)

    pass