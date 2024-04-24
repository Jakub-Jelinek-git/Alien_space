import pygame
import sys
from settings import Settings
from ship import Ship
def load_game():
    """loads the game window"""
    #module needed to run the game
    pygame.init()

    #initialize the settings
    game_settings = Settings()

    #sets the creen size
    screen = pygame.display.set_mode((game_settings.screen_width,
                                      game_settings.screen_height))
    
    #shows the title on top of the screen
    pygame.display.set_caption("Alien Space","AS")   

    #makes ship
    ship = Ship(screen) 
    
    #start the main loop for the game
    while True:
        
        #event loop watching for mouse and keyboard movements
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        #chenges the creen color each loop
        screen.fill(game_settings.bg_color)
        #draws ship
        ship.blitme()
        #draws the most recent screen with changes
        pygame.display.flip()
load_game()