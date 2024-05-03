import stat
import pygame
import game_functions as gf
from settings import Settings
from ship import Ship
from pygame.sprite import Group
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard

def load_game():
    """loads the game window"""
    #module needed to run the game
    pygame.init()
    clock = pygame.time.Clock()
    FPS = 30
    #initialize the settings
    g_settings = Settings()

    
    #creates an instanse of stats
    stats = GameStats(g_settings)

    #sets the creen size
    screen = pygame.display.set_mode((g_settings.screen_width, 
                                      g_settings.screen_height))
    #creates a group to store bullets
    bullet_group = Group()

    #creates a group of aliens
    alien_group = Group()
    
    # Make the Play button.
    play_button = Button(g_settings, screen, "Play")

    #shows the title on top of the screen
    pygame.display.set_caption("Alien Space","AS")   
    # create a scoreboard
    sb = Scoreboard(g_settings,screen,stats)

    #makes ship
    ship = Ship(screen,g_settings) 
    #create a fleet
    gf.create_alien_fleet(screen,g_settings,alien_group,ship)
    #start the main loop for the game
    while True:
        #event loop watching for mouse and keyboard movements
        gf.check_events(ship,screen,g_settings, bullet_group,stats,play_button,
                        alien_group)
        if stats.game_active:
            ship.update()
            gf.update_bullets(bullet_group, alien_group,g_settings,screen,ship)
            gf.update_aliens(alien_group,g_settings,bullet_group,screen,
                             ship,stats)
        gf.screen_unpdate(screen, g_settings, ship, alien_group, bullet_group, 
                          stats, play_button,sb)
        clock.tick(FPS)
load_game()