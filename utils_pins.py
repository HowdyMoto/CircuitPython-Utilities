# By @howdymoto / Wright Bagwell
# Inspired by TodBot's circuitpython-tricks: https://github.com/todbot/circuitpython-tricks
# And by Adafruit/Kattni Rembor's CircuitPython Essentials: https://learn.adafruit.com/circuitpython-essentials/circuitpython-essentials
# MIT license

""" Helper functions for board pins """

import board

COLUMN1_WIDTH = 22

def get_board_pins():
    """Show all board module info.
    Mostly shows pin names, and then the board's named pins."""

    print("\n=== board pins detail ===\n")

    boardNameBoard = board.board_id
    boardNameBoardDescriptor = "Board Name:"
    print(f"{boardNameBoardDescriptor: <{COLUMN1_WIDTH}} {boardNameBoard:<{COLUMN1_WIDTH}}")
    print("Board pins:")

    pins = dir(board)
    pins.sort()

    for item in pins:

    # Look in the board's CicrcuitPython source code mpconfigboard.h for the board to see which pins are used for board.I2C()

        # Generic analog and digital pins
        if len(item) >= 2 and item[0] == "A" and item[1].isdigit():
            descriptor = "Generic analog pin"
        elif len(item) >= 2 and item[0] == "D" and item[1].isdigit():
            descriptor = "Generic digital pin"

        # LED related pins
        elif item == "LED":
            descriptor = "Built-in Neopixel"
        elif item == "NEOPIXEL":
            descriptor = "Built-in Neopixel"
        elif item == "APA102_SCK":
            descriptor = "Built-in DotStar LED Serial Clock"
        elif item == "APA102_MOSI":
            descriptor = "Built-in DotStar LED Master Out Slave In"
        elif item == "DOTSTAR_CLOCK":
            descriptor = "Built-in DotStar LED Serial Clock"
        elif item == "DOTSTAR_DATA":
            descriptor = "Built-in DotStar color data"

        # I2C related pins
        elif item == "I2C":
            descriptor = "I2C Bus"
        elif item == "STEMMA_I2C":
            descriptor = "Stemma I2C Connector"
        elif item.startswith("SCL"):
            descriptor = "I2C Serial Clock Line"
        elif item.startswith("SDA"):
            descriptor = "I2C Serial Data Line"
        elif item.startswith("SCK"):
            descriptor = "I2C Serial Clock"

        # SPI related pins
        elif item == "SPI":
            descriptor = "SPI Bus"
        elif item == "MOSI":
            descriptor = "SPI Master Out Slave In"
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
            descriptor = "UART receive"
        elif item == "TX":
            descriptor = "UART transmit"

        # Buttons
        elif item.startswith("BUTTON"):
            descriptor = "Built-in button"
        elif item == "SLIDE_SWITCH":
            descriptor = "Built-in switch"
        elif item == "POWER_SWITCH":
            descriptor = "Built-in power switch"

        # Built-in display
        elif item == "DISPLAY":
            descriptor = "Built-in display"
        # TFT display pins
        elif item == "TFT_BACKLIGHT":
            descriptor = "TFT display backlight control"
        elif item == "TFT_CS":
            descriptor = "TFT display chip select for SPI bus"
        elif item == "TFT_RS":
            descriptor = "TFT register or display data/command select"
        elif item == "TFT_DC":
            descriptor = "TFT register or display data/command select"
        elif item == "TFT_MOSI":
            descriptor = "TFT display SPI Master Out Slave In"
        elif item == "TFT_RESET":
            descriptor = "TFT display reset"
        elif item == "TFT_SCK":
            descriptor = "TFT display SPI serial clock"
        elif item == "TFT_TE":
            descriptor = "TFT tearing effect/prevention"
        elif item == "TFT_WR":
            descriptor = "TFT display write"
        elif item == "TFT_RD":
            descriptor = "TFT display read"

        # LCD pins
        elif item.startswith("LCD_DATA"):
            descriptor = "LCD data"

        # E-ink display
        elif item == "EPD_BUSY":
            descriptor = "E-ink display busy signal"
        elif item == "EPD_CS":
            descriptor = "E-ink display chip select for SPI bus"
        elif item == "EPD_DC":
            descriptor = "E-ink display data/command select"
        elif item == "EPD_MISO":
            descriptor = "E-ink display SPI Master In Slave Out"
        elif item == "EPD_MOSI":
            descriptor = "E-ink display SPI Master Out Slave In"
        elif item == "EPD_RESET":
            descriptor = "E-ink display display reset"
        elif item == "EPD_SCK":
            descriptor = "E-ink display display SPI serial clock"

        # Touchscreen pins
        elif item == "TOUCH_XL":
            descriptor = "Touchscreen X left"
        elif item == "TOUCH_XR":
            descriptor = "Touchscreen X right"
        elif item == "TOUCH_YD":
            descriptor = "Touchscreen Y down"
        elif item == "TOUCH_YU":
            descriptor = "Touchscreen Y up"

        # Audio in and out
        elif item == "SPEAKER":
            descriptor = "Speaker output"
        elif item == "AUDIO_OUT":
            descriptor = "Speaker output"
        elif item == "SPEAKER_ENABLE":
            descriptor = "Speaker enable"
        elif item == "MICROPHONE_DATA":
            descriptor = "Microphone PDM data"
        elif item == "MICROPHONE_CLOCK":
            descriptor = "Microphone PDM clock"

        # Other misc sensors
        elif item == "LIGHT":
            descriptor = "Light sensor"
        elif item == "L":
            descriptor = "Light sensor TEST"
        elif item == "TEMPERATURE":
            descriptor = "Temperature sensor"

        # ESP32 co-processor pins
        elif item == "ESP_BUSY":
            descriptor = "ESP32 co-processor busy status"
        elif item == "ESP_CS":
            descriptor = "ESP32 co-processor SPI chip select"
        elif item == "ESP_RESET":
            descriptor = "ESP32 co-processor reset"
        elif item == "ESP_RTS":
            descriptor = "ESP32 co-processor request-to-send for UART"
        elif item == "ESP_TX":
            descriptor = "ESP32 co-processor transmit to MCU"
        elif item == "ESP_RX":
            descriptor = "ESP32 co-processor receive from MCU"
        elif item == "ESP_GPIO0":
            descriptor = "ESP32 boot select"


        # Other pins
        elif item == "VOLTAGE_MONITOR":
            descriptor = "Supply voltage monitor"
        elif item == "BATTERY":
            descriptor = "Battery voltage monitor"
        elif item == "VBUS_SENSE":
            descriptor = "USB VBUS power detection"
        elif item == "SMPS_MODE":
            descriptor = "Switched-Mode Power Supply control"
        elif item == "BOOT0":
            descriptor = "Bootloader select"

        # SD card
        elif item == "SD_CS":
            descriptor = "SD card SPI CS"
        elif item == "SD_CARD_DETECT":
            descriptor = "SD card detection"

        # Camera
        elif item == "CAMERA_VSYNC":
            descriptor = "Camera vertical sync signal"
        elif item == "CAMERA_HSYNC":
            descriptor = "Camera horizontal sync signal"

        elif item == "CAMERA_HREF":
            descriptor = "Camera horizontal reference"
        elif item == "CAMERA_XCLK":
            descriptor = "Camera external clock"
        elif item == "CAMERA_PCLK":
            descriptor = "Camera pixel clock"
        elif item == "CAMERA_PWDN":
            descriptor = "Camera power down"
        elif item == "CAMERA_DATA2":
            descriptor = "Camera horizontal sync signal"
        elif item == "CAMERA_RESET":
            descriptor="Camera reset"
        elif item.startswith("CAMERA_DATA"):
            descriptor = "Camera data"

        else:
            descriptor = ""
        print(f"\t{item: <{COLUMN1_WIDTH}} {descriptor:<{COLUMN1_WIDTH}}")


def get_microcontroller_pins():
    """Show microcontroller pin details"""

    print("\n=== microcontroller pins ===\n")

    import microcontroller

    print("Microcontroller pins:")
    for pin in dir(microcontroller.pin):
        print("\t" + pin)

def get_matching_pins():
    """Show how microprocessor and board pins match up"""

    print("\n=== pin name info ===\n")

    import microcontroller

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

# A function to check for a pin
# First param is the pin name
# Second param is a descriptor of the pin, which is shown in the REPL when it checks for the pin.
# If you're using a board not made by Adafruit, you can use this function to search for non-standard pin names.
def check_for_pin(pin):
    """Check for a pin in board module.
    If you're using a board not made by Adafruit, you can use this function to search for non-standard pin names.
    You can 'import board' and then dir(board) to see what pins your board has."""

    if hasattr(board, pin):
        pin_detected = True
    else:
        pin_detected = False
    print(pin,  pin_detected)
    return pin_detected
