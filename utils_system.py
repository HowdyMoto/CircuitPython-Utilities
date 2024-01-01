# utils_system.py -- Helper functions for learning about your boards
# By @howdymoto / Wright Bagwell
# Inspired by TodBot's circuitpython-tricks: https://github.com/todbot/circuitpython-tricks
# And by Adafruit/Kattni Rembor's CircuitPython Essentials: https://learn.adafruit.com/circuitpython-essentials/circuitpython-essentials
# MIT license

import os
import gc
import board

CPUTILS_STRING = 'CP UTILS:'

# A function to check for a pin
# Specify the pin and a description of what it does
# If you're using a board not made by Adafruit, you can use this function to search for non-stnadard pin names.
def check_for_pin(pin, descriptor):
    if hasattr(board, pin):
        pin_detected = True
    else:
        pin_detected = False
    print("\t" + pin, "\t" + descriptor + "\t", pin_detected)
    return pin_detected

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
    get_temperature_info()
    get_speakeroutput_info()
    get_microphone_info()
    get_i2c_info()
    get_uart_info()
    get_spi_info()

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
    builtin_display = check_for_pin("DISPLAY","onboard display")

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
    check_for_pin("LED","status LED\t")

# See if there's a simple status indicator LED on the board.
# This is typically a requirement for CircuitPython boards,
# but there may be some out there that don't have one.
# Almost always set to board.LED pin
def get_dotstar_info():
    check_for_pin("APA102_SCK","DotStar LED\t")

# See if there's a Neopixel LED on the board.
# Almost always set to board.NEOPIXEL pin
def get_neopixel_info():
    check_for_pin("NEOPIXEL","Neopixel LED\t")
    NEOPIXEL_PIN = 'NEOPIXEL'

# See if there's a DotStar LED on the board.
# Almost always set to board.LIGHT pin,
# though I've seen some called AMB (like Unexpected Maker S2)
def get_lightsensor_info():
    check_for_pin("LIGHT","Ambient light sensor")
    check_for_pin("AMB","Ambient light sensor")

# See if there's a Temperature sensot on the board.
# Almost always set to board.TEMPERATURE pin,
def get_temperature_info():
    check_for_pin("TEMPERATURE","temperature sensor")

# See if there's a speaker output on the board.
# Almost always set to board.SPEAKER pin
def get_speakeroutput_info():
   check_for_pin("SPEAKER", "Analog speaker output")

# See if there's microphone on the board.
# Almost always set to board.MICROPHONE_CLOCK and MICROPHONE_DATA, which comes in pairs.
def get_microphone_info():
    check_for_pin("MICROPHONE_CLOCK", "Microphone")

# See if there's an I2C/STEMMA QT connector on the board.
# Almost always set to board.I2C
# Of course you can also manually create I2C connections
# this does not verify whether you can or that you have.
def get_i2c_info():
    i2c_detected = check_for_pin("I2C", "I2C/STEMMA QT")
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
    print("\tI2C scan complete")

# See if there's UART on the board.
# Almost always set to board.UART
def get_uart_info():
    check_for_pin("UART", "UART pin\t")

# See if there's SPI on the board.
# Almost always set to board.SPI
def get_spi_info():
    check_for_pin("SPI", "SPI pin\t")
