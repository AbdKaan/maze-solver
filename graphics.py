from tkinter import Tk, Canvas

class Window:
    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.title("Maze Solver")

        self.canvas = Canvas(self.__root, width=width, height=height)
        self.canvas.pack(fill='both')

        self.running = False

        self.__root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.running = True
        while self.running:
            self.redraw()
        print("Window closed.")

    def close(self):
        self.running = False