import sys
import pygame
from random import randint

from star import Star

def check_events(ai_settings, screen):
    """Respond to keypresses and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #if the quit event is triggered
            sys.exit() # exit game

def get_number_stars_x(ai_settings, star_width):
    """Determine the number of stars that fit in a row."""
    available_space_x = ai_settings.screen_width - 2 * star_width
    number_stars_x = int(available_space_x / (2 * star_width))
    return number_stars_x

def get_number_rows(ai_settings, star_height):
    """Determine the number of rows of stars that fit on the screen."""
    available_space_y = (ai_settings.screen_height - (star_height) )
    number_rows = int(available_space_y / (2 * star_height))
    return number_rows

def create_star(ai_settings, screen, stars, star_number, row_number):
    """Create a star and place it in the row."""
    star = Star(ai_settings, screen)
    # star_width = star.rect.width
    # star.x = star_width + 2 * star_width * star_number
    # star.rect.x = star.x
    # star.rect.y = star.rect.height + 2 * star.rect.height * row_number
    stars.add(star)

def create_fleet(ai_settings, screen, stars):
    """Create a full fleet of stars."""
    # Create an star and find the number of stars in a row.
    # Spacing between each star is equal to one star width.
    star = Star(ai_settings, screen) #1st star which will only function as the left margin. The star wont show because its not added to the group
    number_stars_x = randint(1, get_number_stars_x(ai_settings, star.rect.width))
    number_rows = randint(1, get_number_rows(ai_settings, star.rect.height))

    # Create the first of stars.
    for row_number in range(number_rows):
        for star_number in range(number_stars_x):
            # Create an star and place it in the row.
            create_star(ai_settings, screen, stars, star_number, row_number)

# def check_fleet_edges(ai_settings, stars):
#     """Respond appropriately if any stars have reached an edge."""
#     for star in stars.sprites():
#         if star.check_edges():
#             change_fleet_direction(ai_settings, stars)
#             break
#         elif star.check_TB():
#             change_fleet_direction_TB(ai_settings, stars)
#             break
#
# def change_fleet_direction(ai_settings, stars):
#     """Drop the entire fleet and change the fleet's direction."""
#     for star in stars.sprites():
#         star.rect.y += ai_settings.fleet_drop_speed
#
#     ai_settings.fleet_direction *= -1
#
# def change_fleet_direction_TB(ai_settings, stars):
#     """Drop the entire fleet and change the fleet's direction."""
#     for star in stars.sprites():
#         star.rect.y -= ai_settings.fleet_up_speed
#
#     ai_settings.fleet_direction *= +1
#
# def update_stars(ai_settings, stars):
#     """
#     Check if the fleet is at an edge,
#     Update the postions of all stars in the fleet.
#     """
#     check_fleet_edges(ai_settings, stars)
#     stars.update()

def update_screen(ai_settings, screen, stars):
    """Update images on the screen and flip to the new screen."""

    screen.fill(ai_settings.bg_color) #Redraw the screen during each pass through the loop.

    stars.draw(screen) #Redraw each star in the group to the screen
    pygame.display.flip() # Make the most recently drawn screen visible.
