
import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """class of a alien"""
    def __init__(self,game_settings,screen):
        """initiates the alien"""
        super().__init__()
        self.settings = game_settings
        self.screen = screen
        DEFAULT_IMAGE_SIZE = (70, 60)
 
        # Scale the image to your needed size
        
        self.image = pygame.image.load("sprites/Space-Invaders-Alien-PNG-Image.bmp")
        self.image = pygame.transform.scale(self.image, DEFAULT_IMAGE_SIZE)
        self.rect = self.image.get_rect()

        #starts the alien at position near  a top corner
        self.rect.centerx = self.rect.height
        self.rect.centery = self.rect.width

        self.x = float(self.rect.centerx)

    def update(self):
        """updates the alien postion"""
        self.x += self.settings.alien_speed_factor * self.settings.alien_direction
        self.rect.centerx = self.x

    def check_edges(self):
        screen_rect = self.screen.get_rect()
        if self.rect.left <= 0:
            return True
        elif self.rect.right >= screen_rect.right:
            return True
         
    def blitme(self):
        """draws the alien on the screen"""
        self.screen.blit(self.image, self.rect)

      