import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self,game):
        super().__init__()
        self.spriteSheet = pygame.image.load(f"Assets/Player/StyleBird2/Bird2-1.png").convert_alpha()
        self.image = pygame.transform.scale(self.getSprite(0,0,16,16),(64,64))
        self.rect = self.image.get_rect(midbottom =(75,360))

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
        if game.isKeyPressed(pygame.K_SPACE) or game.isMouseButtonDown(1):
            self.gravity = -700
            print("Jump")
            print(f"y-pos: {self.rect.bottom}")

            pass
        pass

    def applyGravity(self, game):
        self.gravity += 30
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