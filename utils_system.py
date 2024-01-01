# utils_system.py -- Helper functions for learning about your boards
# By @howdymoto / Wright Bagwell
# Inspired by TodBot's circuitpython-tricks: https://github.com/todbot/circuitpython-tricks
# And by Adafruit/Kattni Rembor's CircuitPython Essentials: https://learn.adafruit.com/circuitpython-essentials/circuitpython-essentials
# MIT license

import os
import gc
import board

CPUTILS_STRING = 'CP UTILS:'

def print_board_info():
    print(CPUTILS_STRING, "Getting all board details...")

    print("\tBoard Name:\t" + os.uname().machine)
    print("\tCPU:\t" + os.uname().sysname)
    print("\tCircuitPython ver:\t" + os.uname().release)

    get_mem_storage_info()
    get_display_info()
    get_status_led_info()
    get_dotstar_info()
    get_neopixel_info()
    get_lightsensor_info()
    get_speakeroutput_info()
    get_i2c_info()


# Show details about storage and memory
def get_mem_storage_info():
    fs_stat = os.statvfs('/')
    print("\tDisk size:\t", fs_stat[0] * fs_stat[2] / 1024 / 1024, "\tMB")
    print("\tFree space:\t", fs_stat[0] * fs_stat[3] / 1024 / 1024, "\tMB")
    free_memory = gc.mem_free() / 1024 / 1024
    print("\tFree memory:\t", f"{free_memory:,}", "\tMB" )


# See if the board has a display. If so, show details.
# Almost always set to board.DISPLAY pin
def get_display_info():
    DISPLAY_PIN = 'DISPLAY'
    if hasattr(board, DISPLAY_PIN):
        builtin_display = True
    else:
        builtin_display = False
    print("\t" + DISPLAY_PIN, "\t(display):\t", builtin_display)

    if builtin_display:
        display = board.DISPLAY
        print(
            "\tDisplay size:\t",
            display.width,
            "x",
            display.height
        )
        print("\tDisplay rotation:\t", display.rotation)
        print("\tDisplay bus:\t", display.bus)
        # Some displays, like epaper, do not have an auto-refresh property
        if hasattr(display, 'auto_refresh'):
            auto_refresh_attribute = display.auto_refresh
        else:
            auto_refresh_attribute = "None (probably e-paper)"
        print("\tDisplay auto_refresh:\t", auto_refresh_attribute)
        # Some displays, like epaper, do not have a brightness property
        if hasattr(display, 'brightness'):
            brightness_attribute = display.brightness
        else:
            brightness_attribute = "None (probably e-paper)"
        print("\tDisplay brightness:\t", brightness_attribute)

# See if there's a simple status LED on the board.
# Almost always set to board.LED pin
def get_status_led_info():
    LED_PIN = 'LED'

    if hasattr(board, LED_PIN):
        led_detected = True
    else:
        led_detected = False
    print("\t" + LED_PIN, "\t(status LED):\t", led_detected)

# See if there's a simple status indicator LED on the board.
# This is typically a requirement for CircuitPython boards,
# but there may be some out there that don't have one.
# Almost always set to board.LED pin
def get_dotstar_info():
    DOTSTAR_PIN = 'APA102_SCK'

    if hasattr(board, DOTSTAR_PIN):
        dotstar_detected = True
    else:
        dotstar_detected = False
    print("\t" + DOTSTAR_PIN, "\t(DotStar):\t", dotstar_detected)

# See if there's a Neopixel LED on the board.
# Almost always set to board.NEOPIXEL pin
def get_neopixel_info():
    NEOPIXEL_PIN = 'NEOPIXEL'

    if hasattr(board, NEOPIXEL_PIN):
        neopixel_detected = True
    else:
        neopixel_detected = False
    print("\t"+ NEOPIXEL_PIN, "\t(Neopixel):\t", neopixel_detected)

# See if there's a DotStar LED on the board.
# Almost always set to board.LIGHT pin,
# though I've seen some called AMB (like Unexpected Maker S2)
def get_lightsensor_info():
    LIGHTSENSOR_PIN = 'LIGHT'

    if hasattr(board, LIGHTSENSOR_PIN):
        lightsensor_detected = True
    else:
        lightsensor_detected = False
    print("\t" + LIGHTSENSOR_PIN, "\t(Light sensor):\t", lightsensor_detected)

# See if there's a Temperature sensot on the board.
# Almost always set to board.TEMPERATURE pin,
def get_lightsensor_info():
    TEMPERATURE_PIN = 'TEMPERATURE'

    if hasattr(board, TEMPERATURE_PIN):
        temperature_sensor_detected = True
    else:
        temperature_sensor_detected = False
    print("\t" + TEMPERATURE_PIN, "\t(temperature sensor):\t", temperature_sensor_detected)

# See if there's a speaker output on the board.
# Almost always set to board.SPEAKER pin
def get_speakeroutput_info():
    SPEAKER_PIN = 'SPEAKER'

    if hasattr(board, SPEAKER_PIN):
        speakeroutput_detected = True
    else:
        speakeroutput_detected = False
    print("\t" + SPEAKER_PIN, "\t(speaker ouput):\t", speakeroutput_detected)

# See if there's an I2C Stemma QT connenctor on the board.
# Almost always set to board.I2C
# Of course you can also manually create I2C connections
# this does not verify whether you can or that you have.
def get_i2c_info():
    I2C_PIN = 'I2C'

    if hasattr(board, I2C_PIN):
        i2c_detected = True
    else:
        i2c_detected = False
    print("\t" + I2C_PIN, "\t(I2C/STEAMMA connector):\t", i2c_detected)
    if i2c_detected:
        return
        get_i2c_device_addresses()


def get_i2c_device_addresses():
    i2c = board.I2C()
    print("\tScanning for I2C devices...")
    if not i2c.try_lock():
        pass
    i2c_addresses = i2c.scan()
    if len(i2c_addresses) == 0:
        print("\tNo I2C devices found")
    else:
        print("\tI2C device(s) found at:")
        for address in i2c_addresses:
            print("\t" + hex(address))
    i2c.unlock()
