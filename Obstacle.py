import pygame
from random import randint

class Obstacle(pygame.sprite.Sprite):
    def __init__(self,game, y_pos, flipped, isBottom=False):
        super().__init__()
        self.point = pygame.mixer.Sound(f'Assets/Sounds/sfx_point.mp3')
        self.point.set_volume(.2)
        self.spriteSheet = pygame.image.load(f"Assets/Tiles/Style 1/PipeStyle1.png").convert_alpha()
        pipe_image = pygame.transform.scale(self.getSprite(0,0,32,80),(128,640))
        # self.rect = self.image.get_rect(midbottom =(200,360))
        self.speed = 0
        self.isBottom = isBottom

        if flipped:
            pipe_image = pygame.transform.flip(pipe_image, False, True)

        self.image = pipe_image
        if flipped:
            self.rect = self.image.get_rect(midtop=(600, y_pos))
        else:
            self.rect = self.image.get_rect(midbottom=(600, y_pos))

 
    
    """
    x: top left x corner of sprite in sheet
    y: top left y corner of sprite in sheet
    width: width of sprite, px
    height: height of sprite, px
    """
    def getSprite(self, x, y, width, height):
        sprite = pygame.Surface((width,height), pygame.SRCALPHA)
        sprite.blit(self.spriteSheet, (0,0), (x,y,width,height))
        return sprite
    
    def move(self,game):
        self.speed = game.convertDelta(300)
        if self.rect.x <= -128:
            self.rect.x = 800
        self.rect.x -= self.speed
        pass

    def score(self,game):
        if self.rect.x <= -128 and self.isBottom:
            self.point.play()
            game.score += 1
        pass
        
    def update(self, game):
        self.move(game)
        self.score(game)