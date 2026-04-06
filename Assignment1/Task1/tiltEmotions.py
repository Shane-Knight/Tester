from sense_hat import SenseHat
from PIL import ImageColor
import time

# General colours
R = (255, 0,   0) # red
G = (0,   255, 0) # green
B = (0,   0,   255) # blue
b = (0,   0,   0) # black
Y = (255, 255, 0) # yellow
W = (255, 255, 255) # white

T = ImageColor.getcolor("#F27783", "RGB") # tongue pink

# Pikachu colours
PY = ImageColor.getcolor("#FFEB3C", "RGB")  # yellow
PO = ImageColor.getcolor("#FF9700", "RGB")  # orange
PB = ImageColor.getcolor("#C76D00", "RGB")  # brown
PC = ImageColor.getcolor("#FE2104", "RGB")  # cheeks
PG = ImageColor.getcolor("#424242", "RGB")  # grey
K = (30, 20, 10)   # dark brown for pupil

# Kirby colours
KLB = ImageColor.getcolor("#00BCD4", "RGB")  # light blue
KDB = ImageColor.getcolor("#3F51B5", "RGB")  # dark blue
KLP = ImageColor.getcolor("#F7B7CD", "RGB")  # light pink
KDP = ImageColor.getcolor("#FC7EAC", "RGB")  # dark pink
KLR = ImageColor.getcolor("#F54F89", "RGB")  # light red
KM = ImageColor.getcolor("#C51162", "RGB")  # maroon
KLM = ImageColor.getcolor("#D81B60", "RGB")  # light maroon
KG = ImageColor.getcolor("#4CAF50", "RGB")  # grass


# sleepy colours
DIM_Y = (60, 55, 0) # dimmed yellow
DIM_W = (50, 50, 50) # dimmed white
DIM_B = (0, 0, 50) # dimmed blue

#sick face colours
DIM_G = (0, 50, 0) # dimmed green
DG = (0, 100, 0) # dark green

#animation frames
scared_frames = [
    [
        b, b, PB, PB, PB, PB, b, b,
        b, PB, Y, Y, Y, Y, PB, b,
        PB, Y, W, Y, Y, W, Y, PB,
        PB, B, Y, Y, Y, Y, B, PB,
        B, Y, T, T, T, T, Y, B,
        PB, Y, T, T, T, T, Y, PB,
        b, PB, T, T, T, T, PB, b,
        b, b, PB, PB, PB, PB, b, b,
    ],
    [
        b, b, PB, PB, PB, PB, b, b,
        b, PB, Y, Y, Y, Y, PB, b,
        PB, W, Y, Y, W, Y, Y, PB,
        B, Y, Y, Y, Y, B, Y, PB,
        PB, T, T, T, T, Y, B, PB,
        PB, T, T, T, T, Y, Y, B,
        b, T, T, T, T, Y, PB, b,
        b, b, PB, PB, PB, PB, b, b,
    ],
    [
        b, b, PB, PB, PB, PB, b, b,
        b, PB, Y, Y, Y, Y, PB, b,
        PB, Y, W, Y, Y, W, Y, PB,
        PB, B, Y, Y, Y, Y, B, PB,
        B, Y, T, T, T, T, Y, B,
        PB, Y, T, T, T, T, Y, PB,
        b, PB, T, T, T, T, PB, b,
        b, b, PB, PB, PB, PB, b, b,
    ],
    [
        b, b, PB, PB, PB, PB, b, b,
        b, PB, Y, Y, Y, Y, PB, b,
        PB, Y, Y, W, Y, Y, W, PB,
        PB, Y, B, Y, Y, Y, Y, B,
        PB, B, Y, T, T, T, T, PB,
        B, Y, Y, T, T, T, T, PB,
        b, PB, Y, T, T, T, T, b,
        b, b, PB, PB, PB, PB, b, b,
    ],
]

