try:
    from sense_hat import SenseHat
except ImportError:
    from sense_emu import SenseHat

import time
import json
import sqlite3

sense = SenseHat()

# load thresholds from config file
with open("enviro_config.json") as f:
    thresholds = json.load(f)

TEMP_OFFSET = 2.0
POLL_INTERVAL = 10
DB_NAME = "envirotrack.db"

# colours for LED display
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
AMBER = (255, 165, 0)

def get_status_colour(status):
    if status == "Comfortable" or status == "Aligned":
        return GREEN
    elif status == "High":
        return RED
    elif status == "Low":
        return BLUE
    else:
        return AMBER

# create the database and table if they dont already exist
def create_db():
    con = sqlite3.connect(DB_NAME)
    with con:
        con.execute("""
            CREATE TABLE IF NOT EXISTS readings (
                timestamp DATETIME DEFAULT (datetime('now')),
                temperature REAL,
                temp_status TEXT,
                humidity REAL,
                hum_status TEXT,
                pressure REAL,
                pres_status TEXT,
                pitch REAL,
                pitch_status TEXT,
                roll REAL,
                roll_status TEXT,
                yaw REAL,
                yaw_status TEXT
            )
        """)

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
    # offset tempt
    temperature = round(sense.get_temperature() - TEMP_OFFSET, 2)
    humidity = round(sense.get_humidity(), 2)
    pressure = round(sense.get_pressure(), 2)

    orientation = sense.get_orientation()
    pitch = orientation["pitch"]
    roll = orientation["roll"]
    yaw = orientation["yaw"]

    # change pitch and roll from 0-360 to -180 to 180
    if pitch > 180:
        pitch -= 360
    if roll > 180:
        roll -= 360

    pitch = round(pitch, 2)
    roll = round(roll, 2)
    yaw = round(yaw, 2)

    # store each reading as touple
    sensor_data = {
        "temperature": (temperature, classify_environment(temperature, thresholds["temperature"])),
        "humidity": (humidity, classify_environment(humidity, thresholds["humidity"])),
        "pressure": (pressure, classify_environment(pressure, thresholds["pressure"])),
        "pitch": (pitch, classify_orientation(pitch, thresholds["orientation"]["pitch"])),
        "roll": (roll, classify_orientation(roll, thresholds["orientation"]["roll"])),
        "yaw": (yaw, classify_orientation(yaw, thresholds["orientation"]["yaw"])),
    }

    # save reading to the database
    con = sqlite3.connect(DB_NAME)
    con.execute(
        "INSERT INTO readings (temperature, temp_status, humidity, hum_status, pressure, pres_status, pitch, pitch_status, roll, roll_status, yaw, yaw_status) VALUES (" +
        str(temperature) + ", '" + sensor_data["temperature"][1] + "', " +
        str(humidity) + ", '" + sensor_data["humidity"][1] + "', " +
        str(pressure) + ", '" + sensor_data["pressure"][1] + "', " +
        str(pitch) + ", '" + sensor_data["pitch"][1] + "', " +
        str(roll) + ", '" + sensor_data["roll"][1] + "', " +
        str(yaw) + ", '" + sensor_data["yaw"][1] + "')"
    )
    con.commit()
    con.close()

    print(time.strftime("%H:%M:%S"))
    print("  temperature: " + str(temperature) + "  [" + sensor_data["temperature"][1] + "]")
    print("  humidity: " + str(humidity) + "  [" + sensor_data["humidity"][1] + "]")
    print("  pressure: " + str(pressure) + "  [" + sensor_data["pressure"][1] + "]")
    print("  pitch: " + str(pitch) + "  [" + sensor_data["pitch"][1] + "]")
    print("  roll: " + str(roll) + "  [" + sensor_data["roll"][1] + "]")
    print("  yaw: " + str(yaw) + "  [" + sensor_data["yaw"][1] + "]")

    return sensor_data

def show_on_led(sensor_data):
    displays = [
        ("T:", "temperature"),
        ("H:", "humidity"),
        ("P:", "pressure"),
        ("Pi:", "pitch"),
        ("R:", "roll"),
        ("Y:", "yaw"),
    ]
    for label, key in displays:
        value, status = sensor_data[key]
        colour = get_status_colour(status)
        sense.show_message(label + str(int(round(value))), text_colour=colour, scroll_speed=0.05)

# create db on startup
create_db()

while True:
    data = read_sensors()
    show_on_led(data)