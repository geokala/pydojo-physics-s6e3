#!python3
import os, sys
import time

import curses

import lookupondarkness

def log(text):
    with open("cursing.log", "a") as f:
        f.write("%s\n" % text)

INTERVAL = 0.1

type_map = {
  "smoke" : ".",
  "fire" : "/",
}

class IgnoreCoordinate(BaseException): pass

def test_frames():
    for i in range(10):
        for j in range(10):
            for type in "fog", "fire", "water":
                yield [((i, j), type), ((i * 2, j * 2), type), ((i * 3, j * 3), type)]

def get_objects(generator, screen):
    maxy, maxx = screen.getmaxyx()
    for frame in generator(maxx, maxy):
        log(frame)
        screen.clear()
        for (x, y), object_type in frame:
            log("x, y, object_type: %s, %s, %s" % (x, y, object_type))
            place_on_screen(screen, x, y, object_type)
        screen.refresh()
        time.sleep(INTERVAL)

def place_on_screen(screen, x, y, object_type):
    try:
        x, y = translate(screen, x, y)
    except IgnoreCoordinate:
        pass
    else:
        log("place_on_screen: %s, %s" % (x, y))
        screen.addch(y, x, type_map[object_type])

def translate(screen, x, y):
    """Translate the coordinate system from the one from the Physics engine

    x - The X Coordinate
    y - The Y Coordinate
    """
    #
    # For now, do nothing
    #
    maxy, maxx = screen.getmaxyx()
    log("maxx, maxy: %s, %s" % (maxx, maxy))
    x, y = int(x), int(maxy - y)
    if 0 <= x <= maxx and 0 <= y <= maxy:
        return x, y
    else:
        raise IgnoreCoordinate

def main(stdscr):
    get_objects(lookupondarkness.run, stdscr)

if __name__ == '__main__':
    curses.wrapper(main)
