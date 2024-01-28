# By @howdymoto / Wright Bagwell
# Inspired by TodBot's circuitpython-tricks: https://github.com/todbot/circuitpython-tricks
# And by Adafruit/Kattni Rembor's CircuitPython Essentials: https://learn.adafruit.com/circuitpython-essentials/circuitpython-essentials
# MIT license

""" Helper functions for learning about your boards """

import os
import gc
import board
import microcontroller

COLUMN1_WIDTH = 22
COLUMN_PINNAME_WIDTH = 32
INDENT1 = 20

# A function to check for a pin
# First param is the pin name
# Second param is a descriptor of the pin, which is shown in the REPL when it checks for the pin.
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

    print("\nGetting all board details...")

    # Anything else you're looking for can easily be added with check_for_pin()
    get_board_id()
    get_cpu_info()
    get_circuitpython_info()
    get_mem_storage_info()

    print("\nChecking pins...")
    get_i2c_info()
    get_uart_info()
    get_spi_info()
    get_button_pins()
    get_display_info()
    get_status_led_info()
    get_dotstar_info()
    get_neopixel_info()
    get_lightsensor_info()
    get_temperature_info()
    get_speakeroutput_info()
    get_microphone_info()
    get_accelgyro_info()

    get_all_pins()

    get_builtin_modules()

def get_board_id():
    """Show the board's name.
    There are two names: the one os gives you and the one that board gives you.
    They're both very similar, they're both reported in case that's useful."""

    boardNameOS = os.uname().machine
    boardNameOSDescriptor = "\tBoard Name (os):"
    boardNameBoard = board.board_id
    boardNameBoardDescriptor = "\tBoard Name (board):"
    print(f"{boardNameOSDescriptor: <{COLUMN1_WIDTH}} {boardNameOS: <{COLUMN1_WIDTH}}")
    print(f"{boardNameBoardDescriptor: <{COLUMN1_WIDTH}} {boardNameBoard:<{COLUMN1_WIDTH}}")

def get_cpu_info():
    """Show microcontroller/CPU details"""

    cpu_type_descriptor = "\tCPU:"
    cpu_type = os.uname().sysname

    cpu_frequency_descriptor = "\tCPU 0 frequency:"
    cpu_frequency_unformatted = microcontroller.cpu.frequency / 1000000
    cpu_frequency =  f"{cpu_frequency_unformatted:,}" + " MHz"

    cpu_temperature_descriptor = "\tCPU 0 temperature:"
    cpu_temperature = microcontroller.cpu.temperature
    if cpu_temperature == None:
        cpu_temperature = "Not available"

    cpu_voltage_descriptor = "\tCPU 0 voltage:"
    cpu_voltage = microcontroller.cpu.voltage
    if cpu_voltage == None:
        cpu_voltage = "Not available"

    print(f"{cpu_type_descriptor: <{COLUMN1_WIDTH}} {cpu_type: <{COLUMN1_WIDTH}}")
    print(f"{cpu_frequency_descriptor: <{COLUMN1_WIDTH}} {cpu_frequency: <{COLUMN1_WIDTH}}")
    print(f"{cpu_temperature_descriptor: <{COLUMN1_WIDTH}} {cpu_temperature: <{COLUMN1_WIDTH}}")
    print(f"{cpu_voltage_descriptor: <{COLUMN1_WIDTH}} {cpu_voltage: <{COLUMN1_WIDTH}}")

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
    print(f"{disk_size_descriptor:<{COLUMN1_WIDTH}}{(fs_stat[0] * fs_stat[2] / 1024 ):<{COLUMN1_WIDTH}} KB")
    print(f"{free_space_descriptor:<{COLUMN1_WIDTH}}{(fs_stat[0] * fs_stat[3] / 1024 ):<{COLUMN1_WIDTH}} KB")

    free_memory = gc.mem_free() / 1024
    allocated_memory = gc.mem_alloc() / 1024
    total_memory = allocated_memory + free_memory

    print(f"{total_mem_descriptor:<{COLUMN1_WIDTH}} {total_memory:<{COLUMN1_WIDTH}}", "KB")
    print(f"{free_mem_descriptor:<{COLUMN1_WIDTH}} {free_memory:<{COLUMN1_WIDTH}}", "KB")