sad_frames = [
    [
        b, b, PB, PB, PB, PB, b, b,
        b, PB, Y, Y, Y, Y, PB, b,
        PB, Y, Y, Y, Y, Y, Y, PB,
        PB, Y, W, Y, Y, W, Y, PB,
        PB, Y, B, Y, Y, B, Y, PB,
        PB, Y, B, T, T, B, Y, PB,
        b, PB, Y, Y, Y, Y, PB, b,
        b, b, PB, PB, PB, PB, b, b,
    ],
    [
        b, b, PB, PB, PB, PB, b, b,
        b, PB, Y, Y, Y, Y, PB, b,
        PB, Y, Y, Y, Y, Y, Y, PB,
        PB, Y, W, Y, Y, W, Y, PB,
        PB, Y, Y, Y, Y, Y, Y, PB,
        PB, Y, B, T, T, B, Y, PB,
        b, PB, B, Y, Y, B, PB, b,
        b, b, PB, PB, PB, PB, b, b,
    ],
    [
        b, b, PB, PB, PB, PB, b, b,
        b, PB, Y, Y, Y, Y, PB, b,
        PB, Y, Y, Y, Y, Y, Y, PB,
        PB, Y, W, Y, Y, W, Y, PB,
        PB, Y, B, Y, Y, B, Y, PB,
        PB, Y, Y, T, T, Y, Y, PB,
        b, PB, B, Y, Y, B, PB, b,
        b, b, B, PB, PB, B, b, b,
    ],
    [
        b, b, PB, PB, PB, PB, b, b,
        b, PB, Y, Y, Y, Y, PB, b,
        PB, Y, Y, Y, Y, Y, Y, PB,
        PB, Y, W, Y, Y, W, Y, PB,
        PB, Y, B, Y, Y, B, Y, PB,
        PB, Y, B, T, T, B, Y, PB,
        b, PB, Y, Y, Y, Y, PB, b,
        b, b, B, PB, PB, B, b, b,
    ],
]

hungry_frames = [
    [
        G, G, G, G, G, b, b, b,
        G, R, G, R, G, G, G, G,
        G, G, G, G, G, G, G, G,
        G, G, b, W, b, b, b, W,
        G, G, b, b, b, b, b, b,
        G, G, b, b, b, W, b, b,
        G, G, G, G, G, G, G, G,
        G, G, G, G, G, G, G, G,
    ],
    [
        b, b, b, b, b, b, b, b,
        G, G, G, G, G, b, b, b,
        G, R, G, R, G, G, G, G,
        G, G, G, G, G, G, G, G,
        G, G, b, W, b, W, b, W,
        G, G, G, G, G, G, G, G,
        G, G, G, G, G, G, G, G,
        G, G, G, b, b, b, b, b,
    ],
    [
        b, b, b, b, b, b, b, b,
        G, G, G, G, G, b, b, b,
        G, R, G, R, G, G, G, G,
        G, G, G, G, G, G, G, G,
        G, G, G, G, G, G, G, G,
        G, G, G, G, G, G, G, G,
        G, G, G, b, b, b, b, b,
        G, G, b, b, b, b, b, b,
    ],
]

