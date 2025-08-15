import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        PATH = "FlappyBird/Assets"
        self.spriteSheet = pygame.image.load(f"{PATH}/Player/StyleBird2/Bird2-1.png").convert_alpha()
        print(self.spriteSheet.get_size())
        self.image = pygame.transform.scale(self.getSprite(0,0,16,16),(64,64))
        self.rect = self.image.get_rect(center =(200,360))

        self.gravity = 0
    
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

    def playerInput(self, game):
        if game.isKeyPressed(pygame.K_SPACE):
            self.gravity -= 1500
        pass

    def applyGravity(self, game):
        self.gravity += game.convertDelta(1500)
        self.rect.y += game.convertDelta(self.gravity)

        if self.rect.bottom >= 720:
            self.rect.bottom = 720
        pass

    def animationState(self):
        pass

    def update(self, game):
        self.playerInput(game)
        self.applyGravity(game)
        self.animationState()

        pass