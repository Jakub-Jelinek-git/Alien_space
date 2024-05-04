import pygame.font
from pygame.sprite import Group
from ship import Ship
import json
class Scoreboard():
    """simple scrore board for the game"""
    def __init__(self,g_settings,screen,stats):
        """initializes the base values of the class"""
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.g_settings = g_settings
        self.stats = stats
        self.high_score = stats.high_score
        # Font settings for scoring information.
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)
        
        # Prepare the initial score image.
        self.prep_score()
        self.h_s()
        self.prep_high_score(stats)
        self.prep_level()
        self.prep_ships()
    def h_s(self):
        self.filename = 'high_score.json'
        print(self.high_score)
        hso = 0
        try:
            with open(self.filename) as f_obj:
                hso = json.load(f_obj)
                if hso > self.high_score:
                    self.high_score = int(round(hso,-1))
                else:
                    self.high_score = int(round(self.stats.high_score, -1))
        except FileNotFoundError:
            with open(self.filename, 'w') as f_obj:
                self.high_score = int(round(self.stats.high_score, -1))
                json.dump(self.high_score, f_obj)
        if hso < self.high_score:
            with open(self.filename, 'w') as f_obj:
                json.dump(self.high_score, f_obj)
            
    

    def prep_high_score(self,stats):
        """Turn the high score into a rendered image."""
        
        if self.high_score < stats.score:
            self.high_score = stats.score
        self.high_score_str = "{:,}".format(self.high_score)
        self.high_score_image = self.font.render(self.high_score_str, True,
            self.text_color, self.g_settings.bg_color)
        # Center the high score at the top of the screen.
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top

    def prep_score(self):
        """Turn the score into a rendered image."""
        rounded_score = int(round(self.stats.score, -1))
        score_str = "{:,}".format(rounded_score)
        self.score_image = self.font.render(score_str, True, self.text_color,
                                            self.g_settings.bg_color)
        # Display the score at the top right of the screen.
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def prep_level(self):
        """Turn the level into a rendered image."""
        self.level_image = self.font.render(str(self.stats.level), True,
                self.text_color, self.g_settings.bg_color)
        # Position the level below the score.
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10
    
    def prep_ships(self):
        """Show how many ships are left."""
        self.ships = Group()
        for ship_number in range(self.stats.ships_left):
            ship = Ship( self.screen,self.g_settings,)
            ship.rect.x = 10 + ship_number * ship.rect.width
            ship.rect.y = 10
            self.ships.add(ship)

    def show_score(self):
        """Draw score to the screen."""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        # Draw ships.
        self.ships.draw(self.screen)