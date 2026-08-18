import random
from typing import Any
from .make42_pattern import make_42_pattern


class Cell:
    def __init__(
        self,
        north: bool = True,
        south: bool = True,
        east: bool = True,
        west: bool = True
    ) -> None:
        """
        This init function for Cell that will use
        to make our maze

        made by aabtah
        """
        self.north = north  # up with value 1
        self.south = south  # done with value 2
        self.east = east    # rite
        self.west = west    # left


def create_maze(maze_config: Any) -> tuple[
    list[list[Cell]],
    list[list[bool]]
]:
    """
    A function to build a maze in the form of a list inside
    a 2D list inside an object in four directions,
    and see which direction is open.
    Supports both PERFECT=True and PERFECT=False (Pac-Man board).

    made by aabtah
    """
    # This is regarding the seed and if it included, will build with seed
    if maze_config.seed is not None:
        random.seed(maze_config.seed)

    # start hear
    maze: list[list[Cell]] = []

    # This is to ensure all elements are in order to clear the path later.
    for i in range(maze_config.height):
        row: list[Cell] = []
        for _ in range(maze_config.width):
            row.append(Cell())
        maze.append(row)

    entry_x, entry_y = maze_config.entry
    pattern_42 = make_42_pattern(maze_config)
    need_open = []
    for reserved in pattern_42:
        row_list = []
        for element in reserved:
            row_list.append(element)
        need_open.append(row_list)

    need_open[entry_y][entry_x] = True

    stack = [(entry_x, entry_y)]

    while stack:
        x, y = stack[-1]
        not_open = []
        new_y = y - 1
        if new_y >= 0 and not need_open[new_y][x]:
            not_open.append((x, new_y, 0))
        new_x = x + 1
        if new_x < maze_config.width and not \
                need_open[y][new_x]:
            not_open.append((new_x, y, 1))
        new_y = y + 1
        if new_y < maze_config.height and not need_open[new_y][x]:
            not_open.append((x, new_y, 2))
        new_x = x - 1
        if new_x >= 0 and not need_open[y][new_x]:
            not_open.append((new_x, y, 3))

        if not_open:
            new_x, new_y, choice = random.choice(not_open)
            if choice == 0:
                maze[y][x].north = False
                maze[new_y][new_x].south = False
            elif choice == 1:
                maze[y][x].east = False
                maze[new_y][new_x].west = False
            elif choice == 2:
                maze[y][x].south = False
                maze[new_y][new_x].north = False
            elif choice == 3:
                maze[y][x].west = False
                maze[new_y][new_x].east = False
            need_open[new_y][new_x] = True
            stack.append((new_x, new_y))
        else:
            stack.pop()
    if not maze_config.perfect:
        for i in range(maze_config.height):
            for j in range(maze_config.width):
                if pattern_42[i][j]:
                    continue
                number_of_open_cells = 0
                if i > 0 and not maze[i][j].north:
                    number_of_open_cells += 1
                if i < maze_config.height - 1 and not maze[i][j].south:
                    number_of_open_cells += 1
                if j > 0 and not maze[i][j].west:
                    number_of_open_cells += 1
                if j < maze_config.width - 1 and not maze[i][j].east:
                    number_of_open_cells += 1
                if number_of_open_cells == 1:
                    Openable = []
                    if (
                        i < maze_config.height - 1
                        and maze[i][j].south
                        and not pattern_42[i + 1][j]
                    ):
                        Openable.append(0)
                    if (
                        j < maze_config.width - 1
                        and maze[i][j].east
                        and not pattern_42[i][j + 1]
                    ):
                        Openable.append(1)
                    if (
                        i > 0
                        and maze[i][j].north
                        and not pattern_42[i - 1][j]
                    ):
                        Openable.append(2)
                    if (
                        j > 0
                        and maze[i][j].west
                        and not pattern_42[i][j - 1]
                    ):
                        Openable.append(3)

                    if Openable:
                        choice = random.choice(Openable)
                        if choice == 0:
                            maze[i][j].south = False
                            maze[i + 1][j].north = False
                        elif choice == 1:
                            maze[i][j].east = False
                            maze[i][j + 1].west = False
                        elif choice == 2:
                            maze[i][j].north = False
                            maze[i - 1][j].south = False
                        elif choice == 3:
                            maze[i][j].west = False
                            maze[i][j - 1].east = False
    return maze, pattern_42
