import pygame
from pygame.sprite import Sprite
class Bullet(Sprite):
    """class manage bullet fire from the ship"""
    def __init__(self,set,screen,ship) -> None:
        super(Bullet,self).__init__()
        self.screen=screen
        #create a bullet rect at (0,0) and then set correct position
        self.rect=pygame.Rect(0,0,set.bullet_width,set.bullet_height)
        self.rect.centerx=ship.rect.centerx
        self.rect.top=self.rect.top
        #store bubble position as a decimal value.
        self.y=float(self.rect.y)
        self.color=set.bullet_color
        self.speed_factor=set.bullet_speed_factor
    def update(self):
        """Move the bullet up the screen"""
        self.y -= self.speed_factor
        #Update the rect position
        self.rect.y=self.y
    def draw_bullet(self):
        pygame.draw.rect(self.screen,self.color,self.rect)


    