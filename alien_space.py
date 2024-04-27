import pygame
import sys
import game_functions as gf
from settings import Settings
from ship import Ship
from pygame.sprite import Group

def load_game():
    """loads the game window"""
    #module needed to run the game
    pygame.init()

    #initialize the settings
    game_settings = Settings()

    #sets the creen size
    screen = pygame.display.set_mode((game_settings.screen_width,
                                      game_settings.screen_height))
    #creates a group to store bullets
    bullet_group = Group()

    #shows the title on top of the screen
    pygame.display.set_caption("Alien Space","AS")   

    #makes ship
    ship = Ship(screen,game_settings) 
    
    #start the main loop for the game
    while True:
        
        #event loop watching for mouse and keyboard movements
        gf.check_events(ship,screen,game_settings, bullet_group)
        bullet_group.update()
        gf.screen_unpdate(screen,game_settings,ship,bullet_group)
        ship.update()
load_game()