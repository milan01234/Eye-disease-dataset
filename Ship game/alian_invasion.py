
import pygame
from setting import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from game_states import GameState 
from alian import Alien
def run_game():
    pygame.init()
    set=Settings()
    stats=GameState(set)
    screen=pygame.display.set_mode((set.screen_width,set.screen_height))
    pygame.display.set_caption("Alian Blast")
    alien=Alien(set,screen)
    # Make a ship
    ship=Ship(set,screen)
    bullets=Group()
    aliens=Group()
    gf.create_fleet(set,screen,ship,aliens)
    #start the main loop for the game 
    while True:
        
        screen.fill(set.bg_color)
        ship.blitme()
        gf.check_events(set,screen,ship,bullets)
        if stats.game_active:
            ship.update()
            gf.update_bullets(set,screen,ship,aliens,bullets)
            gf.update_aliens(set,stats,screen,ship,aliens,bullets)
        gf.update_screen(set,screen,ship,aliens,bullets)
        #Watch for keybord nad mouse events
        pygame.display.flip()

run_game()

