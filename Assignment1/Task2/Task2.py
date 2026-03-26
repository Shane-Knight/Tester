try:
    from sense_hat import SenseHat
except ImportError:
    from sense_emu import SenseHat

import math

class SimpleCalc:
    def __init__(self, sense):
        self.sense = sense
        # default value
        self.x = 16

    def run(self):
        self.sense.show_message(str(self.x))

        while True:
            for event in self.sense.stick.get_events():
                if event.action != "pressed":
                    continue

                # x+ 1
                if event.direction == "up":
                    self.x += 1
                    pass

                # x - 1
                elif event.direction == "down":
                    self.x -= 1
                    pass

                # x squared
                elif event.direction == "left":
                    self.x = self.x ** 2
                    pass

                # x square root
                elif event.direction == "right":
                    self.x = math.sqrt(self.x)
                    pass

                elif event.direction == "middle":
                    self.x = 16
                    pass

            self.sense.show_message(str(self.x))

calc = SimpleCalc(SenseHat())
calc.run()