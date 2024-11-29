import pygame
from pygame.sprite import Sprite

class Ufo(Sprite):
    """A class to represent a single ufo in the fleet."""
    
    def __init__(self, ai_game):
        """Initialize the ufo and set its starting position."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        
        #Load the ufo image and set its rect attribute.
        self.image = pygame.image.load("images/ufo_basic.bmp")
        
        self.rect = self.image.get_rect()
        
        #Start each new ufo near the top right of the screen
        self.rect.x = self.screen.get_rect().width-self.rect.width
        self.rect.y = 0
        # self.rect.height
        
        #Store the ufo's exact horizontal position
        self.x = float(self.rect.x)
    
    def check_edges(self):
        """Return True if ufo is at edge of screen. """
        screen_rect = self.screen.get_rect()
        return (self.rect.bottom >= screen_rect.bottom) or (self.rect.top <= 0)
    
    def update(self):
        """Move the ufo to up."""
        self.y += self.settings.ufo_speed * self.settings.fleet_direction
        self.rect.y = self.y