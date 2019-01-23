class Settings():
       """A class to store all settings for star Invasion."""
       def __init__(self):
           """Initialize the game's settings."""
           # Screen settings
           self.screen_width = 1200
           self.screen_height = 800
           self.bg_color = (169,169,169)

           # star settings
           self.star_speed_factor = 1
           self.fleet_drop_speed = 10
           self.fleet_up_speed = 10
           # fleet_direction of 1 represents right; -1 represents left.
           self.fleet_direction = 1
