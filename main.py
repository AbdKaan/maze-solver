from graphics import *
from cell import Cell


def main():
    win = Window(800, 600)

    cell = Cell(win)
    cell.has_left_wall = False
    cell.draw(100, 200, 100, 200)

    cell_two = Cell(win)
    cell_two.has_top_wall = False
    cell_two.draw(200, 300, 100, 200)

    cell_three = Cell(win)
    cell_three.has_bottom_wall = False
    cell_three.draw(300, 400, 100, 200)

    cell_four = Cell(win)
    cell_four.draw(600, 400, 300, 600)

    cell.draw_move(cell_two)
    cell_three.draw_move(cell_four)

    cell.draw_move(cell_two, undo=True)

    win.wait_for_close()

main()