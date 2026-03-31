from sense_hat import SenseHat
from PIL import ImageColor
import time

sense = SenseHat()

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


#Sleep y colours
DIM_Y = (60,  55,   0)   # dimmed yellow
DIM_W = (50,  50,  50)   # dimmed white
DIM_B = (0,    0,  50)   # dimmed blue

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

sleepy_frames = [
    #right most
    [
        b, b, DIM_Y, DIM_Y, DIM_B, DIM_B, DIM_B, DIM_B,
        b, DIM_Y, DIM_Y, DIM_Y, DIM_Y, DIM_Y, DIM_B, b,
        DIM_Y, DIM_W, DIM_W, DIM_Y, DIM_Y, DIM_B, DIM_W, DIM_Y,
        DIM_Y, DIM_Y, DIM_Y, DIM_Y, DIM_B, DIM_B, DIM_B, DIM_B,
        DIM_Y, DIM_Y, DIM_Y, DIM_Y, DIM_Y, DIM_Y, DIM_Y, DIM_Y,
        DIM_Y, DIM_Y, DIM_W, DIM_W, DIM_W, DIM_W, DIM_Y, DIM_Y,
        b, DIM_Y, DIM_Y, DIM_Y, DIM_Y, DIM_Y, DIM_Y, b,
        b, b, DIM_Y, DIM_Y, DIM_Y, DIM_Y, b, b,
    ],
    [
        b, b, DIM_Y, DIM_B, DIM_B, DIM_B, DIM_B, b,
        b, DIM_Y, DIM_Y, DIM_Y, DIM_Y, DIM_B, DIM_Y, b,
        DIM_Y, DIM_W, DIM_W, DIM_Y, DIM_B, DIM_W, DIM_W, DIM_Y,
        DIM_Y, DIM_Y, DIM_Y, DIM_B, DIM_B, DIM_B, DIM_B, DIM_Y,
        DIM_Y, DIM_Y, DIM_Y, DIM_Y, DIM_Y, DIM_Y, DIM_Y, DIM_Y,
        DIM_Y, DIM_Y, DIM_W, DIM_W, DIM_W, DIM_W, DIM_Y, DIM_Y,
        b, DIM_Y, DIM_Y, DIM_Y, DIM_Y, DIM_Y, DIM_Y, b,
        b, b, DIM_Y, DIM_Y, DIM_Y, DIM_Y, b, b,
    ],
    [
        b, b, DIM_B, DIM_B, DIM_B, DIM_B, b, b,
        b, DIM_Y, DIM_Y, DIM_Y, DIM_B, DIM_Y, DIM_Y, b,
        DIM_Y, DIM_W, DIM_W, DIM_B, DIM_Y, DIM_W, DIM_W, DIM_Y,
        DIM_Y, DIM_Y, DIM_B, DIM_B, DIM_B, DIM_B, DIM_Y, DIM_Y,
        DIM_Y, DIM_Y, DIM_Y, DIM_Y, DIM_Y, DIM_Y, DIM_Y, DIM_Y,
        DIM_Y, DIM_Y, DIM_W, DIM_W, DIM_W, DIM_W, DIM_Y, DIM_Y,
        b, DIM_Y, DIM_Y, DIM_Y, DIM_Y, DIM_Y, DIM_Y, b,
        b, b, DIM_Y, DIM_Y, DIM_Y, DIM_Y, b, b,
    ],
    [
        b, DIM_B, DIM_B, DIM_B, DIM_B, DIM_Y, b, b,
        b, DIM_Y, DIM_Y, DIM_B, DIM_Y, DIM_Y, DIM_Y, b,
        DIM_Y, DIM_W, DIM_B, DIM_Y, DIM_Y, DIM_W, DIM_W, DIM_Y,
        DIM_Y, DIM_B, DIM_B, DIM_B, DIM_B, DIM_Y, DIM_Y, DIM_Y,
        DIM_Y, DIM_Y, DIM_Y, DIM_Y, DIM_Y, DIM_Y, DIM_Y, DIM_Y,
        DIM_Y, DIM_Y, DIM_W, DIM_W, DIM_W, DIM_W, DIM_Y, DIM_Y,
        b, DIM_Y, DIM_Y, DIM_Y, DIM_Y, DIM_Y, DIM_Y, b,
        b, b, DIM_Y, DIM_Y, DIM_Y, DIM_Y, b, b,
    ],
    #left most
    [
        DIM_B, DIM_B, DIM_B, DIM_B, DIM_Y, DIM_Y, b, b,
        b, DIM_Y, DIM_B, DIM_Y, DIM_Y, DIM_Y, DIM_Y, b,
        DIM_Y, DIM_B, DIM_W, DIM_Y, DIM_Y, DIM_W, DIM_W, DIM_Y,
        DIM_B, DIM_B, DIM_B, DIM_B, DIM_Y, DIM_Y, DIM_Y, DIM_Y,
        DIM_Y, DIM_Y, DIM_Y, DIM_Y, DIM_Y, DIM_Y, DIM_Y, DIM_Y,
        DIM_Y, DIM_Y, DIM_W, DIM_W, DIM_W, DIM_W, DIM_Y, DIM_Y,
        b, DIM_Y, DIM_Y, DIM_Y, DIM_Y, DIM_Y, DIM_Y, b,
        b, b, DIM_Y, DIM_Y, DIM_Y, DIM_Y, b, b,
    ],
    [
        b, DIM_B, DIM_B, DIM_B, DIM_B, DIM_Y, b, b,
        b, DIM_Y, DIM_Y, DIM_B, DIM_Y, DIM_Y, DIM_Y, b,
        DIM_Y, DIM_W, DIM_B, DIM_Y, DIM_Y, DIM_W, DIM_W, DIM_Y,
        DIM_Y, DIM_B, DIM_B, DIM_B, DIM_B, DIM_Y, DIM_Y, DIM_Y,
        DIM_Y, DIM_Y, DIM_Y, DIM_Y, DIM_Y, DIM_Y, DIM_Y, DIM_Y,
        DIM_Y, DIM_Y, DIM_W, DIM_W, DIM_W, DIM_W, DIM_Y, DIM_Y,
        b, DIM_Y, DIM_Y, DIM_Y, DIM_Y, DIM_Y, DIM_Y, b,
        b, b, DIM_Y, DIM_Y, DIM_Y, DIM_Y, b, b,
    ],
    [
        b, b, DIM_B, DIM_B, DIM_B, DIM_B, b, b,
        b, DIM_Y, DIM_Y, DIM_Y, DIM_B, DIM_Y, DIM_Y, b,
        DIM_Y, DIM_W, DIM_W, DIM_B, DIM_Y, DIM_W, DIM_W, DIM_Y,
        DIM_Y, DIM_Y, DIM_B, DIM_B, DIM_B, DIM_B, DIM_Y, DIM_Y,
        DIM_Y, DIM_Y, DIM_Y, DIM_Y, DIM_Y, DIM_Y, DIM_Y, DIM_Y,
        DIM_Y, DIM_Y, DIM_W, DIM_W, DIM_W, DIM_W, DIM_Y, DIM_Y,
        b, DIM_Y, DIM_Y, DIM_Y, DIM_Y, DIM_Y, DIM_Y, b,
        b, b, DIM_Y, DIM_Y, DIM_Y, DIM_Y, b, b,
    ],
    [
        b, b, DIM_Y, DIM_B, DIM_B, DIM_B, DIM_B, b,
        b, DIM_Y, DIM_Y, DIM_Y, DIM_Y, DIM_B, DIM_Y, b,
        DIM_Y, DIM_W, DIM_W, DIM_Y, DIM_B, DIM_W, DIM_W, DIM_Y,
        DIM_Y, DIM_Y, DIM_Y, DIM_B, DIM_B, DIM_B, DIM_B, DIM_Y,
        DIM_Y, DIM_Y, DIM_Y, DIM_Y, DIM_Y, DIM_Y, DIM_Y, DIM_Y,
        DIM_Y, DIM_Y, DIM_W, DIM_W, DIM_W, DIM_W, DIM_Y, DIM_Y,
        b, DIM_Y, DIM_Y, DIM_Y, DIM_Y, DIM_Y, DIM_Y, b,
        b, b, DIM_Y, DIM_Y, DIM_Y, DIM_Y, b, b,
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



ANIMATIONS = {
    "Scared": scared_frames,
    "Sad":    sad_frames,
    "Hungry": hungry_frames,
    "Jumpy":  jumpy_frames,
    "Funny":  funny_frames,
}
 
face_names = list(ANIMATIONS.keys())
 
TILT_THRESHOLD = 30
 
def get_mood_index(pitch, roll):
    # roll is already converted to -180 to 180 before calling this
    if pitch > 180:
        pitch -= 360
 
    if roll > TILT_THRESHOLD:
        return face_names.index("Scared")
    elif roll < -TILT_THRESHOLD:
        return face_names.index("Sad")
    elif pitch < -TILT_THRESHOLD:
        return face_names.index("Hungry")
    elif pitch > TILT_THRESHOLD:
        return face_names.index("Jumpy")
    else:
        return face_names.index("Funny")
 
# initial state
current_index = 0
current_frame = 0
paused = False
last_roll = 0
last_roll_time = time.time()
 
FRAME_DELAY = 0.4
 
# show first frame
sense.set_pixels(ANIMATIONS[face_names[current_index]][0])
print("Showing: " + face_names[current_index])
 
while True:
    # check joystick
    for event in sense.stick.get_events():
        if event.action != "pressed":
            continue
        if event.direction == "middle":
            paused = not paused

        elif event.direction == "down":
            sense.clear()
            print("End")
            exit()
 
    if paused:
        time.sleep(FRAME_DELAY)
        continue
 
    orientation = sense.get_orientation()
    pitch = orientation["pitch"]
    roll  = orientation["roll"]
 
    # convert roll to -180 to 180 before using it
    if roll > 180:
        roll -= 360
 
    now = time.time()
 
    # check if roll changed more than 60 degrees within 0.5 seconds
    roll_change = abs(roll - last_roll)
    time_diff   = now - last_roll_time
 
 
 
    else:
        new_index = get_mood_index(pitch, roll)
        if new_index != current_index:
            current_index = new_index
            current_frame = 0
            print("Showing: " + face_names[current_index])
            sense.set_pixels(ANIMATIONS[face_names[current_index]][0])
        else:
            frames = ANIMATIONS[face_names[current_index]]
            current_frame = (current_frame + 1) % len(frames)
            sense.set_pixels(frames[current_frame])
 
    last_roll = roll
    last_roll_time = now
 
    time.sleep(FRAME_DELAY)