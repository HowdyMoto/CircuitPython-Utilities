#import i2c

CPUTILS_STRING = 'CPUTILS -'

# TODO Set up speeds enums/consts
# 100_000
# 200_000
# 400_000
# 1_000_0000

def i2c_device_scan(i2c: I2C):
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
