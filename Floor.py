import pygame

class Floor(pygame.sprite.Sprite):
    def __init__(self, game):
        super().__init__()
        self.spriteSheet = pygame.image.load(f"Assets/Tiles/Style 1/SimpleStyle1.png").convert_alpha()
        # Extract the sprite from the sheet
        self.sprite = self.getSprite(0, 80, 16, 24)  # adjust to your actual sprite location
        # Scale it to desired floor width/height
        self.image = pygame.transform.scale(self.sprite, (400, 100))
        # Position at bottom of the screen
        self.rect = self.image.get_rect(midbottom=(200,750))

    def getSprite(self, x, y, width, height):
        sprite = pygame.Surface((width, height), pygame.SRCALPHA)
        sprite.blit(self.spriteSheet, (0, 0), (x, y, width, height))
        return sprite

    def update(self, game):
        # Static floor, nothing to update
        pass
