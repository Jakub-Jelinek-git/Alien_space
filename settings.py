class Settings():
    """a class that stores all settings of the game"""
    def __init__(self):
        """initialize the game settings"""
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (250,250,250)
        self.caption = "Alien Space","AS"
        self.ship_speed_factor = 1.5
        #bullet settings
        
        self.bullet_speed = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color =  (0,0,70)
        self.bullets_allowed = 3
        
        