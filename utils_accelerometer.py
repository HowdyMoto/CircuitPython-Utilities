"""Helper functions for reading accelerometer data.

Provides utilities for reading and formatting LIS3DH accelerometer values.
Work in progress - needs testing on more boards with built-in accelerometers.
"""

import time
import board
import adafruit_lis3dh

# TODO Define enum for types of output formats, such as:
# Raw values
# Raw values divided by -9.8 to give you Gs
# Clamped values

def print_values(lis3dh: adafruit_lis3dh.lis3dh, format="G"):
    """Print accelerometer values from a LIS3DH sensor.

    Reads acceleration data and prints x, y, z axis values converted to Gs.

    Args:
        lis3dh: An initialized adafruit_lis3dh.LIS3DH sensor object.
        format (str, optional): Output format. Currently only "G" (Gs) is
            supported. Defaults to "G".
    """

    x, y, z = [ value / adafruit_lis3dh.STANDARD_GRAVITY for value in lis3dh.acceleration]
    print("x= %0.3f G, y= %0.3f G, z= %0.3f G" % (x, y, z))
