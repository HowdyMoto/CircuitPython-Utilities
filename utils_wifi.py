# utils_wifi.py -- Helper functions for wifi
# By @howdymoto / Wright Bagwell
# Inspired by TodBot's circuitpython-tricks: https://github.com/todbot/circuitpython-tricks
# And by Adafruit/Kattni Rembor's CircuitPython Essentials: https://learn.adafruit.com/circuitpython-essentials/circuitpython-essentials
# MIT license

import os
import wifi
import ipaddress

# Connect to Wifi
# CircuitPython 9 and greater will automatically connect to Wi-Fi if settings.toml has SSID and password.
# You can use this to manually connect to a wifi network.
# If you call this without specifying SSID and password, attempt to read it from settings.toml
def connect_wifi(
        ssid=os.getenv("CIRCUITPY_WIFI_SSID"),
        password=os.getenv("CIRCUITPY_WIFI_PASSWORD")
    ):
    print("=== Connecting to WiFi... ===")

    if wifi.radio.connected:
        print(f"Already connected to Wi-Fi.\nIP Address: {wifi.radio.ipv4_address}")

    # If user doesn't specify ssid/pwd in the function call,
    # they should specify it in settings.toml
    if ssid is None or len(ssid) == 0:
        print(
            "\tNo SSID specified\n",
            "\tEither specify in connect_wifi(),\n",
            "\tor specify one in settings.toml\n",
            "\tPlease see https://docs.circuitpython.org/en/latest/docs/environment.html"
        )
        return
    try:
        print("\tAttempting to connect to", ssid)
        wifi.radio.connect(ssid, password)
        print("\tSuccessfully connected")
    except Exception as e:
        print("\tFailed to connect:", e)
    return


# Look for available WiFI networks (SSIDs)
# Sort by RSSI (signal strength)
# Then, print each found SSID and RSSI
# Finally, return an array of SSIDs and RSSIs
def get_wifi_networks():
    print("=== Scanning for WiFi networks... ===")

    networks = list(wifi.radio.start_scanning_networks())  # Convert to list immediately
    wifi.radio.stop_scanning_networks()

    if not networks:
            print("\tNo Wi-Fi networks found!")
            return []

    networks.sort(key=lambda net: net.rssi, reverse=True)
    for network in networks:
        print("\t", network.ssid, "\t\trssi:", network.rssi, "dBm")
    
    return networks


# Print info about current WiFi network connection to the REPL.
# Then, try a few network operations to verify it's working reliably.
def test_wifi():
    print("=== Testing Wifi connection... ===")

    # Don't bother with tests if not connected to Wifi
    if not wifi.radio.enabled:
        print("\tWifi radio disabled")
        return
    if not wifi.radio.connected:
        print("\tNot connected to WiFi")
        return

    # First, print details about the radio and connection
    print("\tIP:", wifi.radio.ipv4_address)
    mac_address_raw = wifi.radio.mac_address
    mac_formatted = '-'.join(['{:02X}'.format(byte) for byte in mac_address_raw])
    print("\tMAC address:", mac_formatted)
    print("\tDNS server:", wifi.radio.ipv4_dns)
    print("\tGateway:", wifi.radio.ipv4_gateway)
    print("\tSubnet:", wifi.radio.ipv4_subnet)
    print("\tAP Authmode:", wifi.radio.ap_info.authmode)
    print("\tAP SSID:", wifi.radio.ap_info.ssid)
    bssid_raw = wifi.radio.ap_info.bssid
    bssid_formatted = '-'.join(['{:02X}'.format(byte) for byte in bssid_raw])
    print("\tAP BSSID:", bssid_formatted)
    print("\tAP Channel:", wifi.radio.ap_info.channel)
    print("\tAP Country:", wifi.radio.ap_info.country)
    print("\tAP RSSI:", wifi.radio.ap_info.rssi)

    # Second, ping the primary DNS server for Google DNS
    PING_IP = ipaddress.IPv4Address("8.8.8.8")
    ping = wifi.radio.ping(ip=PING_IP)
    if ping is None:
        print("\tCouldn't ping 'google.com' successfully")
    else:
        print("\tPinging 'google.com' took:", ping * 1000, "ms")

    # Third, get some text via HTTP request and print it
    TEXT_URL = "http://wifitest.adafruit.com/testwifi/index.html"
    print("\tHTTP Request from", TEXT_URL)
    import socketpool
    import ssl
    import adafruit_requests
    pool = socketpool.SocketPool(wifi.radio)
    context = ssl.create_default_context()
    requests = adafruit_requests.Session(pool, context)
    try:
        response = requests.get(TEXT_URL)
        if response.content:
            print("\t"+ "HTTP Response successfully received!")
        else:
            print("\t\tSuccessful request, but empty response")
    except Exception as e:
        print("\tFailed to request data from", TEXT_URL, e)
