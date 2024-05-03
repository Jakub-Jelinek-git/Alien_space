"""all the functionality of the game"""
import sys
from threading import stack_size
import pygame
from alien import Alien
from bullet import Bullet
from time import sleep

def fire_bullet(event,g_settings,bullets,screen,ship,stats):
    if event.key == 32 and g_settings.bullets_allowed >= len(bullets)+1 and stats.game_active:
        new_bullet = Bullet(g_settings,screen,ship)
        bullets.add(new_bullet)

def check_key_down_events(event,ship,g_settings,screen,bullets,stats,play_button,aliens,):
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_RIGHT:
            ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            ship.moving_left = True
        elif (event.key == pygame.K_p) and not (stats.game_active):
            start_game(stats,aliens,bullets,ship,screen,g_settings)
        fire_bullet(event,g_settings,bullets,screen,ship,stats)
        

    if event.type == pygame.MOUSEBUTTONDOWN:
        mouse_x, mouse_y = pygame.mouse.get_pos()
        check_play_button(stats, play_button, mouse_x, mouse_y,g_settings,
                          aliens,bullets,screen,ship)
    
def check_key_up_events(event, ship):
    if event.type == pygame.KEYUP:
        if event.key == pygame.K_RIGHT:
            ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            ship.moving_left = False

def check_events(ship,screen,g_settings,bullets,stats,play_button,aliens):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        check_key_down_events(event,ship,g_settings,screen,bullets,stats,
                              play_button,aliens)
        check_key_up_events(event,ship)

def update_bullets(bullets, aliens,g_settings,screen,ship,stats,sb):
    bullets.update()
    #updates bullet pos bullets
    for bullet in bullets.copy():
        if bullet.rect.bottom <=0:
            bullets.remove(bullet)
    check_bullet_alien_collisions(g_settings,screen,ship,aliens,bullets,stats,
                                  sb)
def check_bullet_alien_collisions(g_settings, screen, ship, aliens, bullets,
                                  stats,sb):
    """Respond to bullet-alien collisions."""
    # Remove any bullets and aliens that have collided.
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    if collisions:
        for aliens in collisions.values():
            stats.score += g_settings.alien_points * len(aliens)
            sb.prep_score()
        check_high_score(stats, sb)
    if len(aliens) == 0:
        # Destroy existing bullets, create new fleet and speed up the game.
        bullets.empty()
        g_settings.increase_speed()
        create_alien_fleet(screen,g_settings,aliens,ship)


def draw_bullets(bullets):

    for bullet in bullets.sprites():
         bullet.draw_bullet()

def screen_unpdate(screen, g_settings, ship, aliens, bullets, stats, 
                   play_button, sb):
    #chenges the creen color each loop
        screen.fill(g_settings.bg_color)
        #draws ship
        ship.blitme()
        draw_bullets(bullets)
        for alien in aliens:
            alien.blitme()
        sb.show_score()
         # Draw the play button if the game is inactive.
        if not stats.game_active:
            play_button.draw_button()

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
    # Look for alien-ship collisions.
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(g_settings,stats,screen,ship,aliens,bullets)
        print("Ship hit!!!")
    check_aliens_bottom(g_settings,stats,screen,ship,aliens,bullets)



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
    if stats.ships_left > 1:
        stats.ships_left -= 1
        # Empty the list of aliens and bullets.
        aliens.empty()
        bullets.empty()
        # Create a new fleet and center the ship.
        create_alien_fleet( screen, g_settings,  aliens,ship,)
        ship.center_ship()
        # Pause.
        sleep(0.5)
    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)

def check_aliens_bottom(g_settings, stats, screen, ship, aliens, bullets):
    """Check if any aliens have reached the bottom of the screen."""
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            #same as if the ship got hit.
            ship_hit(g_settings, stats, screen, ship, aliens, bullets)
            break       
def check_play_button(stats, play_button, mouse_x, mouse_y, g_settings,aliens,
                      bullets,screen,ship,):
    """Start a new game when the player clicks Play."""
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:
        start_game(stats,aliens,bullets,ship,screen,g_settings)

def start_game(stats,aliens,bullets,ship,screen,g_settings):
    g_settings.initialize_dynamic_settings()
    # Hide the mouse cursor.
    pygame.mouse.set_visible(False)
    # Reset the game statistics.
    stats.reset_stats()
    stats.game_active = True
    # Empty the list of aliens and bullets.
    aliens.empty()
    bullets.empty()
    # Create a new fleet and center the ship.
    create_alien_fleet(screen,g_settings,   aliens,ship,)
    ship.center_ship()

def check_high_score(stats, sb):
    """Check to see if there's a new high score."""
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sb.prep_high_score()


    
    
    