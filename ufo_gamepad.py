"""
Edit kerning.plist with a USB gamepad. Developed with and tested on 
a Retrolink SNES usb gamepad: https://www.amazon.com/Nintendo-Retrolink-Super-Classic-Controller-NES/
"""

import os
import sys
import math
import pygame as pg

CAPTION = "UFO Gamepad"
SCREEN_SIZE = (500, 500)
BACKGROUND_COLOR = (50, 50, 50)
COLOR_KEY = (255, 0, 255)

class App(object):
    """This is the main class, it manages event loops."""

class Control(object):
    """USB Gamepad"""
    def __init__(self):
        """Setup"""
        self.screen = pg.display.get_surface()
        self.screen_rect = self.screen.get_rect()
        self.joys = initialize_all_gamepads()
        self.done = False
        self.clock = pg.time.Clock()
        self.fps = 60
        self.keys = pg.key.get_pressed()

    def update(self):
        """Update all kerning."""
        self.objects.update(self.screen_rect)

    def draw(self):
        """Draw all glyphs to the display surface."""
        self.screen.fill(BACKGROUND_COLOR)
        self.objects.draw(self.screen)

    def display_fps(self):
        """Show the program's FPS in the window handle."""
        caption = "{} - FPS: {:.2f}".format(CAPTION, self.clock.get_fps())
        pg.display.set_caption(caption)

def initialize_all_gamepads():
    """Checks for gamepads and returns an initialized list of them if found."""
    joysticks = []
    for joystick_id in range(pg.joystick.get_count()):
        joysticks.append(pg.joystick.Joystick(joystick_id))
        joysticks[joystick_id].init()
    return joysticks

def main():
    """Prepare display, load fonts, and start program."""
    global FONT
    os.environ['SDL_VIDEO_CENTERED'] = '1'
    pg.init()
    pg.display.set_caption(CAPTION)
    pg.display.set_mode(SCREEN_SIZE)
    # Control().main_loop()
    pg.quit()
    sys.exit()

if __name__ == "__main__":
    main()