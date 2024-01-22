# CircuitPython Utils
A collection of CircuitPython utilities and helper functions to help you get more done with less effort.

This code is under the MIT license, so I encourage you to do as you please with it.

# Built on and tested with CircuitPython 9
These utilities were created and tested with CircuitPython 9.0.0 Alpha 6, and will be updated as required with future versions of CircuitPython.

They may work fine with older versions of CircuitPython, but I'm not making any effort to support them.

# Usage 

This set of utilities is based on standards that Adafruit uses on their boards. Adafruit is pretty (bot not totally) consistent in naming pins on their boards, so I assume their pin names in the code below. As I learn what naming patterns other manufacturers use, I'll add them.

For example, to see if a board has a built-in ambient light sensor, I look for a pin called `LIGHT`, which is what Adafruit uses on all of their boards that have built-in ambient light sensors. Unexpected Maker names these pins `AMB`. 

Over time, I hope this set of tools can add more support for non-Adafruit boards, but I will first focus on Adafruit boards. If you wish to see wider support for other manufacturers' boards, please submit PRs.

### utils_system.py
A collection of functions that show useful information about your board. Great for quickly gathering details without needing to look up spec sheets.

To print (to the REPL) lots of educational details about your board:
```
import utils_sysetem.py

utils_system.print_board_info()
```
`get_all_info()` calls a series of fucntions that gather more granular info about your board. 

If you want just a subset of that information, pick from the functions in get_all_info() that you need, or look inside of `utils_sysetem.py`. It's pretty self-explanatory.

### utils_wifi.py
A collection of functions that help you find, connect to, and test wifi connections. Currently only useful for esp32 chips with native wi-fi. Boards with esp32 co-processors need more work.

To connect to wifi:
```
import utils_wifi.py
utils_wifi.connect_wifi()
```

To find all of the local available WiFi networks, then put them into an array, sorted by signal strength:
```
import utils_wifi.py
utils_wifi.scan_wifi_networks()
```

To gather details about your wifi connection and perform some basic tests:
```
import utils_wifi.py
utils_wifi.test_wifi()
```

To do an HTTP get request and report bandwith, you can try:
```
import utils_wifi.py
utils_wifi.test_bandwidth()
```
Admittedly, this isn't very helpful at all, since you can't download much of anything to a microcontroller that has so little memory and storage. This is a theoretical test, not a practical test at all. But I'll keep working on ways to test bandwidth, so that future boards that have more memory and storage can attempt a more robust test.

### utils_benchmark.py
Very simple benchmarks that help you understand the realtive performance of your microprocessor.

To see how fast your processor does integer and floating point math:
```
import utils_benchmark.py
utils_benchmark.run_benchmark()
```

For example, here are some results I've seen:
- Adafruit Qt Py SAMD21: 28.72 seconds to run integer math tests, 44.33 seconds to run float math tests.
- Adafruit Qt Py ESP32-S3 No PSRAM: 2.69 seconds to run integer math tests, 3.66 seconds to run float math tests.
- Adafruit MagTag: 17.51 seconds to run integer math tests, 23.13 seconds to run float math tests.
- Adafruit Clue: 3.41 seconds to run integer math tests, 4.91 seconds to run float math tests.

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
| Raspberry Pi | Pico | WORKING |
| UnexpectedMaker | Feather S2 | WORKING |
| LILYGO | T8 ESP32-S2 w/Display | WORKING |
| LILYGO | TTGO T-Display | UKNOWN - can't get CP to run on it |
| LILYGO | TTGO T-Display S3 | WORKING (with T-Embed ESP32S3 UF2) |
| LILYGO | TTGO T-Display S3 AMOLED | WORKING (with ESP32-S3-DevKitC-1-N8R8 UF2) |
| LILYGO | T-Camera S3 | WORKING (with YD-ESP32-S3 (N16R8) UF2) |

| Adafruit  | Pyportal Titano 8 | UKNOWN |

## TODO
- gather info on built-in buttons
- report whether wifi capabilities exist, for ESPSPI chips and for native wifi on newer ESP32 CPUs
- report on bluetooth capabilities
