import sys
import pygame
from bullet import Bullet
from alian import Alien
from time import sleep
def check_keydown(event,set,screen,ship,bullets):
     """Respond to the key press"""
     if event.key == pygame.K_RIGHT:
         #MOVE THE SHIP TO RIGHT.
         ship.moving_right = True
     elif event.key == pygame.K_LEFT:
         ship.moving_left=True
     elif event.key == pygame.K_SPACE:
         #create a new bullet and add it to the new group
         fire_bullet(set,screen,ship,bullets)
     elif event.key == pygame.K_q:
          sys.exit()
        
def check_keyup(event,ship):
     if event.key==pygame.K_RIGHT:
        ship.moving_right=False
     elif event.key == pygame.K_LEFT:
        ship.moving_left=False
     
def check_events(set,screen,ship,bullets):
    """Respond to keypress and mouse events"""
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type==pygame.KEYDOWN:
                check_keydown(event,set,screen,ship,bullets)
            elif event.type==pygame.KEYUP:
                 check_keyup(event,ship)
                

def update_screen(set,screen,ship,aliens,bullets):
    """Update image on the screen and flip on the new screen"""
    #redraw all bullets behind ship and aliens
    screen.fill(set.bg_color)
    #make the most recently drawn screen visible
    
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    aliens.draw(screen)
    pygame.display.flip()

def update_bullets(set,screen,ship,aliens,bullets):
     bullets.update()
     for bullet in bullets.copy():
         if bullet.rect.bottom <= 0:
             bullets.remove(bullet)
     check_bullet_alien_collisions(set,screen,ship,aliens,bullets)
    

def fire_bullet(set,screen,ship,bullets):
    if len(bullets) < set.bullets_allowed:
             new_bullet=Bullet(set,screen,ship)
             bullets.add(new_bullet)
            
def create_fleet(set,screen,ship,aliens):
     alien=Alien(set,screen)
     number_aliens_x=get_number_aliens_x(set,alien.rect.width)
     number_rows=get_number_rows(set,ship.rect.height,alien.rect.height)
     #create the first raw of alien
     for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
          #create and alien and place it in the row
          create_alien(set,screen,aliens,alien_number,row_number)

def get_number_aliens_x(set,alien_width):
     """Determine the number of aliens that fit in row """
     available_space_x=set.screen_width-2*alien_width
     number_aliens_x=int(available_space_x/(2*alien_width))
     return number_aliens_x

def create_alien(set,screen,aliens,alien_number,row_number):
      alien=Alien(set,screen)
      alien_width=alien.rect.width
      alien.x=alien_width+2*alien_width*alien_number
      alien.rect.x=alien.x
      alien.rect.y=alien.rect.height+2*alien.rect.height*row_number
      aliens.add(alien)
    
def get_number_rows(set,ship_height,alien_height):
     """Determine the number of rows of aliens that fit on the screen"""
     available_space_y=(set.screen_height-(3*alien_height)-ship_height)
     number_rows=int(available_space_y/(2*alien_height))
     return number_rows

def update_aliens(set,stats,screen,ship,aliens,bullets):
     check_fleet_edges(set,aliens)
     aliens.update()
     if pygame.sprite.spritecollideany(ship,aliens):
         ship_hit(set,stats,screen,ship,aliens,bullets)
    
def check_fleet_edges(ai_settings, aliens):
     for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break

def change_fleet_direction(ai_settings, aliens):
     """Drop the entire fleet and change the fleet's direction."""
     for alien in aliens.sprites():
         alien.rect.y += ai_settings.fleet_drop_speed
     ai_settings.fleet_direction *= -1
     
def check_bullet_alien_collisions(set,screen,ship,aliens,bullets):
     collisions=pygame.sprite.groupcollide(bullets,aliens,True,True)
     if len(aliens):
          #destroy existing bullet and create new fleet
          bullets.empty()
          create_fleet(set,screen,ship,aliens)
        
def ship_hit(set,stats,screen,ship,aliens,bullets):
     if stats.ship_left>0:
         stats.ships_left-=1
         #empty the list of aliens and bullet
         aliens.empty()
         bullets.empty()
         create_fleet(set,screen,ship,aliens)
         ship.center_ship()
         sleep(0.5)
     else:
          stats.game_active=False
          
def check_aliens_bottom(set, stats, screen, ship, aliens, bullets):
    """Check if any aliens have reached the bottom of the screen."""
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
	    if alien.rect.bottom >= screen_rect.bottom:
		    # Treat this the same as if the ship got hit.
 		    ship_hit(set, stats, screen, ship, aliens, bullets)
            
               
            

     



    