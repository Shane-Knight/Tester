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

        # x+ 1
        if event.direction == "up":
            x += 1
            pass

        # x - 1
        elif event.direction == "down":
            x -= 1
            pass

        # x squared
        elif event.direction == "left":
            x = x ** 2
            pass

        # x square root
        elif event.direction == "right":
            x = math.sqrt(x)
            pass

        elif event.direction == "middle":
            x = 16
            pass

    sense.show_message(str(x))