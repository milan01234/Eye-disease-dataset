import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    def __init__(self,set,screen):
        """Initialize the alien and set it to the starting position"""
        super(Alien,self).__init__()
        self.screen=screen
        self.set=set
        #load the alian image and set it to the rect attribute
        self.image=pygame.image.load("images\Alien.bmp")
        self.rect=self.image.get_rect()
        #start each new alian at top left corner of the screen
        self.rect.x=self.rect.width
        self.rect.y=self.rect.height
        #store alian exact position
        self.x=float(self.rect.x)
    def blitme(self):
        """Draw the alian at it's current location"""
        self.screen.blit(self.image,self.rect)
    def update(self):
        """Move the alien right"""
        self.x+=(self.set.alien_speed_factor*self.set.fleet_direction)
        self.rect.x=self.x
    def check_edges(self):
        """Return True if alien is at edge of screen"""
        screen_rect=self.screen.get_rect()
        if self.rect.right>=screen_rect.right:
            return True
        elif self.rect.left<=0:
            return True