import pygame

class Player:
    # Realization Hero here:

    def __init__(self, Display):
        # Construct here:

        self.Display = Display # init Display.

        # Download Image here:

        self.image = pygame.image.load("images/ship.bmp")
        self.rect = self.image.get_rect()
        self.screen_rect = Display.get_rect()

        # Created Cordinate ship here:

        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def Draw_Player(self):
        # Realization Draw Player here:

        self.Display.blit(self.image, self.rect)

    def Go_Player(self):
        # Realization Go Player here:

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.Check_If_Player_Left_Board() : # Check If hero click Left:
            self.Realization_Go_Player_Left()

        if keys[pygame.K_RIGHT] and self.Check_If_Player_Right_Board(): # Check if hero click Right:
            self.Realization_Go_Player_Right()

    def Realization_Go_Player_Left(self):
        self.rect.centerx -= 1

    def Realization_Go_Player_Right(self):
        self.rect.centerx += 1

    def Check_If_Player_Right_Board(self):
        """
        Check if Player > Board (Right) here
        :param: None
        :return: None
        """

        if self.rect.centerx < 1200 - 50:
            return True

    def Check_If_Player_Left_Board(self):
        """
        Check if player > Board (Left)
        :param: None
        :return: None
        """

        if self.rect.centerx > 5:
            return True

