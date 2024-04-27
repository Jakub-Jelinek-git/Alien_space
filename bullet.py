import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """bullet class"""
    def __init__(self, game_settings, screen, ship):
        """default values and inheritance"""
        super().__init__()
        self.screen = screen

        #creates the bullet at (0,0
        self.rect = pygame.Rect(0,0,game_settings.bullet_width,game_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top
        
        #stores the centery value as float(decimal)
        self.y = float(self.rect.y)
        #other
        self.color = game_settings.bullet_color
        self.speed = game_settings.bullet_speed
    def update(self):
        """updates the bullet position"""
        self.y -= self.speed
        self.rect.y = self.y
    def draw_bullet(self):
        """draws the bullet to the screen"""
        pygame.draw.rect(self.screen,self.color,self.rect)