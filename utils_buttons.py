# By @howdymoto / Wright Bagwell
# Inspired by TodBot's circuitpython-tricks: https://github.com/todbot/circuitpython-tricks
# And by Adafruit/Kattni Rembor's CircuitPython Essentials: https://learn.adafruit.com/circuitpython-essentials/circuitpython-essentials
# MIT license

""" Helper functions for learning about built-in buttons on your board. """

import board
import digitalio
import time

# Find available button pins
button_pins = []
for name in dir(board):
    if name.startswith("BUTTON"):
        button_pins.append(name)

if not button_pins:
    print("No built-in buttons detected!\nThis code looks for pins named BUTTON.")
else:
    print("=== Detected Buttons ===")
    for button in button_pins:
        print(button)

# Convert detected buttons to DigitalInOut objects
buttons = {}  # Create an empty dictionary
for name in button_pins:
    pin = getattr(board, name)  # Get the actual pin from the board module
    buttons[name] = digitalio.DigitalInOut(pin)  # Create DigitalInOut object and store it

# Now `buttons` is a dictionary where each key is a button name, 
# and each value is a DigitalInOut object for that button.
# Configure buttons as input with pull-ups
for button in buttons.values():
    button.switch_to_input(pull=digitalio.Pull.UP)

# Track previous button states (default to True = not pressed)
button_states = {name: True for name in button_pins}

print(f"Monitoring {len(buttons)} button(s)...")

try:
    while True:
        for name, button in buttons.items():
            current_state = button.value  # Read button state

            # Detect press (HIGH -> LOW)
            if not current_state and button_states[name]:
                print(f"{name} PRESSED!")

            # Detect release (LOW -> HIGH)
            if current_state and not button_states[name]:
                print(f"{name} RELEASED!")

            # Update stored state
            button_states[name] = current_state

        time.sleep(0.05)  # Delay to prevent excessive polling

finally:
    # Clean up resources on exit
    for button in buttons.values():
        button.deinit()
    print("Buttons deinitialized.")