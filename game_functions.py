"""all the functionality of the game"""
import sys
import pygame
from bullet import Bullet
def fire_bullet(event,game_settings,bullets,screen,ship):
    if event.key == 32 and game_settings.bullets_allowed >= len(bullets)+1:
        new_bullet = Bullet(game_settings,screen,ship)
        bullets.add(new_bullet)
def check_key_down_events(event,ship,game_settings,screen,bullets):
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_RIGHT:
            ship.moving_right = True
        if event.key == pygame.K_LEFT:
            ship.moving_left = True
            fire_bullet(event,game_settings,bullets,screen,ship)
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
def update_bullets(bullets):
    bullets.update()
    #draws bullets
    for bullet in bullets.copy():
        if bullet.rect.bottom <=0:
            bullets.remove(bullet)
def screen_unpdate(screen, settings, ship, bullets):
    #chenges the creen color each loop
        screen.fill(settings.bg_color)
        #draws ship
        ship.blitme()
        for bullet in bullets.sprites():
            bullet.draw_bullet()
        #draws the most recent screen with changes
        pygame.display.flip()

        
        
        