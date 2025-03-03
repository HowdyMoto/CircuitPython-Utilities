# CircuitPython Utils
A collection of CircuitPython utilities and helper functions to help you get more done with less effort.

This code is under the MIT license, so I encourage you to do as you please with it.

# Built on and tested with CircuitPython 9
These utilities were created and tested with CircuitPython 9, and will be updated as required with future versions of CircuitPython.

They may work fine with older versions of CircuitPython, but I'm not making any effort to support them.

# Usage 

This set of utilities is based on standards that Adafruit uses on their boards. Adafruit is pretty (bot not totally) consistent in naming pins on their boards, so I assume their pin names in the code below. As I learn what naming patterns other manufacturers use, I'll add them.

For example, to see if a board has a built-in ambient light sensor, I look for a pin called `LIGHT`, which is what Adafruit uses on all of their boards that have built-in ambient light sensors. Unexpected Maker names these pins `AMB`. 

Over time, I hope this set of tools can add more support for non-Adafruit boards, but I will first focus on Adafruit boards. If you wish to see wider support for other manufacturers' boards, please submit PRs.

### utils_system.py
A collection of functions that show useful information about your board:
* Microcontroller details
* Built-in modules
* OS Info: Board name, CP version, memory, storage
* Board info (Pin info mostly)

### utils_wifi.py
A collection of functions that help you find, connect to, and test wifi connections. Currently only useful for esp32 chips with native wi-fi. Boards with esp32 co-processors need more work.

### utils_buttons.py
Show the names of built-in buttons, and show which ones are being actively pressed. Only looks for boards with BUTTON pins.

### utils_display.py
A collection of functions that show details about your board's built-in display.

### utils_pins.py
A collection of functions that show details about your board's pins.

### utils_12c.py
A collection of functions that show details about your board's I2C bus.

### utils_benchmark.py
Very simple benchmarks that help you understand the realtive performance of your microprocessor.

Some results I've seen:
| Manufacturer  | Board Name | Status |
| ------------- | ------------- | ------------- |
| Adafruit  | Qt Py SAMD21 | 28.72s integer, 44.33 float |
| Adafruit  | Qt Py ESP32-S3 No PSRAM | 2.69s int, 3.66s float |
| Adafruit  | MagTag  |17.51s int, 23.13s float |
| Adafruit  | Clue | 3.41s int, 4.91s float |
| Adafruit  | Pyportal Titan0 | 5.93s int, 8.42s float |
| Adafruit  | Trinkey RP2040 | 6.14s int, 9.56s float |
_________________

## Boards tested

| Manufacturer  | Board Name | Status |
| ------------- | ------------- | ------------- |
| Adafruit  | MagTag | WORKING |
| Adafruit  | CLUE nRF52840 Express | WORKING |
| Adafruit  | Trinket M0 with samd21e18 | WORKING |
| Adafruit  | QT2040 Trinkey with rp2040 | WORKING |
| Adafruit  | QT Py M0 | WORKING |
| Adafruit  | QtPy esp32-S3 8MB no PSRAM | WORKING |
| Adafruit  | Itsy Bitsy RP2040 |  WORKING |
| Adafruit  | Pyportal Titano |  WORKING |
| Raspberry Pi | Pico | WORKING |
| UnexpectedMaker | Feather S2 | WORKING |
| LILYGO | T8 ESP32-S2 w/Display | WORKING |
| LILYGO | TTGO T-Display | UKNOWN - can't get CP to run on it |
| LILYGO | TTGO T-Display S3 | WORKING (with T-Embed ESP32S3 UF2) |
| LILYGO | TTGO T-Display S3 AMOLED | WORKING (with ESP32-S3-DevKitC-1-N8R8 UF2) |
| LILYGO | T-Camera S3 | WORKING (with YD-ESP32-S3 (N16R8) UF2) |

| Adafruit  | Pyportal Titano 8 | UKNOWN |

_________________

## TODO
- report on ESP32 wi-fi co-processors
- report on bluetooth capabilities