jumpy_frames = [
    [
        b, b, b, b, b, b, b, b,
        b, b, KLP, KLP, KLP, KLP, b, b,
        b, KLP, KLP, KLP, KLP, KLP, KLP, b,
        b, KDP, KLP, b, KLP, b, KLP, KDP,
        KDP, KLP, KLP, KDB, KLP, KDB, KLP, KDP,
        KDP, KDP, KLR, KLP, KLP, KLP, KLR, b,
        b, KM, KDP, KDP, KLP, KLP, KM, b,
        KG, KM, KLM, KLM, KG, KM, KLM, KG,
    ],
    #squat
    [
        b, b, b, b, b, b, b, b,
        b, b, b, b, b, b, b, b,
        b, b, KLP, KLP, KLP, KLP, b, b,
        b, KLP, KLP, KLP, KLP, KLP, KLP, b,
        KDP, KLP, KLP, b, KLP, b, KLP, KDP,
        KDP, KDP, KLP, KLB, KLP, KLB, KLP, KDP,
        KDP, KM, KLR, KDP, KLP, KLP, KLR, KDP,
        KG, KM, KLM, KLM, KG, KM, KLM, KG,
    ],
    #jump
    [
        b, b, KLP, KLP, KLP, KLP, b, b,
        b, KLP, KLP, KLP, KLP, KLP, KLP, b,
        b, KDP, KLP, b, KLP, b, KLP, KDP,
        KDP, KLP, KLP, KDB, KLP, KDB, KLP, KDP,
        KDP, KDP, KLR, KLP, KLP, KLP, KLR, b,
        b, KM, KDP, KDP, KLP, KLP, KM, b,
        b, KM, KLM, KLM, b, KM, KLM, b,
        KG, KG, KG, KG, KG, KG, KG, KG,
    ],
    #height
    [
        b, KDP, KLP, b, KLP, b, KLP, KDP,
        KDP, KLP, KLP, KDB, KLP, KDB, KLP, KDP,
        KDP, KDP, KLR, KLP, KLP, KLP, KLR, b,
        b, KM, KDP, KDP, KLP, KLP, KM, b,
        b, KM, KLM, KLM, b, KM, KLM, b,
        b, b, KLM, b, b, b, KLM, b,
        b, b, b, b, b, b, b, b,
        KG, KG, KG, KG, KG, KG, KG, KG,
    ],
    #fall
    [
        b, b, KLP, KLP, KLP, KLP, b, b,
        b, KLP, KLP, KLP, KLP, KLP, KLP, b,
        b, KDP, KLP, b, KLP, b, KLP, KDP,
        KDP, KLP, KLP, KDB, KLP, KDB, KLP, KDP,
        KDP, KDP, KLR, KLP, KLP, KLP, KLR, b,
        b, KM, KDP, KDP, KLP, KLP, KM, b,
        b, KM, KLM, KLM, b, KM, KLM, b,
        KG, KG, KG, KG, KG, KG, KG, KG,
    ],
    #squat
    [
        b, b, b, b, b, b, b, b,
        b, b, b, b, b, b, b, b,
        b, b, KLP, KLP, KLP, KLP, b, b,
        b, KLP, KLP, KLP, KLP, KLP, KLP, b,
        KDP, KLP, KLP, b, KLP, b, KLP, KDP,
        KDP, KDP, KLP, KLB, KLP, KLB, KLP, KDP,
        KDP, KM, KLR, KDP, KLP, KLP, KLR, KDP,
        KG, KM, KLM, KLM, KG, KM, KLM, KG,
    ],   
]

funny_frames = [
    # 0 degrees
    [
        b, G, G, DIM_W, DIM_W, R, R, b,
        G, G, W, W, W, W, R, R,
        G, W, W, W, W, W, W, R,
        DIM_W, W, B, R, R, B, W, DIM_W,
        DIM_W, W, W, R, R, W, W, DIM_W,
        DIM_W, W, T, T, T, T, W, DIM_W,
        b, DIM_W, W, T, T, W, DIM_W, b,
        b, b, DIM_W, DIM_W, DIM_W, DIM_W, b, b,
    ],
    # 90 degrees
    [
        b, b, DIM_W, DIM_W, DIM_W, G, G, b,
        b, DIM_W, W, W, W, W, G, G,
        DIM_W, W, T, W, B, W, W, G,
        DIM_W, T, T, R, R, W, W, DIM_W,
        DIM_W, T, T, R, R, W, W, DIM_W,
        DIM_W, W, T, W, B, W, W, R,
        b, DIM_W, W, W, W, W, R, R,
        b, b, DIM_W, DIM_W, DIM_W, R, R, b,
    ],
    # 180 degrees
    [
        b, b, DIM_W, DIM_W, DIM_W, DIM_W, b, b,
        b, DIM_W, W, T, T, W, DIM_W, b,
        DIM_W, W, T, T, T, T, W, DIM_W,
        DIM_W, W, W, R, R, W, W, DIM_W,
        DIM_W, W, B, R, R, B, W, DIM_W,
        R, W, W, W, W, W, W, G,
        R, R, W, W, W, W, G, G,
        b, R, R, DIM_W, DIM_W, G, G, b,
    ],
    # 270 degrees
    [
        b, R, R, DIM_W, DIM_W, DIM_W, b, b,
        R, R, W, W, W, W, DIM_W, b,
        R, W, W, B, W, T, W, DIM_W,
        DIM_W, W, W, R, R, T, T, DIM_W,
        DIM_W, W, W, R, R, T, T, DIM_W,
        G, W, W, B, W, T, W, DIM_W,
        G, G, W, W, W, W, DIM_W, b,
        b, G, G, DIM_W, DIM_W, DIM_W, b, b,
    ],
]

