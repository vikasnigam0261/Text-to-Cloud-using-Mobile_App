import wiotp.sdk.device
import time
import random
myConfig = { 
    "identity": {
        "orgId": "7jh6o2",
        "typeId": "VITDevice",
        "deviceId":"12345"
    },
    "auth": {
        "token": "12345678"
    }
}

def myCommandCallback(cmd):
    print("Message received from IBM IoT Platform: %s" % cmd.data['command'])
    

client = wiotp.sdk.device.DeviceClient(config=myConfig, logHandlers=None)
client.connect()

while True:
    client.commandCallback = myCommandCallback
    time.sleep(2)
client.disconnect()