# See if the board has a display. If so, show details.
# Almost always set to board.DISPLAY pin
def get_display_info():
    """Check for a builtin or onboard display, and show its details.
    Will not show details about a display that you add yourself."""

    builtin_display = check_for_pin("DISPLAY","built-in display")

    if builtin_display:
        display = board.DISPLAY
        print(
            f"\t    {"size":<20}",
            display.width,
            "x",
            display.height
        )
        print(f"\t    {"rotation":<20}", display.rotation)
        print(f"\t    {"bus":<20}", display.bus)
        # Some displays, like epaper, do not have an auto-refresh property
        if hasattr(display, 'auto_refresh'):
            auto_refresh_attribute = display.auto_refresh
        else:
            auto_refresh_attribute = "None (probably e-ink)"
        print(f"\t    {"auto_refresh":<20}", auto_refresh_attribute)
        # Some displays, like epaper, do not have a brightness property
        if hasattr(display, 'brightness'):
            brightness_attribute = display.brightness
        else:
            brightness_attribute = "None (probably e-ink)"
        print(f"\t    {"brightness":<20}", brightness_attribute)

def get_status_led_info():
    """See if there's a simple status LED on the board.
    Almost always set to board.LED pin"""

    check_for_pin("LED","Status LED")

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
    """Look for I2C and STEMMA QT I2C pins on the board.
    STEMMA_I2C pin indicates a solderless connector for connecting devices.
    On some boards, I2C and STEMMA_I2C are the same pins, which we check for here."""

    stemma_i2c_detected = check_for_pin("STEMMA_I2C", "STEMMA QT I2C")
    i2c_detected = check_for_pin("I2C", "I2C pins")

    stemma_i2c_same = False

    if stemma_i2c_detected and i2c_detected:
        if board.I2C() == board.STEMMA_I2C():
            print("\t    I2C and STEMMA_I2C are the same bus")
            stemma_i2c_same = True
        else:
            print("\t    I2C and STEMMA_I2C are separate buses")

    if stemma_i2c_detected:
        print("\t    Scanning I2C bus at board.STEMMA_I2C")
        stemma_i2c = board.STEMMA_I2C()
        get_i2c_device_addresses(stemma_i2c)
    if i2c_detected:
        if (stemma_i2c_same == False):
            print("\t    Scanning I2C bus at board.I2C")
            i2c = board.I2C()
            get_i2c_device_addresses(i2c)
        else:
            return

def get_i2c_device_addresses(i2c_bus):
    """Scan the specified I2C bus for devices, and report their addresses in hex."""

    if not i2c_bus.try_lock():
        print("Failed to lock I2C bus for scanning. Trying again...")
        pass
    i2c_addresses = i2c_bus.scan()
    if len(i2c_addresses) == 0:
        print("\t    No connected I2C devices found")
    else:
        print("\t    I2C device(s) found at:")
        for address in i2c_addresses:
            print("\t\t" + hex(address))
    i2c_bus.unlock()

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

    check_for_pin("TEMPERATURE","Temperature sensor")

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

def get_all_pins():
    """List all the board's pin names, one line at a time"""

    print("\nList all pin names:")

    for item in dir(board):
        print("\t",item)

def get_builtin_modules():
    """List all this board's built-in CircuitPython modules"""

    print("Built-in modules:")
    help("modules")

def get_button_pins():
    """List all the board's built-in buttons"""

    button_count=0

    for item in dir(board):
        if item.startswith("BUTTON"):
            button_count += 1
            check_for_pin(item, "Built-in buttons")

    if (button_count == 0):
        check_for_pin("BUTTON*", "Built-in button")
