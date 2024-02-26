# By @howdymoto / Wright Bagwell
# Inspired by TodBot's circuitpython-tricks: https://github.com/todbot/circuitpython-tricks
# And by Adafruit/Kattni Rembor's CircuitPython Essentials: https://learn.adafruit.com/circuitpython-essentials/circuitpython-essentials
# MIT license

""" Helper functions for board pins """

import board

COLUMN1_WIDTH = 25

def get_board_pins2():
    """ Show pins from board module """
    print("\n=== board pin details ===\n")

    # Dictionary mapping pin name prefixes or exact names to descriptions
    pin_descriptions = {
        "LED": "Built-in LED",
        "WHITE_LEDS": "Built-in white LEDs",
        "NEOPIXEL": "Built-in Neopixel",
        "APA102_SCK": "Built-in DotStar LED Serial Clock",
        "APA102_MOSI":"Built-in DotStar LED Master Out Slave In",
        "DOTSTAR_CLOCK": "Built-in DotStar LED Serial Clock",
        "DOTSTAR_DATA": "Built-in DotStar color data",

        # I2C bus

        "STEMMA_I2C": "Stemma I2C Connector",
        "SCK": "I2C Serial Clock",

        # SPI bus
        "SPI": "SPI Bus",
        "MOSI": "SPI Master Out Slave In",
        "MISO": "SPI Master In Slave Out",
        "SS": "SPI Slave Select",
        "CS": "SPI Slave Select (alt name)",

        # UART
        "UART": "UART",
        "UART1": "UART",
        "UART2": "UART",
        "RX": "UART receive",
        "RX0": "UART receive",
        "RX1": "UART receive",
        "TX": "UART transmit",
        "TX0": "UART transmit",
        "TX1": "UART transmit",

        # Misc buttons
        "BUTTON": "Built-in button",
        "SLIDE_SWITCH": "Built-in switch",
        "POWER_SWITCH": "Built-in power switch",

        # Built-in Displau
        "DISPLAY": "Built-in display",

        # TFT display pins
        "TFT_BACKLIGHT": "TFT display backlight control",
        "TFT_CS":"TFT display chip select for SPI bus",
        "TFT_RS": "TFT register or display data/command select",
        "TFT_DC": "TFT register or display data/command select",
        "TFT_MOSI": "TFT display SPI Master Out Slave In",
        "TFT_RESET": "TFT display reset",
        "TFT_SCK": "TFT display SPI serial clock",
        "TFT_TE": "TFT tearing effect/prevention",
        "TFT_WR": "TFT display write",
        "TFT_RD": "TFT display read",

        # TFT pins on Qualia devices 
        "TFT_PINS": "GPIO connections for dot clock TFT displays",
        "TFT_TIMINGS": "TFT timings for single-display boards ",
        "TFT_INIT_SEQUENCE": "board's built in display initialization sequence",
        "TFT_IO_EXPANDER": "I/O expander, for when SPI bus is on an I2C I/O expander",

        # LCD display pins
        "LCD_BCKL": "LCD display backlight control",
        "LCD_CLK": "LCD display  SPI serial clock",
        "LCD_CS": "LCD display chip select",
        "LCD_D_C": "LCD display data/command select",
        "LCD_MOSI": "LCD display SPI Master Out Slave In",
        "LCD_RST": "LCD display reset",
        "LCD_DATA0": "LCD data",  
        "LCD_DATA1": "LCD data",                 
        "LCD_DATA2": "LCD data",                 
        "LCD_DATA3": "LCD data",                 
        "LCD_DATA4": "LCD data",                 
        "LCD_DATA5": "LCD data",                 
        "LCD_DATA6": "LCD data",                 
        "LCD_DATA7": "LCD data",                 

        # LCD pins
        "LCD_DATA": "LCD data",

        # E-ink display
        "EPD_BUSY": "E-ink display busy signal",
        "EPD_CS": "E-ink display chip select for SPI bus",
        "EPD_DC": "E-ink display data/command select",
        "EPD_MISO": "E-ink display SPI Master In Slave Out",
        "EPD_MOSI": "E-ink display SPI Master Out Slave In",
        "EPD_RESET": "E-ink display display reset",
        "EPD_SCK": "E-ink display display SPI serial clock",

        # Touchscreen pins
        "TOUCH_XL":"Touchscreen X left",
        "TOUCH_XR": "Touchscreen X right",
        "TOUCH_YD": "Touchscreen Y down",
        "TOUCH_YU": "Touchscreen Y up",

        # Audio in and out
        "SPEAKER": "Speaker output",
        "AUDIO_OUT": "Speaker output",
        "SPEAKER_ENABLE": "Speaker enable",
        "MICROPHONE_DATA": "Microphone PDM data",
        "MICROPHONE_CLOCK": "Microphone PDM clock",

        # Other misc sensors
        "LIGHT" : "Light sensor",
        "L" : "Light sensor",
        "TEMPERATURE": "Temperature sensor",

        # ESP32 co-processor pins
        "ESP_BUSY": "ESP32 co-processor busy status",
        "ESP_CS": "ESP32 co-processor SPI chip select",
        "ESP_RESET": "ESP32 co-processor reset",
        "ESP_RTS": "ESP32 co-processor request-to-send for UART",
        "ESP_TX": "ESP32 co-processor transmit to MCU",
        "ESP_RX": "ESP32 co-processor receive from MCU",
        "ESP_GPIO0": "ESP32 boot select",


        # Power pins
        "VOLTAGE_MONITOR": "Supply voltage monitor",
        "BATTERY": "Battery voltage monitor",
        "VBUS_SENSE": "USB VBUS power detection",
        "SMPS_MODE": "Switched-Mode Power Supply control",
        "PE_POWER": "Peripheral power",

        # Boot pins
        "BOOT0": "Bootloader select",

        # SD card
        "SD_CS": "SD card SPI chip select",
        "SD_CLK": "SD card SPI clock",
        "SD_CARD_DETECT": "SD card detection",
        "SD_MISO":"SD card SPI Master In Slave Out",
        "SD_MOSI": "SD card SPI Master Out Slave In",

        # Camera
        "CAMERA_VSYNC":"Camera vertical sync signal",
        "CAMERA_HSYNC": "Camera horizontal sync signal",
        "CAMERA_HREF": "Camera horizontal reference",
        "CAMERA_XCLK": "Camera external clock",
        "CAMERA_PCLK": "Camera pixel clock",
        "CAMERA_PWDN": "Camera power down",
        "CAMERA_RESET": "Camera reset",
        "CAMERA_DATA":"Camera data",
        "CAMERA_DATA2": "Camera data",

    }

    pins = dir(board)
    pins.sort()

    for item in pins:
        descriptor = ""  # Default to empty descriptor

        # First, check the dictionary for matching pin names
        for prefix, description in pin_descriptions.items():
            if item == prefix:
                descriptor = description
                break  # Break if a match is found

        # Then check for pins that can have multiple instances
        # UART pins
        if item.startswith("UART"):
                descriptor = "UART"  
        elif item.startswith("TX"):
            descriptor = "UART transmit"  
        elif item.startswith("RX"):
            descriptor = "UART receive"  
    
        # I2C 
        elif item.startswith("I2C"):
            descriptor = "I2C bus"  
        elif item.startswith("SCL"):
            descriptor = "I2C serial clock line"  
        elif item.startswith("SDA"):
            descriptor = "I2C serial data line" 
        
        # Buttons
        elif item.startswith("BUTTON"):
            descriptor = "Built-in button"
        
        # LCD pins
        elif item.startswith("LCD_DATA"):
            descriptor = "LCD data"

        # then check for generic A and D pins
        elif len(item) >= 2 and item[0] == "A" and item[1].isdigit():
            descriptor = "Generic analog pin"
        elif len(item) >= 2 and item[0] == "D" and item[1].isdigit():
            descriptor = "Generic digital pin"
        
        print(f"\t{item: <{COLUMN1_WIDTH}} {descriptor}")

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

# Check for a specific pin
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