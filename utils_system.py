# By @howdymoto / Wright Bagwell
# Inspired by TodBot's circuitpython-tricks: https://github.com/todbot/circuitpython-tricks
# And by Adafruit/Kattni Rembor's CircuitPython Essentials: https://learn.adafruit.com/circuitpython-essentials/circuitpython-essentials
# MIT license
""" Helper functions for learning about your boards """

import os
import gc
import board

CPUTILS_STRING = 'CP UTILS:'
COLUMN1_WIDTH = 22
COLUMN_PINNAME_WIDTH = 32
INDENT1 = 20

# A function to check for a pin
# Specify the pin and a description of what it does
# If you're using a board not made by Adafruit, you can use this function to search for non-standard pin names.
def check_for_pin(pin, descriptor):
    """Check for a pin on the board.
    If you're using a board not made by Adafruit, you can use this function to search for non-standard pin names.
    You can 'import board' and then dir(board) to see what pins your board has."""

    if hasattr(board, pin):
        pin_detected = True
    else:
        pin_detected = False
    print(f"\t{pin:<{COLUMN_PINNAME_WIDTH}}{descriptor:<{COLUMN_PINNAME_WIDTH}}\t{pin_detected}")
    return pin_detected

def get_all_info():
    """Print an exhaustive list of details about your board.
    Add custom calls to check_for_pin() if you want to look for something that's not here."""

    print(CPUTILS_STRING, "Getting all board details...")

    # Anything else you're looking for can easily be added with checK_for_pin()
    get_board_id()
    get_cpu_info()
    get_circuitpython_info()
    get_mem_storage_info()

    print("\n\tChecking pins")
    get_i2c_info()
    get_uart_info()
    get_spi_info()
    get_display_info()
    get_status_led_info()
    get_dotstar_info()
    get_neopixel_info()
    get_lightsensor_info()
    get_temperature_info()
    get_speakeroutput_info()
    get_microphone_info()
    get_accelgyro_info()

    print_all_pins()

    #get_builtin_modules()

def get_board_id():
    """Show the board's name.
    There are two names: the one os gives you and the one that board gives you.
    They're both very similar, they're both reported in case that's useful."""

    boardNameOS = os.uname().machine
    boardNameOSDescriptor = "\tBoard Name (os):"
    boardNameBoard = board.board_id
    boardNameBoardDescriptor = "\tBoard Name (os):"
    print(f"{boardNameOSDescriptor: <{COLUMN1_WIDTH}} {boardNameOS: <{COLUMN1_WIDTH}}")
    print(f"{boardNameBoardDescriptor: <{COLUMN1_WIDTH}} {boardNameBoard:<{COLUMN1_WIDTH}}")

def get_cpu_info():
    """Show what CPU/Chip the board has"""

    cpu_descriptor = "\tCPU:"
    cpu_type = os.uname().sysname
    print(f"{cpu_descriptor: <{COLUMN1_WIDTH}} {cpu_type: <{COLUMN1_WIDTH}}")    
    
def get_circuitpython_info():
    """Show CircuitPython version"""

    cp_descriptor = "\tCircuitPython ver:"
    cp_version = os.uname().release
    print(f"{cp_descriptor: <{COLUMN1_WIDTH}} {cp_version: <{COLUMN1_WIDTH}}")    

def get_mem_storage_info():
    """Show details about storage and memory"""

    disk_size_descriptor = "\tDisk size:"
    free_space_descriptor = "\tDisk free space:"
    total_mem_descriptor = "\tTotal memory (est):"
    free_mem_descriptor = "\tFree memory:"

    fs_stat = os.statvfs('/')
    print(f"{disk_size_descriptor:<{COLUMN1_WIDTH}}{(fs_stat[0] * fs_stat[2] / 1024 / 1024):<{COLUMN1_WIDTH}} MB")
    print(f"{free_space_descriptor:<{COLUMN1_WIDTH}}{(fs_stat[0] * fs_stat[3] / 1024 / 1024):<{COLUMN1_WIDTH}} MB")

    free_memory = gc.mem_free() / 1024 / 1024
    allocated_memory = gc.mem_alloc() / 1024 / 1024
    total_memory = allocated_memory + free_memory

    print(f"{total_mem_descriptor:<{COLUMN1_WIDTH}} {total_memory:<{COLUMN1_WIDTH}}", "MB")
    print(f"{free_mem_descriptor:<{COLUMN1_WIDTH}} {free_memory:<{COLUMN1_WIDTH}}", "MB")

