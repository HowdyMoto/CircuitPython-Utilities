# By @howdymoto / Wright Bagwell
# Inspired by TodBot's circuitpython-tricks: https://github.com/todbot/circuitpython-tricks
# And by Adafruit/Kattni Rembor's CircuitPython Essentials: https://learn.adafruit.com/circuitpython-essentials/circuitpython-essentials
# MIT license

""" Helper functions for learning about built-in buttons on your board. """

import board
import digitalio
import time


def get_buttons():
    """Detect built-in buttons and return them as configured DigitalInOut objects.

    Scans the board module for pins starting with "BUTTON", configures them
    as inputs with pull-ups, and returns them in a dictionary.

    Returns:
        dict: Dictionary mapping button names (str) to DigitalInOut objects.
            Empty dict if no buttons are found.
    """
    button_pins = []
    for name in dir(board):
        if name.startswith("BUTTON"):
            button_pins.append(name)

    if not button_pins:
        print("No built-in buttons detected!\nThis code looks for pins named BUTTON.")
        return {}

    print("=== Detected Buttons ===")
    for button in button_pins:
        print(button)

    buttons = {}
    for name in button_pins:
        pin = getattr(board, name)
        buttons[name] = digitalio.DigitalInOut(pin)

    for button in buttons.values():
        button.switch_to_input(pull=digitalio.Pull.UP)

    return buttons


def monitor_buttons(buttons=None):
    """Monitor buttons for press and release events.

    Polls the given buttons in a loop, printing messages on press and release.
    If no buttons dict is provided, calls get_buttons() to detect them.

    Args:
        buttons (dict, optional): Dictionary of button names to DigitalInOut objects,
            as returned by get_buttons(). If None, buttons are auto-detected.
    """
    if buttons is None:
        buttons = get_buttons()

    if not buttons:
        return

    print(f"Monitoring {len(buttons)} button(s)...")

    button_states = {name: True for name in buttons}

    try:
        while True:
            for name, button in buttons.items():
                current_state = button.value

                if not current_state and button_states[name]:
                    print(f"{name} PRESSED!")

                if current_state and not button_states[name]:
                    print(f"{name} RELEASED!")

                button_states[name] = current_state

            time.sleep(0.05)

    finally:
        for button in buttons.values():
            button.deinit()
        print("Buttons deinitialized.")
