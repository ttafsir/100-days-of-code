import itertools
import sys
import time

# symbols = itertools.cycle('-\|/')
frames = iter((
    "⠋",
    "⠙",
    "⠹",
    "⠸",
    "⠼",
    "⠴",
    "⠦",
    "⠧",
    "⠇",
    "⠏"
))



symbols = itertools.cycle(':\|/')
frame_cycle = itertools.cycle(frames)
while True:
    sys.stdout.write('\r' + next(frame_cycle))
    # sys.stdout.write('\r' + next(symbols))  # \r to keep on new line
    sys.stdout.flush()
    time.sleep(0.2)
