import sqlite3
import pandas
from matplotlib import pyplot
import seaborn
 
# connect to the database
connection = sqlite3.connect("../Task3/envirotrack.db")
sensor_readings = pandas.read_sql_query("SELECT * FROM readings", connection)
connection.close()
 
print("Loaded " + str(len(sensor_readings)) + " readings")
 
# convert timestamp to datetime
sensor_readings["timestamp"] = pandas.to_datetime(sensor_readings["timestamp"])
 
# chart 1 bar chart of temperature readings
pyplot.bar(range(len(sensor_readings)), sensor_readings["temperature"])
pyplot.title("Temperature")
pyplot.savefig("chart1_temperature.png")
pyplot.close()
print("Saved chart1_temperature.png")

#add humidity and pressure to chart 1


 
# chart 2 - line plot of orientation over time
seaborn.lineplot(data=sensor_readings, x="timestamp", y="pitch", label="Pitch")
seaborn.lineplot(data=sensor_readings, x="timestamp", y="roll",  label="Roll")
seaborn.lineplot(data=sensor_readings, x="timestamp", y="yaw",   label="Yaw")
pyplot.title("Orientation Over Time")
pyplot.savefig("chart2_orientation.png")
pyplot.close()
print("Saved chart2_orientation.png")