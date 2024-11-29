class Settings:
    """A class to store all settings for Alien Invasion."""
    
    def __init__(self):
        """Initialize the game's settings"""
        # Screen Settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (215, 247, 253)
        
        # Ship settings
        self.ship_speed = 1.5
        
        # Bullet settings
        self.bullet_speed = 4.0
        self.bullet_width = 15
        self.bullet_height = 5
        self.bullet_color = (60, 60, 60)
        self.bullet_allowed = 3
        
        # Cloud Settings
        self.cloud_speed = 15.0
        self.cloud_limit = 5
        
        # Ufo settings
        self.ufo_speed = 1.0
        self.fleet_drop_speed = 10
        # fleet_direction of -1 represent up; 1 represent down
        self.fleet_direction = -1