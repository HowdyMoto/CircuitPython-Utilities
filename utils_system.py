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

    # Board name
    print("\tBoard:\t" + os.uname().machine)
    # CPU name
    print("\tCPU:\t" + os.uname().sysname)
    # CircuitPython version
    print("\tCircuitPython ver:\t" + os.uname().release)

    get_mem_storage_info()
    get_display_info()
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
    if hasattr(board, 'DISPLAY'):
        builtin_display = True
    else:
        builtin_display = False
    print("\tHas built-in display:", "\t", builtin_display)

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

# See if there's a DotStar LED on the board.
# Almost always set to board.APA102_SCK pin
def get_dotstar_info():
    if hasattr(board, 'APA102_SCK'):
        dotstar_detected = True
    else:
        dotstar_detected = False
    print("\tHas DotStar:", "\t", dotstar_detected)

# See if there's a Neopixel LED on the board.
# Almost always set to board.NEOPIXEL pin
def get_neopixel_info():
    if hasattr(board, 'NEOPIXEL'):
        neopixel_detected = True
    else:
        neopixel_detected = False
    print("\tHas Neopixel:", "\t", neopixel_detected)

# See if there's a DotStar LED on the board.
# Almost always set to board.LIGHT pin,
# though I've seen some called AMB (like Unexpected Maker S2) 
def get_lightsensor_info():
    if hasattr(board, 'LIGHT'):
        lightsensor_detected = True
    else:
        lightsensor_detected = False
    print("\tHas Light sensor:", "\t", lightsensor_detected)

# See if there's a speaker output on the board.
# Almost always set to board.SPEAKER pin
def get_speakeroutput_info():
    if hasattr(board, 'SPEAKER'):
        speakeroutput_detected = True
    else:
        speakeroutput_detected = False
    print("\tHas speaker ouput:", "\t", speakeroutput_detected)

# See if there's an I2C Stemma QT connenctor on the board.
# Almost always set to board.I2C
# Of course you can also manually create I2C connections
# this does not verify whether you can or that you have.
def get_i2c_info():
    if hasattr(board, 'I2C'):
        i2c_detected = True
    else:
        i2c_detected = False
    print("\tHas i2c ouput:", "\t", i2c_detected)
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
