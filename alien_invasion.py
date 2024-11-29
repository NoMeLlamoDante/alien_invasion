import sys
from time import sleep

import pygame

from settings import Settings
from game_stats import GameStats
from ship import Ship
from bullet import Bullet
from ufo import Ufo
from cloud import Cloud

class AlienInvasion:
    """Overall class to manage game assets and behavior."""
    
    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()
        
        # Screen settings
        # activate full screen
        # self.screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width,self.settings.screen_height))
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Alien Invasion")
        
        #Create an instance to store game statistics.
        self.stats = GameStats(self)
        
        #Items
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.ufos = pygame.sprite.Group()
        
        self.clouds = pygame.sprite.Group()
        self._create_fleet()
        
    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()
            self._update_clouds()
            self.ship.update()
            self._update_ufo()
            self._update_bullets()
            self._update_screen()
            self.clock.tick(60)
    
    # Events
    def _check_events(self):
        # Respond to keypresses and mouse events.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
                    
            elif event.type == pygame.KEYUP:
                self._check__keyup_events(event)

    def _check_keydown_events(self, event):
        """Respond to keypresses."""
        if event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_UP:
            self.ship.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check__keyup_events(self, event):
        """Respont to key releases."""
        if event.key == pygame.K_LEFT:
            self.ship.moving_left = False
        elif event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_UP:
            self.ship.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = False

    # Clouds
    def _generate_clouds(self):
        """Create a cloud and place it"""
        if len(self.clouds) < self.settings.cloud_limit:
            new_cloud = Cloud(self)
            self.clouds.add(new_cloud)
    
    def _update_clouds(self):
        """Update position of clouds and get rid of old clouds"""
        self._generate_clouds()
        #Update Clouds position
        self.clouds.update()
        #Get rid of clouds that have disappeared
        for cloud in self.clouds.copy():
            if cloud.rect.x <= 0 - cloud.rect.width:
                self.clouds.remove(cloud)
    
    # Ship
    def _shit_hit(self):
        """Respond to the ship being hit by a ufo"""
        # Decrement ships_left
        self.stats.ships_left -= 1
        # Get rid of any remaining bullets and ufos.
        self.bullets.empty()
        self.ufos.empty()
        
        # Create a new fleet and center the ship.
        self._create_fleet()
        self.ship.center_ship()
        
        # Pause
        sleep(0.5)
    
    # Bullets
    def _fire_bullet(self):
        """Create a new bullet and add it to the bullet group."""
        if len(self.bullets) < self.settings.bullet_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)
    
    def _update_bullets(self):
        """Update position of bullets and get rid of old bullets."""
        #Update bullets positions.
        self.bullets.update()
        #Get rid of bullet that have disappeared
        for bullet in self.bullets.copy():
            if bullet.rect.x >= self.settings.screen_width:
                self.bullets.remove(bullet)
        
        self._check_bullet_ufo_collision()
    
    def _check_bullet_ufo_collision(self):
        """Respot to bullet-alien_collision. """
        # Remove any bullets and ufo that have collided.
        collisions = pygame.sprite.groupcollide(
            self.bullets, self.ufos,True, True)
        if not self.ufos:
            # Destroy existing bullets and create new fleet.
            self.bullets.empty()
            self._create_fleet()
    
    # Ufos
    def _create_fleet(self):
        """Create the fleet of aliens."""
        # Make a ufo and keep adding ufos until there's no room left.
        # Space between ufo is one ufo height.
        ufo = Ufo(self)
        ufo_width, ufo_height = ufo.rect.size
        current_x,  current_y = self.settings.screen_width-ufo_width, ufo_height
        while current_x > (5 * ufo_width):
            while current_y < (self.settings.screen_height - 2 * ufo_height):
                self._create_ufo(current_x, current_y)
                current_y += 2 * ufo_height
            # Finished a column; reset y value, and increment x value.
            current_y = ufo_height
            current_x -= 1.5 * ufo_width
            
    def _create_ufo(self, x_position, y_position):
        """Create a Ufo and place it in the row"""
        new_ufo = Ufo(self)
        new_ufo.y = y_position
        new_ufo.rect.y = y_position
        new_ufo.rect.x = x_position
        self.ufos.add(new_ufo)
    
    def _update_ufo(self):
        """Check if the fleet is at an edge, then update positions"""
        self._check_fleet_edges()
        
        self.ufos.update()
        
        # Look for ufo-ship collisions.
        if pygame.sprite.spritecollideany(self.ship, self.ufos):
            self._shit_hit()

        #Look for ufo hitting the left of the screen
        self._check_ufos_left()
    
    def _check_fleet_edges(self):
        """Respond appropriately if any ufo have reached an edge."""
        for ufo in self.ufos.sprites():
            if ufo.check_edges():
                self._change_fleet_direction()
                break
    
    def _change_fleet_direction(self):
        """Drop the entire fleet and change the fleet's direction."""
        for ufo in self.ufos.sprites():
            ufo.rect.x -= self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1
    
    def _check_ufos_left(self):
        """Check if any ufo have reached the bottom of the screen."""
        for ufo in self.ufos.sprites():
            if ufo.rect.left <= 0:
                # Treat this the same as if the ship got hit.
                self._shit_hit()
                break
    
    # Screen
    def _update_screen(self):
        # Update images on the screen, and flipto the new screen
        self.screen.fill(self.settings.bg_color)
        for cloud in self.clouds.sprites():
            cloud.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.ship.blitme()
        self.ufos.draw(self.screen)
        
        pygame.display.flip()

if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()