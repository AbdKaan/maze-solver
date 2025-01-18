from graphics import *


def main():
    win = Window(800, 600)
    win.draw_line(Line(Point(0, 0), Point(800, 600)), "black")
    win.draw_line(Line(Point(50, 500), Point(400, 600)), "red")
    win.draw_line(Line(Point(100, 690), Point(500, 500)), "blue")
    win.draw_line(Line(Point(800, 0), Point(0, 600)), "purple")
    win.wait_for_close()

main()