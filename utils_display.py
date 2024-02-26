# By @howdymoto / Wright Bagwell
# Inspired by TodBot's circuitpython-tricks: https://github.com/todbot/circuitpython-tricks
# And by Adafruit/Kattni Rembor's CircuitPython Essentials: https://learn.adafruit.com/circuitpython-essentials/circuitpython-essentials
# MIT license

""" Helper functions for your board's buit-in display """

import board

# See if the board has a display. If so, show details.
# Almost always set to board.DISPLAY pin
def get_display_info():
    """Check for a builtin or onboard display, and show its details.
    Will not show details about a display that you add yourself."""

    print("\n=== Built-in Display info ===\n")

    if hasattr(board, "DISPLAY"):
        print("board.DISPLAY pin found")

        display = board.DISPLAY
        print(
            f"{"size":<20}",
            display.width,
            "x",
            display.height
        )
        print(f"{"rotation":<20}", display.rotation)
        print(f"{"bus":<20}", display.bus)
        
        # Auto-refresh
        # Some displays, like epaper, do not have an auto-refresh property
        if hasattr(display, 'auto_refresh'):
            auto_refresh_attribute = display.auto_refresh
        else:
            auto_refresh_attribute = "None (probably e-ink)"
        print(f"{"auto_refresh":<20}", auto_refresh_attribute)
        
        # Brightness
        # Some displays, like epaper, do not have a brightness property
        if hasattr(display, 'brightness'):
            brightness_attribute = display.brightness
        else:
            brightness_attribute = "None (probably e-ink)"
        print(f"{"brightness":<20}", brightness_attribute)
    
    else:
        print("board.DISPLAY pin not found")
    
def rotate_display(angle):
    display = board.DISPLAY
    display.rotation = angle
    print("\nDisplay rotated to", angle)