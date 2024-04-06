BOUND = 15
A = 25  # edge length of node
A1 = 1  # the space between 2 bricks (don't mind it)

ROWS, COLS = 0, 0
RES = WIDTH, HEIGHT = 0, 0
START = 0
GOAL = 0

# change the FPS here
FPS = 60

# change the speed here
SPEED = 20

# bool mode
ON = True
OFF = False

# change show nodes' cost mode here
MODE = OFF

# default colors
DARK_GREY = (70, 70, 70)
DIM_GREY = (110, 110, 110)
WHITE = (255, 255, 255)  # path
YELLOW = (200, 200, 0)  # current node
RED = (200, 0, 0)  # discovered node
BLUE = (30, 144, 255)  # completed node (item of closed set)
PURPLE = (138, 43, 226)  # goal
ORANGE = (255, 165, 0)  # start
GREEN = (54, 179, 72)
BLACK = (0, 0, 0)  # brick
