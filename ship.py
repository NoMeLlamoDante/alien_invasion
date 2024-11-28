import pygame

class Ship:
    """A class to amange the ship."""
    
    def __init__(self, ai_game):
        """Initialize the ship and set its starting position"""
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()
        
        # Load the ship image and get its rect
        self.image = pygame.image.load("images/ship.bmp")
        self.rect = self.image.get_rect()
        
        # Start each new ship at the botton center of the screen.
        self.rect.centery = self.screen_rect.centery
        
        # Store a float for the ship's exact horizontal position.
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        
        # Movement flag; start with a ship that's not moving
        self.moving_left = False
        self.moving_right = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        """Update the ship's position based on the moveemnt flag."""
        #Update the ship's x value, not the rect
        if self.moving_left:
            self.x -= self.settings.ship_speed
        if self.moving_right:
            self.x += self.settings.ship_speed
        if self.moving_up:
            self.y -= self.settings.ship_speed
        if self.moving_down:
            self.y += self.settings.ship_speed

        #Update rect object from self.x and self.y
        self.rect.x = self.x
        self.rect.y = self.y

    def blitme(self):
        """Draw the ship at its curent location."""
        self.screen.blit(self.image, self.rect)