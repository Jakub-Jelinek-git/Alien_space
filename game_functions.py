"""all the functionality of the game"""
import sys
import pygame

def check_events(ship):
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                        ship.moving_right = True
                if event.key == pygame.K_LEFT:
                        ship.moving_left = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                        ship.moving_right = False
                if event.key == pygame.K_LEFT:
                        ship.moving_left = False
def screen_unpdate(screen, settings, ship):
     #chenges the creen color each loop
        screen.fill(settings.bg_color)
        #draws ship
        ship.blitme()
        #draws the most recent screen with changes
        pygame.display.flip()