"""all the functionality of the game"""
import sys
import pygame
from alien import Alien
from bullet import Bullet
from time import sleep

def fire_bullet(event,g_settings,bullets,screen,ship):
    if event.key == 32 and g_settings.bullets_allowed >= len(bullets)+1:
        new_bullet = Bullet(g_settings,screen,ship)
        bullets.add(new_bullet)

def check_key_down_events(event,ship,g_settings,screen,bullets):
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_RIGHT:
            ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            ship.moving_left = True
        fire_bullet(event,g_settings,bullets,screen,ship)

def check_key_up_events(event, ship):
    if event.type == pygame.KEYUP:
        if event.key == pygame.K_RIGHT:
            ship.moving_right = False
        if event.key == pygame.K_LEFT:
            ship.moving_left = False

def check_events(ship,screen,g_settings,bullets):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        check_key_down_events(event,ship,g_settings,screen,bullets)
        check_key_up_events(event,ship)

def update_bullets(bullets, aliens):
    bullets.update()
    #updates bullet pos bullets
    for bullet in bullets.copy():
        if bullet.rect.bottom <=0:
            bullets.remove(bullet)
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
def draw_bullets(bullets):

    for bullet in bullets.sprites():
         bullet.draw_bullet()

def screen_unpdate(screen, g_settings, ship, aliens, bullets):
    #chenges the creen color each loop
        screen.fill(g_settings.bg_color)
        #draws ship
        ship.blitme()
        draw_bullets(bullets)
        for alien in aliens:
            alien.blitme()
        #draws the most recent screen with changes
        pygame.display.flip()

def get_number_aliens_x(g_settings, alien_width):
    """returs the number of aliens possible on the screen"""
    available_space = g_settings.screen_width - (alien_width * 2)
    number_aliens_x = int(available_space  / (alien_width * 2))
    return number_aliens_x

def get_number_rows_y(g_settings,alien_height,ship_height):
    """returns the number of rows possible on thi spage"""
    space_available = (g_settings.screen_height - 
                        (alien_height * 3) - ship_height)
    number_of_rows = int(space_available / (alien_height * 2))
    return number_of_rows 

def create_allien(g_settings,screen,aliens,alien_number, rows_number):
    alien = Alien(g_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * rows_number 
    alien.rect.centerx = alien.x
    aliens.add(alien)

def create_alien_fleet(screen, g_settings, aliens, ship):
    """creates a fleet of aliens based on screen width"""
    alien = Alien(g_settings, screen)
    number_aliens_x = get_number_aliens_x(g_settings,alien.rect.width)
    number_of_rows = get_number_rows_y(g_settings,alien.rect.height,ship.rect.height)
    for row in range(number_of_rows):
        for alien_number in range(number_aliens_x):
            create_allien(g_settings,screen,aliens,alien_number,row)

def update_aliens(aliens,g_settings,bullets,screen,ship,stats):
    """Update the postions of all aliens in the fleet."""
    fleet_check_edges(aliens,g_settings)
    aliens.update()
    if len(aliens) == 0:
        # Destroy existing bullets and create new fleet.
        bullets.empty()
        create_alien_fleet(screen, g_settings, aliens,ship,)
    # Look for alien-ship collisions.
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(g_settings,stats,screen,ship,aliens,bullets)
        print("Ship hit!!!")



def fleet_check_edges(aliens,g_settings):
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(aliens,g_settings)
            break 

def change_fleet_direction(aliens, g_settings):
    for alien in aliens.sprites():
        alien.rect.y += g_settings.alien_drop_factor
    g_settings.alien_direction *= -1

def ship_hit(g_settings, stats, screen, ship, aliens, bullets):
    """Respond to ship being hit by alien."""
    # Decrement ships_left.
    stats.ships_left -= 1
    # Empty the list of aliens and bullets.
    aliens.empty()
    bullets.empty()
    # Create a new fleet and center the ship.
    create_alien_fleet( screen, g_settings,  aliens,ship,)
    ship.center_ship()
    # Pause.
    sleep(0.5)

        



        
        
        