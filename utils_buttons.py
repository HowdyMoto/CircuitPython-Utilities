# By @howdymoto / Wright Bagwell
# Inspired by TodBot's circuitpython-tricks: https://github.com/todbot/circuitpython-tricks
# And by Adafruit/Kattni Rembor's CircuitPython Essentials: https://learn.adafruit.com/circuitpython-essentials/circuitpython-essentials
# MIT license

""" Helper functions for learning about built-in buttons on your board. """

import board
import digitalio
import time

# Find available button pins
button_pins = [name for name in dir(board) if name.startswith("BUTTON")]

if not button_pins:
    print("No buttons detected! Check your board's documentation.")
else:
    print("=== Detected Buttons ===")
    for button in button_pins:
        print(button)

# Convert detected buttons to DigitalInOut objects
buttons = {name: digitalio.DigitalInOut(getattr(board, name)) for name in button_pins}

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