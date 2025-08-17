import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self,game):
        super().__init__()
        self.spriteSheet = pygame.image.load(f"Assets/Player/StyleBird2/Bird2-1.png").convert_alpha()

                # Slice into frames (1 row, 4 cols, each 16x16)
        self.frames = []
        for i in range(4):
            frame = self.getSprite(i * 16, 0, 16, 16)
            frame = pygame.transform.scale(frame, (64, 64))
            self.frames.append(frame)

        self.image = self.frames[0]
        self.rect = self.image.get_rect(midbottom=(75, 360))

        # Animation control
        self.frame_index = 0
        self.frame_time = 1 / 10  # 10 FPS animation speed
        self.time_accumulator = 0
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
            pass
        pass

    def applyGravity(self, game):
        self.gravity += 30
        self.rect.y += game.convertDelta(self.gravity)

        if self.rect.bottom >= 656:
            self.rect.bottom = 656
            game.active = False
            game.over = True
        pass

    def animationState(self,game):
        self.time_accumulator += game.convertDelta(.8)
        if self.time_accumulator >= self.frame_time:
            self.time_accumulator -= self.frame_time
            self.frame_index = (self.frame_index + 1) % len(self.frames)
            self.image = self.frames[self.frame_index]
        pass

    def update(self, game):
        self.playerInput(game)
        self.applyGravity(game)
        self.animationState(game)

        pass