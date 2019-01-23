import pygame
from pygame.sprite import Group

from settings import Settings
import game_function as gf

def run_game():
    '''
    Initialize pygame ,
    create a screen object
    (window screen size & window caption) & settings
    '''
    pygame.init()
    ai_settings = Settings() #Object of Settings() class
    screen = pygame.display.set_mode(
    (ai_settings.screen_width, ai_settings.screen_height)) #set screen size by passing in Settings width & height attributes
    pygame.display.set_caption("Stars Drop")

    #Make a ship, a group of bullets & a group of stars
    stars = Group()

    #Create the fleet of stars
    gf.create_fleet(ai_settings, screen, stars)


    # Start the main loop for the game.
    while True:
        gf.check_events(ai_settings, screen)
        # gf.update_stars(ai_settings, stars)
        gf.update_screen(ai_settings, screen, stars)


run_game()
