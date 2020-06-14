import pygame

class Enemy:
    # Realization Enemy here:

    def __init__(self, Display):
        # Construct here:

        self.Display = Display # Init Display here.

        # Download Enemy Image here:

        self.image = pygame.image.load("images/alien.bmp")
        self.rect = self.image.get_rect()
        self.screen_rect = Display.get_rect()

        # Created Cordinate alien here:

        self.X_ENEMY = 1200 / 2 - 50
        self.Y_ENEMY = 30

    def Draw_Enemy(self):
        # Realization Draw Enemy here:

        self.Display.blit(self.image, (self.X_ENEMY, self.Y_ENEMY))

    def Go_Enemy(self):
        # Realization Go Enemy here:

        pass

    def Attack_Enemy(self):
        # Realization Attack Enemy here:

        pass