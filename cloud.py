import pygame
from pygame.sprite import Sprite
from random import randint, choice

class Cloud(Sprite):
    """A class to represent a single cloud in the background."""
    
    def __init__(self, ai_game):
        """Initialize a cloud and set its starting position."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        
        # Load cloud image, scale random and set rect
        self.image = pygame.image.load("images/cloud.bmp")
        cloud_size = randint(1,6)
        self.image = pygame.transform.scale_by(self.image,factor=cloud_size*.4)
        self.rect = self.image.get_rect()
        
        # randomly start cloud
        random_x = randint(self.screen.get_rect().width,
                           int(self.screen.get_rect().width * 1.7))
        random_y = randint(self.rect.height, 
                            self.screen.get_rect().height - self.rect.height)
        self.rect.x = random_x
        self.rect.y = random_y
        
        # Store the cloud's exact horizontal position
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        
    def update(self):
        """Move the cloud over the screen"""
        # Update the exact position t the cloud
        self.x -= self.settings.bullet_speed
        # Update the rect position
        self.rect.x = self.x
        
    
    def blitme(self):
        """Draw the cloud to the screen"""
        self.screen.blit(self.image, self.rect)