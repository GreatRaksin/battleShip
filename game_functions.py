import sys
from pygame import *


def check_events():
    for i in event.get():
        if i.type == QUIT:
            sys.exit()