import sqlite3
import pandas
from matplotlib import pyplot
import seaborn

# connect to the database and pull readings 
connection = sqlite3.connect("../Task3/envirotrack.db")
sensor_readings = pandas.read_sql_query("SELECT * FROM readings ORDER BY timestamp", connection)
connection.close()
 
print("Loaded " + str(len(sensor_readings)) + " readings")

# convert timestamp to datetime so matplotlib can use it on the x axis
sensor_readings["timestamp"] = pandas.to_datetime(sensor_readings["timestamp"])

# colour code bars based on their classification status
colour_map = {"Comfortable": "green", "High": "red", "Low": "blue"}

# Chart 1: bar charts for temperature, humidity and pressure
# matplotlib bar charts used here because they are good for showing discrete readings and comparing them to thresholds
# the colour of each bar changes based on status
# create 3 side by side subplots one for each environmental parameter
fig, axes = pyplot.subplots(1, 3, figsize=(12, 4))
fig.suptitle("Environmental Readings")

# temperature build a list of colours based on each readings status
temperature_bar_colours = [colour_map.get(status, "grey") for status in sensor_readings["temp_status"]]
axes[0].bar(range(len(sensor_readings)), sensor_readings["temperature"], color=temperature_bar_colours)
axes[0].set_title("Temperature (C)")
# set y range to always show the thresholds and extending if any readings go outside them
axes[0].set_ylim(min(sensor_readings["temperature"].min(), 15) - 1, max(sensor_readings["temperature"].max(), 24) + 1)
# dashed lines show the min and max acceptable values
axes[0].axhline(y=15, color="black", linestyle="--", label="min 15")
axes[0].axhline(y=24, color="black", linestyle="--", label="max 24")
axes[0].legend()

# humidity
humidity_bar_colours = [colour_map.get(status, "grey") for status in sensor_readings["hum_status"]]
axes[1].bar(range(len(sensor_readings)), sensor_readings["humidity"], color=humidity_bar_colours)
axes[1].set_title("Humidity (%)")
# set y range to always show the thresholds and extending if any readings go outside them
axes[1].set_ylim(min(sensor_readings["humidity"].min(), 30) - 1, max(sensor_readings["humidity"].max(), 65) + 1)
axes[1].axhline(y=30, color="black", linestyle="--", label="min 30")
axes[1].axhline(y=65, color="black", linestyle="--", label="max 65")
axes[1].legend()

# pressure
pressure_bar_colours = [colour_map.get(status, "grey") for status in sensor_readings["pres_status"]]
axes[2].bar(range(len(sensor_readings)), sensor_readings["pressure"], color=pressure_bar_colours)
axes[2].set_title("Pressure (hPa)")
# set y range to always show the thresholds and extending if any readings go outside them
axes[2].set_ylim(min(sensor_readings["pressure"].min(), 980) - 1, max(sensor_readings["pressure"].max(), 1030) + 1)
axes[2].axhline(y=980,  color="black", linestyle="--", label="min 980")
axes[2].axhline(y=1030, color="black", linestyle="--", label="max 1030")
axes[2].legend()

pyplot.tight_layout()
pyplot.savefig("chart1_sensor_bar_charts.png", dpi=150)
pyplot.close()
print("Saved chart1_sensor_bar_charts.png")

# Chart 2: angle over time
# seaborn line plot used here because it is good for showing trends over time and comparing multiple related variables pitch roll yaw
pyplot.figure(figsize=(10, 5))
seaborn.lineplot(data=sensor_readings, x="timestamp", y="pitch", label="Pitch")
seaborn.lineplot(data=sensor_readings, x="timestamp", y="roll",  label="Roll")
seaborn.lineplot(data=sensor_readings, x="timestamp", y="yaw",   label="Yaw")
pyplot.title("Orientation Over Time")
pyplot.xlabel("Time")
pyplot.ylabel("Angle")
pyplot.savefig("chart2_orientation_over_time.png", dpi=150)
pyplot.close()
print("Saved chart2_orientation_over_time.png")