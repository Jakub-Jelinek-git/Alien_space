class Settings():
    """a class that stores all settings of the game"""
    def __init__(self):
        """initialize the game settings"""
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (100,100,100)
        self.caption = "Alien Space","AS"
        #bullet settings
        
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color =  (0,0,70)
        self.bullets_allowed = 3


        self.alien_drop_factor = 10
        
        # Ship settings
        self.ship_limit = 3

        # How quickly the game speeds up
        self.speedup_scale = 1.1
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Initialize settings that change throughout the game."""
        self.ship_speed_factor = 12
        self.bullet_speed = 18
        # fleet_direction of 1 represents right; -1 represents left.
        self.alien_direction = 1
        self.alien_speed_factor = 4
    
    def increase_speed(self):
        """Increase speed settings."""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale