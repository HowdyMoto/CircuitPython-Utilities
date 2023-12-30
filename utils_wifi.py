import os
import wifi

# These utils will print hepful info to the REPL
# For readability, function calls start by printing this string
# Data printed inside each function indented with \t for readability
CPUTILS_STRING = 'CP UTILS:'

# =======================================
# Connect to Wifi
# If user doesn't specify SSID and password, it's taken from settings.toml
def connect_wifi(
        ssid=os.getenv("CIRCUITPY_WIFI_SSID"),
        password=os.getenv("CIRCUITPY_WIFI_PASSWORD")
    ):
    print(CPUTILS_STRING, "Connecting to WiFi...")
    print("\tssid:", ssid)
    print("\tpassword:", password)

    # TODO: Help the user understand what to do if they don't specify an SSID and pwd,
    # and do not have a settings.toml file set up.
    if len(ssid) == 0:
        print(
            "No SSID specified",
            "Either specify in connect_wifi(),",
            "or specify one in settings.toml",
            "Please see https://docs.circuitpython.org/en/latest/docs/environment.html"
        )

    try:
        wifi.radio.connect(ssid, password)
        print("\tSuccessfully connected")
    except Exception as e:
        print("\tFailed to connect:", e)
    return

# =======================================
# Look for available WiFI networks (SSIDs)
# Then, print each found SSID and RSSI (Strength)
# Finally, return an array of SSIDs and RSSIs
def scan_wifi_networks():
    print(CPUTILS_STRING, "Scanning for WiFi networks...")

    networks = []
    for network in wifi.radio.start_scanning_networks():
        networks.append(network)
    wifi.radio.stop_scanning_networks()
    networks = sorted(networks, key=lambda net: net.rssi, reverse=True)
    for network in networks:
        print("\t", network.ssid, "\t\trssi:", network.rssi)
    return networks

# =======================================
# Print info about current WiFi network connection to the REPL.
# Then, try a few network operations to verify it's working reliably.
def test_wifi():
    print(CPUTILS_STRING, "Testing Wifi connection...")

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
    
    # Second, ping 8.8.8.8 - the primary DNS server for Google DNS
    import ipaddress
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
        print("\t"+ "-" * 40)
        print("\t"+ response.text)
        print("\t"+ "-" * 40)
    except Exception as e:
        print("\tFailed to request data from", TEXT_URL, e)

# =======================================
# Download a ~1MB file to test speed
def test_bandwidth():
    print(CPUTILS_STRING, "Testing download bandwidth...")

    # Abort if not connected to Wifi
    if not wifi.radio.enabled:
        print("\tWifi radio disabled")
        return
    if not wifi.radio.connected:
        print("\tNot connected to WiFi")
        return

    import time
    import socketpool
    import ssl
    import adafruit_requests

    pool = socketpool.SocketPool(wifi.radio)
    context = ssl.create_default_context()
    requests = adafruit_requests.Session(pool, context)

    FILE_DOWNLOAD_URL = 'https://freetestdata.com/wp-content/uploads/2023/04/1.17-MB.bmp'

    start_time = time.monotonic()
    try:
        print("HTTP request for file...")
        response = requests.get(FILE_DOWNLOAD_URL)
        if response.status_code == 200:
            print("Success! HTTP code 200")
            # Calculate download speed
            end_time = time.monotonic()
            duration = end_time - start_time    # Time taken for download in seconds
            data_length = len(response.content)  # Length of data in bytes
            speed_bps = data_length / duration  # Speed in bytes per second

            print("Downloaded", data_length, "bytes in", duration, "seconds.")
            print("Download speed:", speed_bps, "Bytes per second.")
        else:
            print("Failed to download test file. Status code:", response.status_code)
    except Exception as e:
        print("\HTTP request failed:", e)