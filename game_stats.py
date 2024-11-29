class GameStats:
    """Track statistics for Alien invasion."""
    
    def __init__(self, aigame):
        """Initialize statistics."""
        self.settings = aigame.settings
        self.reset_stats()
    
    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.ships_left = self.settings.ship_limit
        