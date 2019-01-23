import pygame
from pygame.sprite import Sprite
from random import randint

class Star(Sprite):
    """A class to represent a single star in the fleet."""

    def __init__(self, ai_settings, screen):
       """Initialize the star and set its starting position."""
       super().__init__()
       self.screen = screen
       self.ai_settings = ai_settings
       # Load the star image and set its rect attribute.
       self.image = pygame.image.load('images/Star.bmp')
       self.rect = self.image.get_rect()
       # Start each new star near the top left of the screen.
       self.rect.x = randint(self.rect.width, 1200 - self.rect.width)
       self.rect.y = randint(self.rect.height, 800 - self.rect.height)
       # Store the star's exact position.
       self.x = float(self.rect.x)

    # def check_edges(self):
    #     """Return True if star is at edge of screen."""
    #     screen_rect = self.screen.get_rect()
    #     if self.rect.right >= screen_rect.right:
    #         return True
    #     elif self.rect.left <= 0:
    #         return True
    #
    # def check_TB(self):
    #     """Return True if star is at edge of screen."""
    #     screen_rect = self.screen.get_rect()
    #     if self.rect.bottom >= screen_rect.bottom:
    #         return True
    #     elif self.rect.top <= 0:
    #         return True
    #
    # def update(self):
    #     """Move the star righ or left"""
    #     self.x += (self.ai_settings.star_speed_factor *
    #                     self.ai_settings.fleet_direction)
    #     self.rect.x = self.x

    def blitme(self):
       """Draw the star at its current location."""
       self.screen.blit(self.image, self.rect)