# See if the board has a display. If so, show details.
# Almost always set to board.DISPLAY pin
def get_display_info():
    """Check for a builtin or onboard display, and show its details.
    Will not show details about a display that you add yourself."""

    builtin_display = check_for_pin("DISPLAY","built-in display")

    if builtin_display:
        display = board.DISPLAY
        print(
            f"\t\t{"size":<20}",
            display.width,
            "x",
            display.height
        )
        print(f"\t\t{"rotation":<20}", display.rotation)
        print(f"\t\t{"bus":<20}", display.bus)
        # Some displays, like epaper, do not have an auto-refresh property
        if hasattr(display, 'auto_refresh'):
            auto_refresh_attribute = display.auto_refresh
        else:
            auto_refresh_attribute = "None (probably e-paper)"
        print(f"\t\t{"auto_refresh":<20}", auto_refresh_attribute)
        # Some displays, like epaper, do not have a brightness property
        if hasattr(display, 'brightness'):
            brightness_attribute = display.brightness
        else:
            brightness_attribute = "None (probably e-paper)"
        print(f"\t\t{"brightness":<20}", brightness_attribute)

def get_status_led_info():
    """See if there's a simple status LED on the board.
    Almost always set to board.LED pin"""

    check_for_pin("LED","status LED")

def get_dotstar_info():
    """See if there's a simple status indicator LED on the board.
    This is typically a requirement for CircuitPython boards,
    but there may be some out there that don't have one.
    Almost always set to board.LED pin"""

    check_for_pin("APA102_SCK","DotStar LED")

def get_neopixel_info():
    """See if there's a Neopixel LED on the board.
    Almost always set to board.NEOPIXEL pin"""

    check_for_pin("NEOPIXEL","Neopixel LED")
    NEOPIXEL_PIN = 'NEOPIXEL'

def get_lightsensor_info():
    """See if there's a DotStar LED on the board.
    Almost always set to board.LIGHT pin,
    though I've seen some called AMB (like Unexpected Maker S2)"""

    check_for_pin("LIGHT","Ambient light sensor")
    check_for_pin("AMB","Ambient light sensor")

def get_i2c_info():
    """See if there's an I2C/STEMMA QT connector on the board.
    Some boards have board.I2C but no STEMMA so I check for STEMMA_I2C
    Of course you can also manually create I2C connections. This does not verify whether you can or that you have."""

    i2c_detected = check_for_pin("STEMMA_I2C", "I2C STEMMA QT")
    if i2c_detected:
        get_i2c_device_addresses()

def get_i2c_device_addresses():
    """Scan the I2C bus for devices, and report their addresses in hex."""

    try:
        i2c = board.STEMMA_I2C()
        print("\t    I2C pin found at board.STEMMA_I2C")
    except:
        i2c = board.I2C()
        print("\tI2C pin found at board.I2C")

    if not i2c.try_lock():
        print("Failed to lock I2C bus for scanning. Trying again...")
        pass
    i2c_addresses = i2c.scan()
    if len(i2c_addresses) == 0:
        print("\t    No connected I2C devices found")
    else:
        print("\t    I2C device(s) found at:")
        for address in i2c_addresses:
            print("\t\t" + hex(address))
    i2c.unlock()

def get_uart_info():
    """See if there's UART serial output on the board.
    Almost always set to board.UART"""

    check_for_pin("UART", "UART pin")

def get_spi_info():
    """See if there's SPI output on the board.
    Almost always set to board.SPI"""

    check_for_pin("SPI", "SPI pin")

def get_temperature_info():
    """See if there's a built-in Temperature sensot on the board.
    Almost always set to board.TEMPERATURE pin"""

    check_for_pin("TEMPERATURE","temp sensor")

def get_speakeroutput_info():
    """See if there's a built-in speaker output on the board.
    Almost always set to board.SPEAKER pin"""

    check_for_pin("SPEAKER", "Analog speaker output")

def get_microphone_info():
    """See if there's a built-in microphone on the board.
    Almost always set to board.MICROPHONE_CLOCK and MICROPHONE_DATA, which come in pairs."""

    check_for_pin("MICROPHONE_CLOCK", "Microphone")

def get_accelgyro_info():
    """See if there's a built-in LSM9DS1-type accelerometer/magnetometer/gyroscope on the board.
    Almost always set to board.ACCELEROMETER_GYRO_INTERRUPT"""

    check_for_pin("ACCELEROMETER_GYRO_INTERRUPT", "LSM9DS1 pin")

def print_all_pins():
    """List all the board's pin names, one line at a time"""

    print(CPUTILS_STRING, "List all pin names:")

    for item in dir(board):
        print("\t",item)

def get_builtin_modules():
    """List all this board's built-in CircuitPython modules"""

    print(CPUTILS_STRING, "Built-in modules:")
    help("modules")