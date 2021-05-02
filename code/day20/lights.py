import sys
import time
from collections import namedtuple
from itertools import cycle

COLORS = {
    'green': "\033[1;32;40m",
    'yellow': "\033[1;33;40m",
    'red': "\033[1;31;40m",
    'white': "\033[1;37;40m"
}

Light = namedtuple('Light', 'color chars')

green_light = Light(color=COLORS["green"], chars=" ●    ")
yellow_light = Light(color=COLORS["yellow"], chars="   ●  ")
red_light = Light(color=COLORS["red"], chars="     ●")

light_frames = (
    "(" + f"{green_light.color} {green_light.chars} {COLORS['white']} )",
    "(" + f"{yellow_light.color} {yellow_light.chars} {COLORS['white']} )",
    "(" + f"{red_light.color} {red_light.chars} {COLORS['white']} )",
)
colored_lights_cycle = cycle(light_frames)


while True:
    sys.stdout.write("\r" + next(colored_lights_cycle).ljust(7))
    time.sleep(2)
    sys.stdout.flush()
