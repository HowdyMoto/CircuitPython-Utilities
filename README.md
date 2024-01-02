# CircuitPython Utils
A collection of CircuitPython utilities and helper functions to help you get more done with less effort.

This code is under the MIT license, so I encourage you to do as you please with it.

# CircuitPython version
These utilities were created and tested with CircuitPython 9.0.0 Alpha 6, and will be updated as required with future versions of CircuitPython.

# Usage 

This set of utilities is based on standards that Adafruit uses on their boards. Adafruit names their pins consistently on all of their boards, and I assume their pin names in the code below. 

For example, to see if a board has a built-in ambient light sensor, I look for a pin called `LIGHT`, which is what Adafruit uses on all of their boards that have built-in ambient light sensors. Unexpected Maker names these pins `AMB`. 

Over time, I hope this set of tools can add more support for non-Adafruit boards, but I will first focus on Adafruit boards. If you wish to see wider support for other manufacturers' boards, please submit PRs.

### utils_system.py
A collection of functions that show useful information about your board. Great for quickly gathering details without needing to look up spec sheets.

### utils_wifi.py
A collection of functions that help you find, connect to, and test wifi connections.

## Boards I'll be testing
- Adafruit MagTag - works
- Adafruit CLUE nRF52840 Express - works
- Adafruit Trinket M0 with samd21e18 - works
- Adafruit QT2040 Trinkey with rp2040 - works
- Raspberry Pi Pico with rp2040 - works
- UnexpectedMaker Feather S2 - works
- LILYGO TTGO T8 ESP32-S2 w/Display - works
  
- Adafruit Pyportal Titano 
- Lilygo T-Display - uknown, trying to get CP running on it

Boards exhibiting I2C issue `RuntimeError: No pull up found on SDA or SCL; check your wiring`

- Adafruit Itsy Bitsy RP2040
- Adafruit QT Py M0 with samd21e18
- Adafruit QtPy esp32-S3 8MB no PSRAM

| Manufacturer  | Board Name | Status
| ------------- | ------------- |
| Adafruit  | MagTag | WORKING
| Adafruit  | CLUE nRF52840 Express | WORKING
| Adafruit  | Trinket M0 with samd21e18 | WORKING
| Adafruit  | QT2040 Trinkey with rp2040 | WORKING
| Adafruit  | Pyportal Titano 8 | UKNOWN
| Adafruit  | Itsy Bitsy RP2040 | NOT WORKING No pull up found on SDA or SCL
| Adafruit  | QT Py M0 | NOT WORKING No pull up found on SDA or SCL
| Adafruit  | QtPy esp32-S3 8MB no PSRAM | NOT WORKING No pull up found on SDA or SCL
