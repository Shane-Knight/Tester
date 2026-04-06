import sqlite3
import pandas
from matplotlib import pyplot
import seaborn

class SensorAnalytics:
    def __init__(self):
        # load data from database
        connection = sqlite3.connect("../Task3/envirotrack.db")
        self.sensor_readings = pandas.read_sql_query("SELECT * FROM readings ORDER BY timestamp", connection)
        connection.close()

        print("Loaded " + str(len(self.sensor_readings)) + " readings")

        # convert timestamp so it plots properly
        self.sensor_readings["timestamp"] = pandas.to_datetime(self.sensor_readings["timestamp"])

        # bar colours based on status
        self.colour_map = {"Comfortable": "green", "High": "red", "Low": "blue"}

    def chart1_bar_charts(self):
    # matplotlib bar charts used here because they are good for showing discrete readings and comparing them with the thresholds
    # the colour of each bar changes based on status
    # 3 side by side subplots one for each environment
        fig, axes = pyplot.subplots(1, 3)
        fig.suptitle("Environmental Readings")

        # temperature
        temperature_bar_colours = [self.colour_map.get(status, "grey") for status in self.sensor_readings["temp_status"]]
        axes[0].bar(range(len(self.sensor_readings)), self.sensor_readings["temperature"], color=temperature_bar_colours)
        axes[0].set_title("Temperature (C)")
        # set y range to always show the thresholds and extending if any readings go outside them
        axes[0].set_ylim(min(self.sensor_readings["temperature"].min(), 15) - 1, max(self.sensor_readings["temperature"].max(), 24) + 1)
        # dashed lines show the min and max acceptable values
        axes[0].axhline(y=15, color="black", linestyle="--", label="min 15")
        axes[0].axhline(y=24, color="black", linestyle="--", label="max 24")
        axes[0].legend()

        # humidity, all pretty much the same as temp
        humidity_bar_colours = [self.colour_map.get(status, "grey") for status in self.sensor_readings["hum_status"]]
        axes[1].bar(range(len(self.sensor_readings)), self.sensor_readings["humidity"], color=humidity_bar_colours)
        axes[1].set_title("Humidity (%)")
        # set y range to always show the thresholds and extending if any readings go outside them
        axes[1].set_ylim(min(self.sensor_readings["humidity"].min(), 30) - 1, max(self.sensor_readings["humidity"].max(), 65) + 1)
        axes[1].axhline(y=30, color="black", linestyle="--", label="min 30")
        axes[1].axhline(y=65, color="black", linestyle="--", label="max 65")
        axes[1].legend()

        # pressure same as above
        pressure_bar_colours = [self.colour_map.get(status, "grey") for status in self.sensor_readings["pres_status"]]
        axes[2].bar(range(len(self.sensor_readings)), self.sensor_readings["pressure"], color=pressure_bar_colours)
        axes[2].set_title("Pressure (hPa)")
        # set y range to always show the thresholds and extending if any readings go outside them
        axes[2].set_ylim(min(self.sensor_readings["pressure"].min(), 980) - 1, max(self.sensor_readings["pressure"].max(), 1030) + 1)
        axes[2].axhline(y=980,  color="black", linestyle="--", label="min 980")
        axes[2].axhline(y=1030, color="black", linestyle="--", label="max 1030")
        axes[2].legend()

        pyplot.savefig("chart1_sensor_bar_charts.png")
        pyplot.close()
        print("Saved chart1_sensor_bar_charts.png")

    def chart2_orientation(self):
    # seaborn line plot used here because it is good for showing trends over time and comparing multiple related variables pitch roll yaw
        seaborn.lineplot(data=self.sensor_readings, x="timestamp", y="pitch", label="Pitch")
        seaborn.lineplot(data=self.sensor_readings, x="timestamp", y="roll",  label="Roll")
        seaborn.lineplot(data=self.sensor_readings, x="timestamp", y="yaw",   label="Yaw")
        pyplot.title("Orientation Over Time")
        pyplot.xlabel("Time")
        pyplot.ylabel("Angle")
        pyplot.savefig("chart2_orientation_over_time.png")
        pyplot.close()
        print("Saved chart2_orientation_over_time.png")

    def run(self):
        self.chart1_bar_charts()
        self.chart2_orientation()


analytics = SensorAnalytics()
analytics.run()