# CircuitPython Utils
A collection of CircuitPython utilities and helper functions to help you get more done with less effort.

This code is under the MIT license, so I encourage you to do as you please with it.

# Usage 

This set of utilities is based on standards that Adafruit uses on their boards. Adafruit names their pins consistently on all of their boards, and I assume their pin names in the code below. 

For example, to see if a board has a built-in ambient light sensor, I look for a pin called `LIGHT`, which is what Adafruit uses on all of their boards that have built-in ambient light sensors. Unexpected Maker names these pins `AMB`. 

Over time, I hope this set of tools can add more support for non-Adafruit boards, but I will first focus on Adafruit boards. If you wish to see wider support for other manufacturer's boards, please submit PRs.

### utils_system.py
A collection of functions that show useful information about your board. Great for quickly gathering details without needing to look up spec sheets.

### utils_wifi.py
A collection of functions that help you find, connect to, and test wifi connections.

## Boards I'll be testing
- Adafruit MagTag - works
- Adafruit Trinket M0 - works
- UnexpectedMaker Feather S2 - works
- Adafruit QtPy - works
  
- Adafruit Pyportal Titano 
- Adafruit QtPy esp32-S3 8MB no PSRAM
- Lilygo T-Display

- Adafruit itsy Bitsy RP2040 - Does NOT work
