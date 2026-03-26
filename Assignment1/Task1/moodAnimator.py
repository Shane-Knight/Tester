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

#artifact but want to keep 
FRAMES = {
    # "Pikachu": [
    #     W,  PG, PG, W,  W,  W,  W,  PG,
    #     W,  W,  PY, PO, W,  W,  W,  PO,
    #     W,  W,  W,  PY, PY, PY, PY, PO,
    #     PO, PO, W,  PY, K, PY, PY, K,
    #     PO, PO, W,  PC, PY, PY, PY, PO,
    #     W,  PB, W,  PY, PO, PO, PO, W,
    #     W,  PB, PY, PO, PY, PO, PY, W,
    #     W,  W,  PY, PO, PB, PB, PO, W,
    # ],
    # "Red Ghost": [
    #     b,   b,   RGC, RGC, RGC, RGC, b,   b,
    #     b,   RGC, RGC, RGC, RGC, RGC, RGC, b,
    #     RGC, RGW, RGW, RGC, RGC, RGW, RGW, RGC,
    #     RGC, RGW, RGB, RGC, RGC, RGW, RGB, RGC,
    #     RGC, RGC, RGC, RGC, RGC, RGC, RGC, RGC,
    #     RGC, RGC, RGC, RGC, RGC, RGC, RGC, RGC,
    #     RGC, RGD, RGC, RGD, RGC, RGD, RGC, RGD,
    #     b,   RGD, b,   RGD, b,   RGD, b,   RGD,
    # ],

    # "Blue Ghost": [
    #     b,   b,   BGC, BGC, BGC, BGC, b,   b,
    #     b,   BGC, BGC, BGC, BGC, BGC, BGC, b,
    #     BGC, BGW, BGW, BGC, BGC, BGW, BGW, BGC,
    #     BGC, BGW, BGB, BGC, BGC, BGW, BGB, BGC,
    #     BGC, BGC, BGC, BGC, BGC, BGC, BGC, BGC,
    #     BGC, BGC, BGC, BGC, BGC, BGC, BGC, BGC,
    #     BGC, BGD, BGC, BGD, BGC, BGD, BGC, BGD,
    #     b,   BGD, b,   BGD, b,   BGD, b,   BGD,
    # ],
}


ANIMATIONS = {
    "Scared": scared_frames,
    "Sad": sad_frames,
    "Hungry": hungry_frames,
    "Jumpy": jumpy_frames,
    "Funny": funny_frames,
}

#face names as a list to cycle through them
face_names = list(ANIMATIONS.keys())


FRAME_DELAY  = 0.4   # per frame
RATE_LIMIT   = 3.0   # between accepted presses
IDLE_TIMEOUT = 15.0  # before sleep mode kicks in

# initial state
current_index = 0
current_frame = 0
paused = False
sleeping = False
last_press_time = 0
last_event_time = time.time()

 

# display first emoji
sense.set_pixels(ANIMATIONS[face_names[current_index]][0])
print("Showing: " + face_names[current_index])

while True:
    # if not asleep or paused go through animation frames
    if not paused and not sleeping:
        frames = ANIMATIONS[face_names[current_index]]
        current_frame = (current_frame + 1) % len(frames) # mod for looping
        sense.set_pixels(frames[current_frame])
 
    # check if idle for 15 seconds
    if not sleeping and time.time() - last_event_time >= IDLE_TIMEOUT:
        print("im getting tired... zzz")
        sleeping = True
        sleep_frame = 0 
        sense.set_pixels(sleepy_frames[0])
 
    # animate the sleep face while sleeping
    elif sleeping:
        sleep_frame = (sleep_frame + 1) % len(sleepy_frames)
        sense.set_pixels(sleepy_frames[sleep_frame])
 
    # check for joystick input
    for event in sense.stick.get_events():
 
        if event.action != "pressed":
            continue
 
        now = time.time()
        last_event_time = now
 
        # wake from sleep on any press
        if sleeping:
            print("waking up")
            sleeping = False
            sense.set_pixels(ANIMATIONS[face_names[current_index]][current_frame])
            last_press_time = now
            continue
 
        # ignore if within rate limit window
        if now - last_press_time < RATE_LIMIT:
            print("too fast between inputs")
            continue
 
        last_press_time = now
 
        if event.direction == "right":
            current_index = (current_index + 1) % len(face_names)
            current_frame = 0
            print("Showing: " + face_names[current_index])
            sense.set_pixels(ANIMATIONS[face_names[current_index]][0])
 
        elif event.direction == "left":
            current_index = (current_index - 1) % len(face_names)
            current_frame = 0
            print("Showing: " + face_names[current_index])
            sense.set_pixels(ANIMATIONS[face_names[current_index]][0])
 
        elif event.direction == "middle":
            paused = not paused
            print("paused" if paused else "resumed")
 
        elif event.direction == "down":
            print("End")
            sense.clear()
            exit()
 
    time.sleep(FRAME_DELAY)