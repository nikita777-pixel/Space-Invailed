"""Nikita Volodin from Russian!"""

# Import Library here:

import pygame
import sys

# Include project file here:

from settings import Settings # Import settings here.
from player import Player # Import Player here.
from enemy import Enemy # Import Enemy here.

settings = Settings() # Cretaed settings (Objects) |GLOBAL| here.

class Game:
    # Main class in this project'

    def __init__(self):
        # Construct here:

        pygame.init()
        pygame.mixer.init()

        self.Display = pygame.display.set_mode((settings.DISPLAY_WIDTH, settings.DISPLAY_HEIGHT))
        self.Screen = pygame.display.set_caption(settings.DISPLAY_TITLE)

    def main(self):
        # Main While and Main Objects here:

        # Created Objects here:

        hero = Player(self.Display) # Created Player (object) and Give Display Variable here.
        enemy = Enemy(self.Display) # Created Enemy (object) and Give Display Variable here.

        RunGame = True
        while RunGame: # Check if RunGame == True created main While here:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit() # Exit program here.



            self.Display.fill(settings.DISPLAY_COLOR) # Display draw to white color evry time

            # Write code here:

            hero.Draw_Player() # Created Draw Player here.
            enemy.Draw_Enemy()
            hero.Go_Player()
            enemy.Go_Enemy()

            pygame.display.update()
            pygame.display.flip()


game = Game() # Created game object
game.main() # Give from Object main method.
