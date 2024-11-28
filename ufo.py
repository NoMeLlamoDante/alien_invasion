import pygame
from pygame.sprite import Sprite

class Ufo(Sprite):
    """A class to represent a single alien in the fleet."""
    
    def __init__(self, ai_game):
        """Initialize the alien and set its starting position."""
        super().__init__()
        self.screen = ai_game.screen
        
        
        #Load the alien image and set its rect attribute.
        self.image = pygame.image.load("images/ufo_basic.bmp")
        
        self.rect = self.image.get_rect()
        
        #Start each new alien near the top right of the screen
        self.rect.x = self.screen.get_rect().width-self.rect.width
        self.rect.y = 0
        # self.rect.height
        
        #Store the alien's exact horizontal position
        self.x = float(self.rect.x)