from typing import Coroutine
from time import sleep
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
import cv2

ex = [(0, {(10, 10): 'black', (10, 9): 'black', (10, 8): 'black', (9, 10): 'red', (37, 9): 'green', (25, 29): 'green', (10, 27): 'green'}), (0, {(37, 9): 'green', (25, 29): 'green', (10, 27): 'green', (10, 11): 'black', (10, 10): 'black', (10, 9): 'black', (9, 10): 'red'}), (0, {(37, 9): 'green', (25, 29): 'green', (10, 27): 'green', (10, 12): 'black', (10, 11): 'black', (10, 10): 'black', (9, 10): 'red'}), (0, {(37, 9): 'green', (25, 29): 'green', (10, 27): 'green', (10, 13): 'black', (10, 12): 'black', (10, 11): 'black', (9, 10): 'red'}), (0, {(37, 9): 'green', (25, 29): 'green', (10, 27): 'green', (10, 14): 'black', (10, 13): 'black', (10, 12): 'black', (9, 10): 'red'}), (0, {(37, 9): 'green', (25, 29): 'green', (10, 27): 'green', (10, 15): 'black', (10, 14): 'black', (10, 13): 'black', (9, 10): 'red'}), (0, {(37, 9): 'green', (25, 29): 'green', (10, 27): 'green', (10, 16): 'black', (10, 15): 'black', (10, 14): 'black', (9, 10): 'red'}), (0, {(37, 9): 'green', (25, 29): 'green', (10, 27): 'green', (10, 17): 'black', (10, 16): 'black', (10, 15): 'black', (9, 10): 'red'}), (0, {(37, 9): 'green', (25, 29): 'green', (10, 27): 'green', (10, 18): 'black', (10, 17): 'black', (10, 16): 'black', (9, 10): 'red'}), (0, {(37, 9): 'green', (25, 29): 'green', (10, 27): 'green', (10, 19): 'black', (10, 18): 'black', (10, 17): 'black', (9, 10): 'red'}), (0, {(37, 9): 'green', (25, 29): 'green', (10, 27): 'green', (9, 19): 'black', (10, 19): 'black', (10, 18): 'black', (9, 10): 'red'}), (0, {(37, 9): 'green', (25, 29): 'green', (10, 27): 'green', (8, 19): 'black', (9, 19): 'black', (10, 19): 'black', (9, 10): 'red'}), (0, {(37, 9): 'green', (25, 29): 'green', (10, 27): 'green', (7, 19): 'black', (8, 19): 'black', (9, 19): 'black', (9, 10): 'red'}), (0, {(37, 9): 'green', (25, 29): 'green', (10, 27): 'green', (7, 18): 'black', (7, 19): 'black', (8, 19): 'black', (9, 10): 'red'}), (0, {(37, 9): 'green', (25, 29): 'green', (10, 27): 'green', (7, 17): 'black', (7, 18): 'black', (7, 19): 'black', (9, 10): 'red'}), (0, {(37, 9): 'green', (25, 29): 'green', (10, 27): 'green', (7, 16): 'black', (7, 17): 'black', (7, 18): 'black', (9, 10): 'red'}), (0, {(37, 9): 'green', (25, 29): 'green', (10, 27): 'green', (7, 15): 'black', (7, 16): 'black', (7, 17): 'black', (9, 10): 'red'}), (0, {(37, 9): 'green', (25, 29): 'green', (10, 27): 'green', (7, 14): 'black', (7, 15): 'black', (7, 16): 'black', (9, 10): 'red'}), (0, {(37, 9): 'green', (25, 29): 'green', (10, 27): 'green', (7, 13): 'black', (7, 14): 'black', (7, 15): 'black', (9, 10): 'red'}), (0, {(37, 9): 'green', (25, 29): 'green', (10, 27): 'green', (7, 12): 'black', (7, 13): 'black', (7, 14): 'black', (9, 10): 'red'}), (0, {(37, 9): 'green', (25, 29): 'green', (10, 27): 'green', (7, 11): 'black', (7, 12): 'black', (7, 13): 'black', (9, 10): 'red'}), (0, {(37, 9): 'green', (25, 29): 'green', (10, 27): 'green', (7, 10): 'black', (7, 11): 'black', (7, 12): 'black', (9, 10): 'orange'}), (0, {(37, 9): 'green', (25, 29): 'green', (10, 27): 'green', (7, 9): 'black', (7, 10): 'black', (7, 11): 'black', (9, 11): 'orange', (8, 10): 'orange', (9, 9): 'orange', (10, 10): 'orange'}), (0, {(37, 9): 'green', (25, 29): 'green', (10, 27): 'green', (7, 8): 'black', (7, 9): 'black', (7, 10): 'orange', (9, 12): 'orange', (10, 11): 'orange', (8, 11): 'orange', (9, 8): 'orange', (8, 9): 'orange', (11, 10): 'orange', (10, 9): 'orange'})]
act = [(0, {(10, 10): 'black', (10, 9): 'black', (10, 8): 'black', (9, 10): 'red', (37, 9): 'green', (25, 29): 'green', (10, 27): 'green'}), (0, {(37, 9): 'green', (25, 29): 'green', (10, 27): 'green', (9, 10): 'red', (10, 11): 'black', (10, 10): 'black', (10, 9): 'black'}), (0, {(37, 9): 'green', (25, 29): 'green', (10, 27): 'green', (9, 10): 'red', (10, 12): 'black', (10, 11): 'black', (10, 10): 'black'}), (0, {(37, 9): 'green', (25, 29): 'green', (10, 27): 'green', (9, 10): 'red', (10, 13): 'black', (10, 12): 'black', (10, 11): 'black'}), (0, {(37, 9): 'green', (25, 29): 'green', (10, 27): 'green', (9, 10): 'red', (10, 14): 'black', (10, 13): 'black', (10, 12): 'black'}), (0, {(37, 9): 'green', (25, 29): 'green', (10, 27): 'green', (9, 10): 'red', (10, 15): 'black', (10, 14): 'black', (10, 13): 'black'}), (0, {(37, 9): 'green', (25, 29): 'green', (10, 27): 'green', (9, 10): 'red', (10, 16): 'black', (10, 15): 'black', (10, 14): 'black'}), (0, {(37, 9): 'green', (25, 29): 'green', (10, 27): 'green', (9, 10): 'red', (10, 17): 'black', (10, 16): 'black', (10, 15): 'black'}), (0, {(37, 9): 'green', (25, 29): 'green', (10, 27): 'green', (9, 10): 'red', (10, 18): 'black', (10, 17): 'black', (10, 16): 'black'}), (0, {(37, 9): 'green', (25, 29): 'green', (10, 27): 'green', (9, 10): 'red', (10, 19): 'black', (10, 18): 'black', (10, 17): 'black'}), (0, {(37, 9): 'green', (25, 29): 'green', (10, 27): 'green', (9, 10): 'red', (9, 19): 'black', (10, 19): 'black', (10, 18): 'black'}), (0, {(37, 9): 'green', (25, 29): 'green', (10, 27): 'green', (9, 10): 'red', (8, 19): 'black', (9, 19): 'black', (10, 19): 'black'}), (0, {(37, 9): 'green', (25, 29): 'green', (10, 27): 'green', (9, 10): 'red', (7, 19): 'black', (8, 19): 'black', (9, 19): 'black'}), (0, {(37, 9): 'green', (25, 29): 'green', (10, 27): 'green', (9, 10): 'red', (7, 18): 'black', (7, 19): 'black', (8, 19): 'black'}), (0, {(37, 9): 'green', (25, 29): 'green', (10, 27): 'green', (9, 10): 'red', (7, 17): 'black', (7, 18): 'black', (7, 19): 'black'}), (0, {(37, 9): 'green', (25, 29): 'green', (10, 27): 'green', (9, 10): 'red', (7, 16): 'black', (7, 17): 'black', (7, 18): 'black'}), (0, {(37, 9): 'green', (25, 29): 'green', (10, 27): 'green', (9, 10): 'red', (7, 15): 'black', (7, 16): 'black', (7, 17): 'black'}), (0, {(37, 9): 'green', (25, 29): 'green', (10, 27): 'green', (9, 10): 'red', (7, 14): 'black', (7, 15): 'black', (7, 16): 'black'}), (0, {(37, 9): 'green', (25, 29): 'green', (10, 27): 'green', (9, 10): 'red', (7, 13): 'black', (7, 14): 'black', (7, 15): 'black'}), (0, {(37, 9): 'green', (25, 29): 'green', (10, 27): 'green', (9, 10): 'red', (7, 12): 'black', (7, 13): 'black', (7, 14): 'black'}), (0, {(37, 9): 'green', (25, 29): 'green', (10, 27): 'green', (9, 10): 'red', (7, 11): 'black', (7, 12): 'black', (7, 13): 'black'}), (0, {(37, 9): 'green', (25, 29): 'green', (10, 27): 'green', (9, 10): 'orange', (7, 10): 'black', (7, 11): 'black', (7, 12): 'black'}), (0, {(37, 9): 'green', (25, 29): 'green', (10, 27): 'green', (8, 10): 'orange', (9, 9): 'orange', (9, 11): 'orange', (10, 10): 'orange', (7, 9): 'black', (7, 10): 'black', (7, 11): 'black'}), (0, {(37, 9): 'green', (25, 29): 'green', (10, 27): 'green', (7, 10): 'black', (8, 9): 'orange', (8, 11): 'orange', (9, 8): 'orange', (9, 12): 'orange', (10, 9): 'orange', (10, 11): 'orange', (11, 10): 'orange', (7, 9): 'black'})]
COLORS = {
    'red': [255, 0, 0],
    'black': [0, 0, 0],
    "green": [0, 255, 0],
    "orange": [255, 255, 0],
    "white": [255, 255, 255]}


size = 15
w, h = 40*size, 30*size
out = cv2.VideoWriter(
    'project.mp4', cv2.VideoWriter_fourcc(*'mp4v'),
    15, (w * 2, h), True)

for i in range(max(len(act), len(ex))):
    data = np.zeros((h, w*2, 3), dtype=np.uint8)
    data[:, :w] = [255, 255, 255]

    try:
        for coord, color in ex[i][1].items():
            x, y = coord[0] * size, coord[1] * size
            c = COLORS[color]
            data[y:(y+size), x:x+size] = c
    except:
        pass
    try:
        for coord, color in act[i][1].items():
            x, y = coord[0] * size, coord[1] * size
            c = COLORS["white" if color == "black" else color]
            x += w
            data[y:(y+size), x:x+size] = c
    except:
        pass
    data = np.flipud(data)
    img = Image.fromarray(data, 'RGB')
    for i in range(15):
        out.write(data)

out.release()
