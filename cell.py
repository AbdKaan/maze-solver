from graphics import Line, Point

class Cell:
    def __init__(self, window):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = None
        self._x2 = None
        self._y1 = None
        self._y2 = None
        self._win = window

    def draw(self, x1, x2, y1, y2):
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2

        if self.has_bottom_wall:
            self._win.draw_line(Line(Point(self._x1, self._y2), Point(self._x2, self._y2)))

        if self.has_right_wall:
            self._win.draw_line(Line(Point(self._x2, self._y1), Point(self._x2, self._y2)))

        if self.has_top_wall:
            self._win.draw_line(Line(Point(self._x1, self._y1), Point(self._x2, self._y1)))

        if self.has_left_wall:
            self._win.draw_line(Line(Point(self._x1, self._y1), Point(self._x1, self._y2)))

    def draw_move(self, to_cell, undo=False):
        color = "red" if not undo else "gray"

        cell_center_x = (self._x1 + self._x2) // 2
        cell_center_y = (self._y1 + self._y2) // 2
        to_cell_center_x = (to_cell._x1 + to_cell._x2) // 2
        to_cell_center_y = (to_cell._y1 + to_cell._y2) // 2
        line = Line(Point(cell_center_x, cell_center_y), Point(to_cell_center_x, to_cell_center_y))

        self._win.draw_line(line, color)