sick_frames = [
    # middle
    [
        b, b, DIM_G, DIM_G, DIM_G, DIM_G, b, b,
        b, DIM_G, DG, DG, DG, DG, DIM_G, b,
        DIM_G, DG, W, DG, DG, W, DG, DIM_G,
        DIM_G, DG, DG, DG, DG, DG, DG, DIM_G,
        DIM_G, DG, DG, T, T, DG, DG, DIM_G,
        DIM_G, DG, T, T, T, T, DG, DIM_G,
        b, DIM_G, T, T, T, T, DIM_G, b,
        b, b, DIM_G, DIM_G, DIM_G, DIM_G, b, b,
    ],
    #shift left
    [
        b, DIM_G, DIM_G, DIM_G, DIM_G, b, b, b,
        DIM_G, DG, DG, DG, DG, DIM_G, b, b,
        DG, W, DG, DG, W, DG, DIM_G, b, 
        DG, DG, DG, DG, DG, DG, DIM_G, b,
        DG, DG, T, T, DG, DG, DIM_G, b,
        DG, T, T, T, T, DG, DIM_G, b, 
        DIM_G, T, T, T, T, DIM_G, b, b,
        b, DIM_G, DIM_G, DIM_G, DIM_G, b, b, b, 
    ],
    #shift up left
    [
        DIM_G, DG, DG, DG, DG, DIM_G, b, b,
        DG, W, DG, DG, W, DG, DIM_G, b, 
        DG, DG, DG, DG, DG, DG, DIM_G, b,
        DG, DG, T, T, DG, DG, DIM_G, b,
        DG, T, T, T, T, DG, DIM_G, b, 
        DIM_G, T, T, T, T, DIM_G, b, b,
        b, DIM_G, DIM_G, DIM_G, DIM_G, b, b, b,
        b, b, b, b, b, b, b, b, 
    ],
    # middle
    [
        b, b, DIM_G, DIM_G, DIM_G, DIM_G, b, b,
        b, DIM_G, DG, DG, DG, DG, DIM_G, b,
        DIM_G, DG, W, DG, DG, W, DG, DIM_G,
        DIM_G, DG, DG, DG, DG, DG, DG, DIM_G,
        DIM_G, DG, DG, T, T, DG, DG, DIM_G,
        DIM_G, DG, T, T, T, T, DG, DIM_G,
        b, DIM_G, T, T, T, T, DIM_G, b,
        b, b, DIM_G, DIM_G, DIM_G, DIM_G, b, b,
    ],
    # Shift right
    [
        b, b, b, DIM_G, DIM_G, DIM_G, DIM_G, b, 
        b, b, DIM_G, DG, DG, DG, DG, DIM_G, 
        b, DIM_G, DG, W, DG, DG, W, DG, 
        b, DIM_G, DG, DG, DG, DG, DG, DG, 
        b, DIM_G, DG, DG, T, T, DG, DG, 
        b, DIM_G, DG, T, T, T, T, DG,
        b, b, DIM_G, T, T, T, T, DIM_G,
        b, b, b, DIM_G, DIM_G, DIM_G, DIM_G, b,
    ],
    # Shift down right
    [
        b, b, b, b, b, b, b, b,
        b, b, b, DIM_G, DIM_G, DIM_G, DIM_G, b, 
        b, b, DIM_G, DG, DG, DG, DG, DIM_G, 
        b, DIM_G, DG, W, DG, DG, W, DG, 
        b, DIM_G, DG, DG, DG, DG, DG, DG, 
        b, DIM_G, DG, DG, T, T, DG, DG, 
        b, DIM_G, DG, T, T, T, T, DG,
        b, b, DIM_G, T, T, T, T, DIM_G,
    ],
]


