import os
import gc

CPUTILS_STRING = 'CPUTILS:'

def print_board():
    print(CPUTILS_STRING, "Getting board details...")
    print("\t" + os.uname().machine)
    print("\t" + os.uname().sysname)
    print("\t" + os.uname().release)
    fs_stat = os.statvfs('/')
    print("\tDisk size:", "\t", fs_stat[0] * fs_stat[2] / 1024 / 1024, "\tMB")
    print("\tFree space:", "\t", fs_stat[0] * fs_stat[3] / 1024 / 1024, "\tMB")
    free_memory = gc.mem_free() / 1024 / 1024
    print("\tFree memory:", "\t", f"{free_memory:,}", "\tMB" )
