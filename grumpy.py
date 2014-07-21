# -*- coding: utf-8 -*-
from itertools import cycle
from textwrap import wrap

MAX_WIDTH = 80
HORIZONTAL_BAR = "█" * MAX_WIDTH
LEFT_CAT = """▌                         ▐█     ▐ %s █
▌    ▄                  ▄█▓█▌    ▐ %s █
▌   ▐██▄               ▄▓░░▓▓    ▐ %s █
▌   ▐█░██▓            ▓▓░░░▓▌    ▐ %s █
▌   ▐█▌░▓██          █▓░░░░▓     ▐ %s █
▌    ▓█▌░░▓█▄███████▄███▓░▓█     ▐ %s █
▌    ▓██▌░▓██░░░░░░░░░░▓█░▓▌     ▐ %s █
▌     ▓█████░░░░░░░░░░░░▓██      ▐ %s █
▌     ▓██▓░░░░░░░░░░░░░░░▓█      ▐ %s █
▌     ▐█▓░░░░░░█▓░░▓█░░░░▓█▌     ▐ %s █
▌     ▓█▌░▓█▓▓██▓░█▓▓▓▓▓░▓█▌     ▐ %s █
▌     ▓▓░▓██████▓░▓███▓▓▌░█▓     ▐ %s █
▌    ▐▓▓░█▄▐▓▌█▓░░▓█▐▓▌▄▓░██     ▐ %s █
▌    ▓█▓░▓█▄▄▄█▓░░▓█▄▄▄█▓░██▌    ▐ %s █
▌    ▓█▌░▓█████▓░░░▓███▓▀░▓█▓    ▐ %s █
▌   ▐▓█░░░▀▓██▀░░░░░ ▀▓▀░░▓█▓    ▐ %s █
▌   ▓██░░░░░░░░▀▄▄▄▄▀░░░░░░▓▓    ▐ %s █
▌   ▓█▌░░░░░░░░░░▐▌░░░░░░░░▓▓▌   ▐ %s █
▌   ▓█░░░░░░░░░▄▀▀▀▀▄░░░░░░░█▓   ▐ %s █
▌  ▐█▌░░░░░░░░▀░░░░░░▀░░░░░░█▓▌  ▐ %s █
▌  ▓█░░░░░░░░░░░░░░░░░░░░░░░██▓  ▐ %s █
▌  ▓█░░░░░░░░░░░░░░░░░░░░░░░▓█▓  ▐ %s █"""
LEFT_BAR = "██████████████████████████████████ %s █"
LEFT_NOPE = """█░▀░░░░▀█▀░░░░░░▀█░░░░░░▀█▀░░░░░▀█ %s █
█░░▐█▌░░█░░░██░░░█░░██░░░█░░░██░░█ %s █
█░░▐█▌░░█░░░██░░░█░░██░░░█░░░██░░█ %s █
█░░▐█▌░░█░░░██░░░█░░░░░░▄█░░▄▄▄▄▄█ %s █
█░░▐█▌░░█░░░██░░░█░░░░████░░░░░░░█ %s █
█░░░█░░░█▄░░░░░░▄█░░░░████▄░░░░░▄█ %s █"""
MSG_WIDTH = MAX_WIDTH - 35 - 2

def grumpy_print(msg):
    """
    Print something with a scrolling grumpy-cat follwoed by "NOPE" message on
    the left side.
    """
    lines = wrap(msg, MSG_WIDTH)
    lines = [(line + ' ' * MSG_WIDTH)[:MSG_WIDTH] for line in lines]

    chunks = [HORIZONTAL_BAR]

    for left in cycle([LEFT_CAT, LEFT_BAR, LEFT_NOPE, LEFT_BAR]):
        if not lines:
            break
        slots = left.count("%s")
        chunk_lines = (lines[:slots] + [' ' * MSG_WIDTH] * slots)[:slots]
        chunks.append(left % tuple(chunk_lines))
        lines = lines[slots:]

    chunks.append(HORIZONTAL_BAR)

    for chunk in chunks:
        print chunk
