from graphics import *


def main():
    win = Window(800, 600)
    cell = Cell(100, 200, 100, 200, win)
    cell.draw()
    cell_two = Cell(200, 300, 100, 200, win)
    cell_two.draw()
    cell_three = Cell(300, 400, 100, 200, win)
    cell_three.draw()
    cell_four = Cell(600, 400, 300, 600, win)
    cell_four.draw()
    win.wait_for_close()

main()