ANIMATIONS = {
    "Scared": scared_frames,
    "Sad":    sad_frames,
    "Hungry": hungry_frames,
    "Jumpy":  jumpy_frames,
    "Funny":  funny_frames,
    "Sick":   sick_frames,
}

TILT_THRESHOLD = 30
FLIP_THRESHOLD = 60
FLIP_TIME = 0.5
SICK_DURATION = 3.0
FRAME_DELAY = 0.4

# update for OOP style code
class TiltEmotions:
    def __init__(self):
        self.sense = SenseHat()
        self.face_names = list(ANIMATIONS.keys())
        self.current_index = 0
        self.current_frame = 0
        self.paused = False
        self.last_roll = 0
        self.last_roll_time = time.time()
        self.sick_until = 0
 
    def run(self):
        self.sense.set_pixels(ANIMATIONS[self.face_names[self.current_index]][0])
        print("Showing: " + self.face_names[self.current_index])
 
        while True:
            # check joystick
            for event in self.sense.stick.get_events():
                if event.action != "pressed":
                    continue
                if event.direction == "middle":
                    self.paused = not self.paused

                elif event.direction == "down":
                    self.sense.clear()
                    print("End")
                    exit()
 
            if self.paused:
                time.sleep(FRAME_DELAY)
                continue
 
            orientation = self.sense.get_orientation()
            pitch = orientation["pitch"]
            roll  = orientation["roll"]
 
            # convert pitch and roll to -180 to 180 before using it
            if roll > 180:
                roll -= 360
 
            if pitch > 180:
                pitch -= 360
 
            now = time.time()
 
            # check if roll changed more than 60 degrees within 0.5 seconds
            roll_change = abs(roll - self.last_roll)
            time_diff   = now - self.last_roll_time
 
            if roll_change > FLIP_THRESHOLD and time_diff < FLIP_TIME:
                self.sick_until = now + SICK_DURATION
                if self.current_index != self.face_names.index("Sick"):
                    self.current_index = self.face_names.index("Sick")
                    self.current_frame = 0
                    print("Showing: Sick")
                    self.sense.set_pixels(ANIMATIONS[self.face_names[self.current_index]][0])
 
            elif now < self.sick_until:
                # still within sick duration, keep animating sick frames
                frames = ANIMATIONS[self.face_names[self.current_index]]
                self.current_frame = (self.current_frame + 1) % len(frames)
                self.sense.set_pixels(frames[self.current_frame])
 
            else:
                # work out mood from orientation
                if roll > TILT_THRESHOLD:
                    new_index = self.face_names.index("Scared")
                elif roll < -TILT_THRESHOLD:
                    new_index = self.face_names.index("Sad")
                elif pitch < -TILT_THRESHOLD:
                    new_index = self.face_names.index("Hungry")
                elif pitch > TILT_THRESHOLD:
                    new_index = self.face_names.index("Jumpy")
                else:
                    new_index = self.face_names.index("Funny")
 
                if new_index != self.current_index:
                    self.current_index = new_index
                    self.current_frame = 0
                    print("Showing: " + self.face_names[self.current_index])
                    self.sense.set_pixels(ANIMATIONS[self.face_names[self.current_index]][0])
                else:
                    frames = ANIMATIONS[self.face_names[self.current_index]]
                    self.current_frame = (self.current_frame + 1) % len(frames)
                    self.sense.set_pixels(frames[self.current_frame])
 
            self.last_roll = roll
            self.last_roll_time = now
 
            time.sleep(FRAME_DELAY)
 
 
tilt = TiltEmotions()
tilt.run()