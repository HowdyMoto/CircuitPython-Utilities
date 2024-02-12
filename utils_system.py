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
    print(f"{pin:<{COLUMN_PINNAME_WIDTH}}{descriptor:<{COLUMN_PINNAME_WIDTH}}\t{pin_detected}")
    return pin_detected

def get_all_info():
    """Print an exhaustive list of details about your board."""

    print("\nBOARD DETAILS...\n")

    get_os_info()
    get_board_info()
    get_microcontroller_info()

    get_i2c_info()
    get_uart_info()
    get_spi_info()

    get_builtin_modules()

def get_os_info():
    """Show os module info. Includes CircuitPython version and filesystem info.
    Show details about storage and memory"""

    print("\n=== os module info ===\n")

    boardNameOS = os.uname().machine
    boardNameOSDescriptor = "Board Name:"
    print(f"{boardNameOSDescriptor: <{COLUMN1_WIDTH}} {boardNameOS: <{COLUMN1_WIDTH}}")

    sysname_descriptor = "System name (CPU):"
    sysname = os.uname().sysname
    print(f"{sysname_descriptor: <{COLUMN1_WIDTH}} {sysname: <{COLUMN1_WIDTH}}")

    cp_descriptor = "CircuitPython ver:"
    cp_version = os.uname().release
    print(f"{cp_descriptor: <{COLUMN1_WIDTH}} {cp_version: <{COLUMN1_WIDTH}}")

    version_descriptor = "Version:"
    version = os.uname().version
    print(f"{version_descriptor: <{COLUMN1_WIDTH}} {version: <{COLUMN1_WIDTH}}")

    free_mem_descriptor = "Free memory:"

    fs_stat = os.statvfs('/')

    disk_size_descriptor = "Disk size:"
    print(f"{disk_size_descriptor:<{COLUMN1_WIDTH}} {(fs_stat[0] * fs_stat[2] / 1024 ):<{COLUMN1_WIDTH}} KB")

    free_space_descriptor = "Disk free space:"
    print(f"{free_space_descriptor:<{COLUMN1_WIDTH}} {(fs_stat[0] * fs_stat[3] / 1024 ):<{COLUMN1_WIDTH}} KB")

    free_memory = gc.mem_free() / 1024
    print(f"{free_mem_descriptor:<{COLUMN1_WIDTH}} {free_memory:<{COLUMN1_WIDTH}}", "KB")

    allocated_memory = gc.mem_alloc() / 1024
    total_memory = allocated_memory + free_memory

    total_mem_descriptor = "Total memory (est):"
    print(f"{total_mem_descriptor:<{COLUMN1_WIDTH}} {total_memory:<{COLUMN1_WIDTH}}", "KB")

    # statvfs
    print("statvfs /")
    print("\t", os.statvfs("/"))


def get_board_info():
    """Show all board module info.
    Mostly shows pin names, and then the board's named pins."""

    print("\n=== board module info ===\n")

    boardNameBoard = board.board_id
    boardNameBoardDescriptor = "Board Name:"
    print(f"{boardNameBoardDescriptor: <{COLUMN1_WIDTH}} {boardNameBoard:<{COLUMN1_WIDTH}}")

    print("Board pins:")

    for item in dir(board):

    # Look in the board's CicrcuitPython source code mpconfigboard.h for the board to see which pins are used for board.I2C()

        # LED related pins
        if item == "LED":
            descriptor = "Built-in Neopixel"
        elif item == "NEOPIXEL":
            descriptor = "Built-in Neopixel"
        elif item == "APA102_SCK":
            descriptor = "Built-in DotStar LED Serial Clock"
        elif item == "APA102_MOSI":
            descriptor = "Built-in DotStar LED Master Out Slave In"
        elif item == "DISPLAY":
            descriptor = "Built-in display"

        # I2C related pins
        elif item == "I2C":
            descriptor = "I2C Bus"
        elif item == "STEMMA_I2C":
            descriptor = "Stemma I2C Connector"
        elif item == "SCL":
            descriptor = "I2C Serial Clock Line"
        elif item == "SDA":
            descriptor = "I2C Serial Data Line"
        elif item == "SCK":
            descriptor = "I2C Serial Clock"

        # SPI related pins
        elif item == "SPI":
            descriptor = "SPI Bus"
        elif item == "MOSI":
            descriptor == "SPI Master Out Slave In"
        elif item == "MISO":
            descriptor = "SPI Master In Slave Out"
        elif item == "SS":
            descriptor = "SPI Slave Select"
        elif item == "CS":
            descriptor = "SPI Slave Select (alt name)"

        # UART
        elif item.startswith("UART"):
            descriptor = "UART"
        elif item == "RX":
            descriptor = "UART receive pin"
        elif item == "TX":
            descriptor = "UART transmit pin"

        # Buttons
        elif item.startswith("BUTTON"):
            descriptor = "Built-in button"
        elif item == "SLIDE_SWITCH":
            descriptor = "Built-in switch"
        elif item == "POWER_SWITCH":
            descriptor = "Built-in power switch"

        # A built-in display
        elif item == "DISPLAY":
            descriptor = "Built-in display"


        # Audio in and out
        elif item == "SPEAKER":
            descriptor = "Speaker output"
        elif item == "AUDIO_OUT":
            descriptor = "Speaker output"
        elif item == "SPEAKER_ENABLE":
            descriptor = "Speaker enabler pin"
        elif item == "MICROPHONE_DATA":
            descriptor = "Microphone PDM data"
        elif item == "MICROPHONE_CLOCK":
            descriptor = "Microphone PDM clock"

        # Other misc sensors
        elif item == "LIGHT":
            descriptor = "Light sensor"
        elif item == "TEMPERATURE":
            descriptor = "Temperature sensor"

        else:
            descriptor = ""
        print(f"\t{item: <{COLUMN1_WIDTH}} {descriptor:<{COLUMN1_WIDTH}}")


