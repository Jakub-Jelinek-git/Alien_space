"""all the functionality of the game"""
import sys
import pygame
def check_key_down_events(event,ship):
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_RIGHT:
            ship.moving_right = True
        if event.key == pygame.K_LEFT:
            ship.moving_left = True
def check_key_up_events(event, ship):
    if event.type == pygame.KEYUP:
        if event.key == pygame.K_RIGHT:
            ship.moving_right = False
        if event.key == pygame.K_LEFT:
            ship.moving_left = False
def check_events(ship):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        check_key_down_events(event,ship)
        check_key_up_events(event,ship)
def screen_unpdate(screen, settings, ship):
     #chenges the creen color each loop
        screen.fill(settings.bg_color)
        #draws ship
        ship.blitme()
        #draws the most recent screen with changes
        pygame.display.flip()