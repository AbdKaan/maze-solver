from graphics import *
from maze import Maze


def main():
    win = Window(800, 600)

    maze = Maze(
        x1=100,
        y1=100,
        num_rows=10,
        num_cols=10,
        cell_size_x=60,
        cell_size_y=40,
        win=win
    )

    win.wait_for_close()

main()