import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
    """class of a ship"""
    def __init__(self,screen, game_settings):
        """initializes the ship and starting position"""
        super().__init__()
        self.screen = screen
        self.game_settings = game_settings

        #creates the ship from image and its shape (rectangle)
        self.image = pygame.image.load("sprites/Space-Invaders-Ship.bmp")

        # Set the size for the image
        DEFAULT_IMAGE_SIZE = (70, 90)
 
        # Scale the image to your needed size
        self.image = pygame.transform.scale(self.image, DEFAULT_IMAGE_SIZE)
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        
        #sets the position to bottom middle of the screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom =  self.screen_rect.bottom

        #stores a decimal value of the ship center/position
        self.center = float(self.rect.centerx)

        #movemnt flags
        self.moving_right = False
        self.moving_left = False
    def update(self):
        """update sthe ship movement"""
        #updates the ships center value not rect
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.game_settings.ship_speed_factor
        if self.moving_left and self.rect.left > self.screen_rect.left:
            self.center -= self.game_settings.ship_speed_factor
        
        #updates the ships rect value
        self.rect.centerx = self.center
        

    def blitme(self):
        """draws the ship at its current location"""
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """Center the ship on the screen."""
        self.center = self.screen_rect.centerx