def get_microcontroller_info():
    """Show microcontroller/CPU details"""

    print("\n=== microcontroller info ===\n")

    cpu_type_descriptor = "CPU:"
    cpu_type = os.uname().sysname
    print(f"{cpu_type_descriptor: <{COLUMN1_WIDTH}} {cpu_type: <{COLUMN1_WIDTH}}")

    nvm_descriptor = "Non-volatile memory:"
    nvm_bytes = len(microcontroller.nvm) / 1024
    nvm_bytes_formatted = str(nvm_bytes) + " KB"
    print(f"{nvm_descriptor: <{COLUMN1_WIDTH}} {nvm_bytes_formatted: <{COLUMN1_WIDTH}}")

    cpu_frequency_descriptor = "CPU 0 frequency:"
    cpu_frequency_unformatted = microcontroller.cpu.frequency / 1000000
    cpu_frequency =  f"{cpu_frequency_unformatted:,}" + " MHz"
    print(f"{cpu_frequency_descriptor: <{COLUMN1_WIDTH}} {cpu_frequency: <{COLUMN1_WIDTH}}")

    cpu_temperature_descriptor = "CPU 0 temperature:"
    cpu_temperature = microcontroller.cpu.temperature
    if cpu_temperature == None:
        cpu_temperature = "Not available"
    print(f"{cpu_temperature_descriptor: <{COLUMN1_WIDTH}} {cpu_temperature: <{COLUMN1_WIDTH}}")

    cpu_voltage_descriptor = "CPU 0 voltage:"
    cpu_voltage = microcontroller.cpu.voltage
    if cpu_voltage == None:
        cpu_voltage = "Not available"
    print(f"{cpu_voltage_descriptor: <{COLUMN1_WIDTH}} {cpu_voltage: <{COLUMN1_WIDTH}}")

    print("Microcontroller pins:")
    for pin in dir(microcontroller.pin):
        print("\t" + pin)


def get_pin_info():
    """Show how microprocessor and board pins match up"""

    print("\n=== pin name info ===\n")

    # microcontroller.pin contains the list of pins directly provided by the CPU
    # they are typically not labeled with friendly names.
    # Friendly names are created in board.pins as aliases of these pins

    microcontroller_pins = []

    # get the list provided by microcontroller.pin,
    # which contains some other things than Pins
    for pin in dir(microcontroller.pin):
        # check each item to see if it's a Pin
        pin_attr = getattr(microcontroller.pin, pin)
        if (isinstance(pin_attr, microcontroller.Pin) ):
            # the list of pin names associated with the Pin
            pins = []
            # dir(board) has some items that are aliases
            # look at the list it returns
            for alias in dir(board):
                if getattr(board, alias) is getattr(microcontroller.pin, pin):
                    pins.append(f"board.{alias}")
            # Add the original GPIO name, in parentheses.

            # Only include pins that are in board.
            if pins:
                pins.append(f"({str(pin)})")
                microcontroller_pins.append(" ".join(pins))

    for pins in sorted(microcontroller_pins):
        print(pins)


