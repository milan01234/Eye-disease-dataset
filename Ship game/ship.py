import pygame
class Ship():
    def __init__(self,set,screen) -> None:
        """Initialize the shipp and set it to the strting position"""
        self.screen=screen
        #load the ship image and get it's rect
        self.image=pygame.image.load("images\ship.bmp")
        self.rect=self.image.get_rect()
        self.screen_rect=screen.get_rect()
        self.set=set
        #start each new ship at the bottom center of the ship
        self.rect.centerx=self.screen_rect.centerx
        self.rect.bottom=self.screen_rect.bottom
        self.center=float(self.rect.centerx)
        self.moving_right=False
        self.moving_left=False
    def update(self):
        """Update the ship position based on the movement flag"""
        if self.moving_right and self.rect.right<self.screen_rect.right:
            self.center +=self.set.ship_speed_factor
        if self.moving_left and self.rect.left>0:
            self.center -=self.set.ship_speed_factor
        self.rect.centerx=self.center
    def blitme(self):
        """Draw the ship at it's current location"""
        self.screen.blit(self.image,self.rect)
    def center_ship(self):
        self.center=self.screen_rect.centerx

    

