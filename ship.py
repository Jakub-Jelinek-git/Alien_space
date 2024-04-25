import pygame

class Ship():
    """class of a ship"""
    def __init__(self,screen):
        """initializes the ship and starting position"""
        self.screen = screen

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

        #movemnt flags
        self.moving_right = False
        self.moving_left = False
    def update(self):
        """update sthe ship movement"""
        if self.moving_right:
            self.rect.centerx += 1
        if self.moving_left:
            self.rect.centerx += -1

    def blitme(self):
        """draws the ship at its current location"""
        self.screen.blit(self.image, self.rect)