# See if the board has a display. If so, show details.
# Almost always set to board.DISPLAY pin
def get_display_info():
    """Check for a builtin or onboard display, and show its details.
    Will not show details about a display that you add yourself."""

    print("\n=== Built-in Display info ===\n")

    if hasattr(board, "DISPLAY"):
        print("board.DISPLAY pin found")

        display = board.DISPLAY
        print(
            f"{"size":<20}",
            display.width,
            "x",
            display.height
        )
        print(f"{"rotation":<20}", display.rotation)
        print(f"{"bus":<20}", display.bus)
        # Some displays, like epaper, do not have an auto-refresh property
        if hasattr(display, 'auto_refresh'):
            auto_refresh_attribute = display.auto_refresh
        else:
            auto_refresh_attribute = "None (probably e-ink)"
        print(f"{"auto_refresh":<20}", auto_refresh_attribute)
        # Some displays, like epaper, do not have a brightness property
        if hasattr(display, 'brightness'):
            brightness_attribute = display.brightness
        else:
            brightness_attribute = "None (probably e-ink)"
        print(f"{"brightness":<20}", brightness_attribute)
    else:
        print("board.DISPLAY pin not found")


def get_i2c_info():
    """Look for I2C and STEMMA QT I2C pins on the board.
    STEMMA_I2C pin often indicates a solderless connector for connecting devices, but not always.
    On some boards, I2C and STEMMA_I2C are the same pins, which we check for here."""

    print("\n=== i2c info ===\n")
    print("i2c pins found:")

    i2c_pin_found = False
    stemma_i2c_pin_found = False
    stemma_i2c_same = False


    for item in dir(board):
        if item == "SCL":
            descriptor = "I2C Serial Clock Line"
        elif item == "SDA":
            descriptor = "I2C Serial Data Line"
        elif item == "SCK":
            descriptor = "I2C Serial Clock"
        elif item == "I2C":
            descriptor = "I2C Bus"
            i2c_pin_found = True
        elif item == "STEMMA_I2C":
            descriptor = "Stemma I2C Connector"
            stemma_i2c_pin_found = True
        else:
            descriptor = ""
        if descriptor != "":
            print(f"\t{item: <{COLUMN1_WIDTH}} {descriptor:<{COLUMN1_WIDTH}}")


    if i2c_pin_found and stemma_i2c_pin_found:
        if board.I2C() == board.STEMMA_I2C():
            print("\n\tI2C and STEMMA_I2C are the same bus")
            stemma_i2c_same = True
        else:
            print("\tI2C and STEMMA_I2C are separate buses")

    if i2c_pin_found:
            print("\nScanning I2C bus at board.I2C")
            i2c = board.I2C()
            get_i2c_device_addresses(i2c)
    if stemma_i2c_pin_found:
        if (stemma_i2c_same == False):
            print("\nScanning I2C bus at board.STEMMA_I2C")
            stemma_i2c = board.STEMMA_I2C()
            get_i2c_device_addresses(stemma_i2c)

    else:
        print("No I2C or STEMMA_I2C pin found")

def get_i2c_device_addresses(i2c_bus):
    """Scan the specified I2C bus for devices, and report their addresses in hex."""

    if not i2c_bus.try_lock():
        print("Failed to lock I2C bus for scanning. Trying again...")
        pass
    i2c_addresses = i2c_bus.scan()
    if len(i2c_addresses) == 0:
        print("\tNo connected I2C devices found")
    else:
        print("\tI2C device(s) found at:")
        for address in i2c_addresses:
            print("\t\t" + hex(address))
    i2c_bus.unlock()


def get_spi_info():
    """See if there's SPI output on the board.
    Almost always set to board.SPI"""

    check_for_pin("SPI", "SPI pin")
    check_for_pin("MOSI", "SPI Master Out Slave In")
    check_for_pin("MISO", "SPI Master In Slave Out")
    check_for_pin("SCK", "SPI serial clock")
    check_for_pin("SS", "SPI Slave Select")
    check_for_pin("CS", "SPI Slave Select (alt name)")


def get_builtin_modules():
    """List all this board's built-in CircuitPython modules"""

    print("\nBuilt-in modules:\n")
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
