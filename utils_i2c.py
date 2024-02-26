# By @howdymoto / Wright Bagwell
# Inspired by TodBot's circuitpython-tricks: https://github.com/todbot/circuitpython-tricks
# And by Adafruit/Kattni Rembor's CircuitPython Essentials: https://learn.adafruit.com/circuitpython-essentials/circuitpython-essentials
# MIT license

""" Helper functions for i2c bus and devices """

def get_i2c_info():
    """Look for I2C and STEMMA QT I2C pins on the board.
    STEMMA_I2C pin often indicates a solderless connector for connecting devices, but not always.
    On some boards, I2C and STEMMA_I2C are the same pins, which we check for here."""

    print("\n=== i2c info ===\n")
    print("i2c pins found:")

    import board

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
            print(f"\t{item}\t{descriptor}")

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
