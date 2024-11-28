class Settings:
    """A class to store all settings for Alien Invasion."""
    
    def __init__(self):
        """Initialize the game's settings"""
        #Screen Settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (215, 247, 253)
        
        #Ship settings
        self.ship_speed = 1.5
        
        #Bullet settings
        self.bullet_speed = 2.0
        self.bullet_width = 15
        self.bullet_height = 5
        self.bullet_color = (60, 60, 60)
        self.bullet_allowed = 3