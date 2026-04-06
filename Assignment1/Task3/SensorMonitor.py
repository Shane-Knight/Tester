try:
    from sense_hat import SenseHat
except ImportError:
    from sense_emu import SenseHat

import time
import json

sense = SenseHat()

# load thresholds from config file
with open("enviro_config.json") as f:
    thresholds = json.load(f)

TEMP_OFFSET   = 2.0
POLL_INTERVAL = 10

def classify_environment(reading, threshold):
    if reading < threshold["min"]:
        return "Low"
    elif reading > threshold["max"]:
        return "High"
    else:
        return "Comfortable"

def classify_orientation(angle, threshold):
    if threshold["min"] <= angle <= threshold["max"]:
        return "Aligned"
    else:
        return "Tilted"

def read_sensors():
    temperature = round(sense.get_temperature() - TEMP_OFFSET, 2)
    humidity    = round(sense.get_humidity(), 2)
    pressure    = round(sense.get_pressure(), 2)

    orientation = sense.get_orientation()
    pitch = orientation["pitch"]
    roll  = orientation["roll"]
    yaw   = orientation["yaw"]

    if pitch > 180:
        pitch -= 360
    if roll > 180:
        roll -= 360

    pitch = round(pitch, 2)
    roll  = round(roll,  2)
    yaw   = round(yaw,   2)

    # print all readings with their status
    print(time.strftime("%H:%M:%S"))
    print("  temperature: " + str(temperature) + "  [" + classify_environment(temperature, thresholds["temperature"]) + "]")
    print("  humidity:    " + str(humidity)    + "  [" + classify_environment(humidity,    thresholds["humidity"])    + "]")
    print("  pressure:    " + str(pressure)    + "  [" + classify_environment(pressure,    thresholds["pressure"])    + "]")
    print("  pitch:       " + str(pitch)       + "  [" + classify_orientation(pitch, thresholds["orientation"]["pitch"]) + "]")
    print("  roll:        " + str(roll)        + "  [" + classify_orientation(roll,  thresholds["orientation"]["roll"])  + "]")
    print("  yaw:         " + str(yaw)         + "  [" + classify_orientation(yaw,   thresholds["orientation"]["yaw"])   + "]")

while True:
    read_sensors()
    time.sleep(POLL_INTERVAL)