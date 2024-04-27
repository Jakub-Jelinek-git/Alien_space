"""all the functionality of the game"""
import sys
import pygame
from bullet import Bullet
def check_key_down_events(event,ship,game_settings,screen,bullets):
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_RIGHT:
            ship.moving_right = True
        if event.key == pygame.K_LEFT:
            ship.moving_left = True
        if event.key == 32 and game_settings.bullets_allowed >= len(bullets)+1:
            new_bullet = Bullet(game_settings,screen,ship)
            bullets.add(new_bullet)
def check_key_up_events(event, ship):
    if event.type == pygame.KEYUP:
        if event.key == pygame.K_RIGHT:
            ship.moving_right = False
        if event.key == pygame.K_LEFT:
            ship.moving_left = False
def check_events(ship,screen,game_settings,bullets):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        check_key_down_events(event,ship,game_settings,screen,bullets)
        check_key_up_events(event,ship)
def screen_unpdate(screen, settings, ship, bullets):
    #chenges the creen color each loop
        screen.fill(settings.bg_color)
        #draws ship
        ship.blitme()
        #draws bullets
        for bullet in bullets.sprites():
            if bullet.rect.bottom <=0:
                bullets.remove(bullet)
            else:
                bullet.draw_bullet()
        
        #draws the most recent screen with changes
        pygame.display.flip()
        
        