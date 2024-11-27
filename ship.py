import pygame

class Ship:
    """A class to amange the ship."""
    
    def __init__(self, ai_game):
        """Initialize the ship and set its starting position"""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        
        #Load the ship image and get its rect
        self.image = pygame.image.load("images/ship.bmp")
        self.rect = self.image.get_rect()
        
        #Start each new ship at the botton center of the screen.
        self.rect.centery = self.screen_rect.centery
        
    def blitme(self):
        """Draw the ship at its curent location."""
        self.screen.blit(self.image, self.rect)