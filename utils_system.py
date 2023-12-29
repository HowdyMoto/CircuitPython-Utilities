import os
import gc
import board

CPUTILS_STRING = 'CP UTILS:'

def print_board_info():
    print(CPUTILS_STRING, "Getting board details...")

    # Board name
    print("\t" + os.uname().machine)
    # CPU name
    print("\t" + os.uname().sysname)
    # CircuitPython version
    print("\tCircuitPython version:" + os.uname().release)
    fs_stat = os.statvfs('/')
    print("\tDisk size:", "\t", fs_stat[0] * fs_stat[2] / 1024 / 1024, "\tMB")
    print("\tFree space:", "\t", fs_stat[0] * fs_stat[3] / 1024 / 1024, "\tMB")
    free_memory = gc.mem_free() / 1024 / 1024
    print("\tFree memory:", "\t", f"{free_memory:,}", "\tMB" )

    # See if the board has a display. If so, show details.
    if hasattr(board, 'DISPLAY'):
        display = board.DISPLAY
        print(
            "\tDisplay size:\t",
            display.width,
            "x",
            display.height
        )
        print("\tDisplay rotation:\t", display.rotation)
        print("\tDisplay bus:", display.bus)
        # Some displays, like epaper, do not have an auto-refresh property
        if hasattr(display, 'auto_refresh'):
            print("\t Display auto_refresh:", display.auto_refresh)
        # Some displays, like epaper, do not have a brightness property
        if hasattr(display, 'brightness'):
            print("\tDisplay brightness:", display.brightness)
    else:
        print("\tNo display detected")
    i2c_device_scan()

def i2c_device_scan():
    i2c = board.I2C()
    print(CPUTILS_STRING, "Scanning I2C bus for devices")
    if not i2c.try_lock():
        pass
    i2c_addresses = i2c.scan()
    if len(i2c_addresses) == 0:
        print("No I2C devices found")
    else:
        print("\tI2C device(s) found at:")
        for address in i2c_addresses:
            print("\t", hex(address))
    i2c.unlock()
