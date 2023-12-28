import os
import wifi

CPUTILS_STRING = 'CPUTILS:'

def connect_wifi(ssid=os.getenv("CIRCUITPY_WIFI_SSID"), password=os.getenv("CIRCUITPY_WIFI_PASSWORD")):
    print(CPUTILS_STRING, "Connecting to WiFi...")
    print("\tssid:", ssid)
    print("\tpassword:", password)

    # TODO: Help the user understand what to do if they don't specify an SSID and pwd,
    # and do not have a settings.toml file set up.

    try:
        wifi.radio.connect(ssid, password)
        print("\tConnected to", ssid)
    except Exception as e:
        print("\tFailed to connect to WiFi:", e)
    return


def scan_wifi_networks():
    print(CPUTILS_STRING, "Scanning for WiFi networks...")

    # TODO: make this take longer to find all the local Netowrks

    networks = []
    for network in wifi.radio.start_scanning_networks():
        networks.append(network)
    wifi.radio.stop_scanning_networks()
    networks = sorted(networks, key=lambda net: net.rssi, reverse=True)
    for network in networks:
        print("\t", network.ssid, "\t\trssi:", network.rssi)
    return networks

def test_wifi():
    print(CPUTILS_STRING, "Testing Wifi connection...")
    #TODO: abort if not connected to Wifi

    print("\tIP:", wifi.radio.ipv4_address)
    print("\tMAC address:", wifi.radio.mac_address)
    print("\tDNS server:", wifi.radio.ipv4_dns)
    print("\tGateway:", wifi.radio.ipv4_gateway)
    print("\tSubnet:", wifi.radio.ipv4_subnet)

    ip_to_ping = "1.1.1.1"
    print("\tPinging", ip_to_ping)

    try:
        # TODO ping test
        for i in range(5):
            print("\tping:", wifi.radio.ping(ip_to_ping))
            time.sleep(1)
    except Exception as e:
        print("\tPing failed:", e)

    print("\tMaking HTTP request...")
    import socketpool
    import ssl
    import adafruit_requests
    import json
    pool = socketpool.SocketPool(wifi.radio)
    context = ssl.create_default_context()
    try:
        url = "http://httpbin.org/get"
        http = adafruit_requests.Session(pool, context)
        response = http.get(url)
        print("\tResponse:", response.text)
        data = json.loads(response.text)
        message = data.get("origin", "No message found")
        print("\tRetrieved message:", message)
    except Exception as e:
        print("\tFailed to request data from", url, e)

    print("\tTesting connection speed...")
    try:
        print("\tTODO: Pladceholder bandwidth test...")
    except Exception as e:
        print("\tFailed to perform bandwidth test", e)
    return
