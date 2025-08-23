import initPygame
import pygame
import Player
import Obstacle
import Floor
from random import randint

def spawnObstacle(game):
    gap_size = -225
    gap_y = randint(100, 500)

    top_pipe = Obstacle.Obstacle(game, gap_y - gap_size//2, flipped=True, isBottom=False)
    bottom_pipe = Obstacle.Obstacle(game, gap_y + gap_size//2, flipped=False, isBottom=True)

    game.enemyGroup.add(top_pipe)
    game.enemyGroup.add(bottom_pipe)

def spawnFloor(game):
    game.floorGroup.add(Floor.Floor())

def start(game):
    """Background"""
    game.backgroundSurface = pygame.image.load("Assets/Background/Background1.png").convert_alpha()
    game.scaledBackground = pygame.transform.scale(game.backgroundSurface, (400,720))
    
    """Sound"""
    game.die = pygame.mixer.Sound(f'Assets/Sounds/sfx_die.mp3')
    game.die.set_volume(.2)
    game.backgroundMusic = pygame.mixer.Sound(f'Assets/Sounds/doors-elevator-music.mp3')
    game.backgroundMusic.set_volume(0.1)
    game.backgroundMusic.play(loops = -1)

    """Text"""
    game.Font = pygame.font.Font("./Pixeltype.ttf", 50)
    game.startTextSurface = game.Font.render("Press space to start\n        or LMB to start!", False, (255,255,255))
    game.startTextRect = game.startTextSurface.get_rect(center=(200,400))
    
    game.scoreSurface = game.Font.render("Score: 0", False, (255,255,255))
    game.scoreRect = game.startTextSurface.get_rect(center=(300,100))
    
    """Groups"""
    game.player = pygame.sprite.GroupSingle()
    game.player.add(Player.Player(game))

    game.enemyGroup = pygame.sprite.Group()
    game.floorGroup = pygame.sprite.Group()
    game.floorGroup.add(Floor.Floor(game))

    """Event"""
    game.onEvent("Spawn Obstacle", spawnObstacle)

    """Vars"""
    game.active = False
    game.over = False
    game.score = 0
    pass

def update(game, screen, keys, events):

    screen.blit(game.scaledBackground, (0,0))
    game.player.draw(screen)
    game.enemyGroup.draw(screen)
    game.floorGroup.draw(screen)

    if game.active:
        game.player.update(game)
        game.enemyGroup.update(game)
        game.scoreSurface = game.Font.render(f'Score: {game.score}', False, (255,255,255))

        screen.blit(game.scoreSurface, game.scoreRect)

        if pygame.sprite.spritecollide(game.player.sprite, game.enemyGroup, False):
            game.die.play()
            game.enemyGroup.empty()
            game.active = False
            game.over = True
    else:
        if game.over:
            game.startTextSurface = game.Font.render("Game Over!", False, (255,255,255))
            game.startTextRect = game.startTextSurface.get_rect(center=(200,360))
        if game.isKeyPressed(pygame.K_SPACE) or game.isMouseButtonDown(1):
            game.active = True
            game.over = False
            game.score = 0
            game.player.sprite.rect.midbottom = (75,360)
            game.player.sprite.gravity = 0
            game.enemyGroup.empty()
            game.onEvent("Spawn Obstacle", spawnObstacle)
        pass

        pygame.draw.rect(screen, "#b68728", game.startTextRect, border_radius=10)
        screen.blit(game.startTextSurface, game.startTextRect)
    pass

if '__main__' == __name__:
    screensize = (400,720)
    game = initPygame.InitPyGame(screensize, "Flappy Bird")
    game.onStart(start)
    game.gameloop(update)

    pass