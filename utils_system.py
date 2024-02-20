# By @howdymoto / Wright Bagwell
# Inspired by TodBot's circuitpython-tricks: https://github.com/todbot/circuitpython-tricks
# And by Adafruit/Kattni Rembor's CircuitPython Essentials: https://learn.adafruit.com/circuitpython-essentials/circuitpython-essentials
# MIT license

""" Helper functions for learning about your boards """

def get_os_info():
    """Show os module info. Includes CircuitPython version and filesystem info.
    Show details about storage and memory"""

    print("\n=== os module info ===\n")

    import os
    import gc

    boardNameOS = os.uname().machine
    print("Board name:\t", boardNameOS)

    print("System name (CPU):\t", os.uname().sysname)
    print("CircuitPython ver:\t", os.uname().release)
    print("Version:\t\t", os.uname().version)

    free_memory = gc.mem_free() / 1024
    allocated_memory = gc.mem_alloc() / 1024
    total_memory = allocated_memory + free_memory

    print("Free memory:\t", free_memory, "KB")
    print("Total memory:\t", total_memory, "KB")

    fs_stat = os.statvfs('/')

    print("Disk size:\t", fs_stat[0] * fs_stat[2] / 1024, "KB")
    print("Disk free space:\t", fs_stat[0] * fs_stat[3] / 1024, "KB")

    # statvfs
    print("statvfs /")
    print("\t", fs_stat)


def get_board_info():
    """Show all board module info.
    Mostly shows pin names, and then the board's named pins."""

    print("\n=== board module info ===\n")

    import board

    boardNameBoard = board.board_id

    print("Board name:\t", board.board_id)
    print("Board pins:")

    pins = dir(board)
    pins.sort()

    for item in pins:

        print("\t" + item)


def get_microcontroller_info():
    """Show microcontroller/CPU details"""

    print("\n=== microcontroller info ===\n")

    import os
    import microcontroller

    cpu_type_descriptor = "CPU:"
    cpu_type = os.uname().sysname
    print("CPU:\t\t", cpu_type)

    nvm_bytes = len(microcontroller.nvm) / 1024
    nvm_bytes_formatted = str(nvm_bytes) + " KB"
    print("NVM:\t\t", nvm_bytes_formatted)

    cpu_frequency_unformatted = microcontroller.cpu.frequency / 1000000
    cpu_frequency =  f"{cpu_frequency_unformatted:,}" + " MHz"
    print("CPU 0 frequency:\t", cpu_frequency)

    cpu_temperature = microcontroller.cpu.temperature
    if cpu_temperature == None:
        cpu_temperature = "Not available"
    print("CPU 0 temperature:\t", cpu_temperature)

    cpu_voltage = microcontroller.cpu.voltage
    if cpu_voltage == None:
        cpu_voltage = "Not available"
    print("CPU 0 voltage:\t", cpu_voltage)

    print("Microcontroller pins:")
    for pin in dir(microcontroller.pin):
        print("\t" + pin)


def get_builtin_modules():
    """List all this board's built-in CircuitPython modules"""

    print("\nBuilt-in modules:\n")
    help("modules")
