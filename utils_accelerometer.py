import time
import board
import adafruit_lis3dh

# TODO Define enum for types of output formats, such as:
# Raw values
# Raw values divided by -9.8 to give you Gs
# Clamped values

def print_values(lis3dh: adafruit_lis3dh.lis3dh, format="G"):
    # lis3dh.acceleration reports values in m / s ^ 2.
    # Returns a 3-tuple of x, y, z axis values.
    # Divide them by adafruit_lis3dh.STANDARD_GRAVITY (9.806) to convert to Gs.

    x, y, z = [ value / adafruit_lis3dh.STANDARD_GRAVITY for value in lis3dh.acceleration]
    print("x= %0.3f G, y= %0.3f G, z= %0.3f G" % (x, y, z))
