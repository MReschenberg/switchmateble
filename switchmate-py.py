import bleak

ON_OFF_HANDLE = 45
BATTERY_HANDLE = 13
ON_ARRAY = bytearray(b'\x01')
OFF_ARRAY = bytearray(b'\x00')

# This class expects you pass a device using an externally created bluetooth scanner
# see https://developers.home-assistant.io/docs/bluetooth/
class SwitchmateWrapper:
    def __init__(self, device, mac):
        self.device = device
        self.mac = mac
        self.client = bleak.BleakClient(self.device)
        self.client.connect()

    def get_state(self):
        if (!self.client.is_connected()):
            self.client.connect()
        
        turned_on = client.read_gatt_char(ON_OFF_HANDLE) == ON_ARRAY
        log.info(f"current client is on: {turned_on}\n")
        
    def turn_on(self):
        if (!self.client.is_connected()):
            self.client.connect()

        client.write_gatt_char(ON_OFF_HANDLE, ON_ARRAY)
        log.info("turned on")

    def turn_off(self):
        if (!self.client.is_connected()):
            self.client.connect()

        client.write_gatt_char(ON_OFF_HANDLE, OFF_ARRAY)
        log.info("turned off")

    def get_battery_level(self):
        if (!self.client.is_connected()):
            self.client.connect()

        level = ord(client.read_gatt_char(BATTERY_HANDLE))
        log.info(f"battery level is {level}\n")


 
