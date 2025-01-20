import unittest
from maze import Maze


class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        maze = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(maze._cells),
            num_cols,
        )
        self.assertEqual(
            len(maze._cells[0]),
            num_rows,
        )

    def test_maze_create_cells_2(self):
        num_cols = 5
        num_rows = 5
        maze = Maze(100, 0, num_rows, num_cols, 20, 20)
        self.assertEqual(
            len(maze._cells),
            num_cols,
        )
        self.assertEqual(
            len(maze._cells[0]),
            num_rows,
        )

    def test_maze_create_cells_3(self):
        num_cols = 20
        num_rows = 30
        maze = Maze(100, 100, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(maze._cells),
            num_cols,
        )
        self.assertEqual(
            len(maze._cells[0]),
            num_rows,
        )

    def test_enter_and_exit(self):
        num_cols = 5
        num_rows = 5
        maze = Maze(100, 0, num_rows, num_cols, 20, 20)
        maze._break_entrance_and_exit()
        self.assertEqual(
            maze._cells[0][0].has_top_wall,
            False,
        )
        self.assertEqual(
            maze._cells[-1][-1].has_bottom_wall,
            False,
        )

    def test_visited_false(self):
        num_cols = 5
        num_rows = 5
        maze = Maze(100, 0, num_rows, num_cols, 20, 20)
        maze._cells[3][3].visited = True
        maze._cells[4][2].visited = True
        maze._cells[1][4].visited = True
        maze._reset_cells_visited()
        for i in range(num_cols):
            for j in range(num_rows):
                self.assertEqual(
                    maze._cells[i][j].visited,
                    False,
                )

if __name__ == "__main__":
    unittest.main()