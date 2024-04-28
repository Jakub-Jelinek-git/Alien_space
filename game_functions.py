"""all the functionality of the game"""
import sys
import pygame
from alien import Alien
from bullet import Bullet
def fire_bullet(event,game_settings,bullets,screen,ship):
    if event.key == 32 and game_settings.bullets_allowed >= len(bullets)+1:
        new_bullet = Bullet(game_settings,screen,ship)
        bullets.add(new_bullet)
def check_key_down_events(event,ship,game_settings,screen,bullets):
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_RIGHT:
            ship.moving_right = True
        elif event.key == pygame.K_LEFT:
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
    #updates bullet pos bullets
    for bullet in bullets.copy():
        if bullet.rect.bottom <=0:
            bullets.remove(bullet)
def draw_bullets(bullets):
    for bullet in bullets.sprites():
         bullet.draw_bullet()
def screen_unpdate(screen, settings, ship, aliens, bullets):
    #chenges the creen color each loop
        screen.fill(settings.bg_color)
        #draws ship
        ship.blitme()
        update_bullets(bullets)
        draw_bullets(bullets)
        for alien in aliens:
            alien.blitme()
        #draws the most recent screen with changes
        pygame.display.flip()
def get_number_aliens_x(game_settings, alien_width):
    """returs the number of aliens possible on the screen"""
    available_space = game_settings.screen_width - (alien_width * 2)
    number_aliens_x = int(available_space  / (alien_width * 2))
    return number_aliens_x
def create_allien(game_settings,screen,aliens,alien_number):
    alien = Alien(game_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.centerx = alien.x
    aliens.add(alien)
def create_alien_fleet(screen, game_settings, aliens):
    """creates a fleet of aliens based on screen width"""
    alien = Alien(game_settings, screen)
    number_aliens_x = get_number_aliens_x(game_settings,alien.rect.width)
    for alien_number in range(number_aliens_x):
        create_allien(game_settings,screen,aliens,alien_number)
        



        
        
        