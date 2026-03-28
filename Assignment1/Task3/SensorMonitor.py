try:
    from sense_hat import SenseHat
except ImportError:
    from sense_emu import SenseHat

import time
import json
import sqlite3

TEMP_OFFSET = 2.0
POLL_INTERVAL = 10
DB_NAME = "envirotrack.db"

# colours for LED display
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
AMBER = (255, 165, 0)

# update for OOP style code
class SensorMonitor:
    def __init__(self):
        self.sense = SenseHat()
        self.is_paused = False
        self.latest_sensor_data = None
        # load thresholds from config file
        self.thresholds = json.load(open("enviro_config.json"))

        print("Database path: " + os.path.abspath(DB_NAME))
        self.create_db()

    def get_status_colour(self, status):
        # return a colour based on the status string
        if status == "Comfortable" or status == "Aligned":
            return GREEN
        elif status == "High":
            return RED
        elif status == "Low":
            return BLUE
        else:
            return AMBER

# create the database and table if they dont already exist
    def create_db(self):
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

    def classify_environment(self, reading, threshold):
        # compare reading against min/max from config
        if reading < threshold["min"]:
            return "Low"
        elif reading > threshold["max"]:
            return "High"
        else:
            return "Comfortable"

    def classify_orientation(self, angle, threshold):
        # check if angle is within the range
        if threshold["min"] <= angle <= threshold["max"]:
            return "Aligned"
        else:
            return "Tilted"

    def read_sensors(self):
        # offset tempt
        temperature = round(self.sense.get_temperature() - TEMP_OFFSET, 2)
        humidity = round(self.sense.get_humidity(), 2)
        pressure = round(self.sense.get_pressure(), 2)

        orientation = self.sense.get_orientation()
        pitch = orientation["pitch"]
        roll = orientation["roll"]
        yaw = orientation["yaw"]

    # change pitch and roll from 0-360 to -180 to 180
        if pitch > 180:
            pitch -= 360
        if roll > 180:
            roll -= 360

        # store each reading as a tuple of (value, status)
        sensor_data = {
            "temperature": (temperature, self.classify_environment(temperature, self.thresholds["temperature"])),
            "humidity": (humidity, self.classify_environment(humidity, self.thresholds["humidity"])),
            "pressure": (pressure, self.classify_environment(pressure, self.thresholds["pressure"])),
            "pitch": (pitch, self.classify_orientation(pitch, self.thresholds["orientation"]["pitch"])),
            "roll": (roll, self.classify_orientation(roll, self.thresholds["orientation"]["roll"])),
            "yaw": (yaw, self.classify_orientation(yaw, self.thresholds["orientation"]["yaw"])),
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

    def show_on_led(self, sensor_data):
        # scroll each reading across the LED with its colour
        displays = [
            ("T:", "temperature"),
            ("H:", "humidity"),
            ("P:", "pressure"),
            ("Pi:", "pitch"),
            ("R:", "roll"),
            ("Y:", "yaw"),
        ]
        for label, key in displays
    # for each display slot scroll the label and value across the LED in the status colour:
            value, status = sensor_data[key]
            colour = self.get_status_colour(status)
            self.sense.show_message(label + str(int(value)), text_colour=colour, scroll_speed=0.05)

    def run(self):
        while True:
            self.latest_sensor_data = self.read_sensors()
            self.show_on_led(self.latest_sensor_data)


monitor = SensorMonitor()
monitor.run()