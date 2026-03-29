try:
    from sense_hat import SenseHat
except ImportError:
    from sense_emu import SenseHat

import math

sense = SenseHat()

# default value
x = 16


sense.show_message(str(x))

while True:
    for event in sense.stick.get_events():
        if event.action != "pressed":
            continue

        if event.direction == "up":
            pass

        elif event.direction == "down":
            pass

        elif event.direction == "left":
            pass

        elif event.direction == "right":
            pass

        elif event.direction == "middle":
            pass

    sense.show_message(str(x))