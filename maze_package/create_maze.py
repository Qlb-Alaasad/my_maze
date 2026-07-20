import random
from .make42_pattern import make_42_pattern
from .dict_validate import MazeConfig


class Cell():
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
        self.east = east  # rite
        self.west = west  # left


def Imperfect(
        maze: list[list[Cell]], maze_config: MazeConfig
        ) -> list[list[Cell]]:
    """
    تعديل المتاهة لتصبح غير كاملة (Imperfect) عن طريق إزالة بعض الجدران الداخلية
    مع ضمان عدم المساس بالحدود الخارجية للمتاهة.
    """
    num_removals = (maze_config.width * maze_config.height) // 80

    for _ in range(num_removals):
        removed = False
        attempts = 0
        while not removed and attempts < 100:
            y = random.randint(0, maze_config.height - 1)
            x = random.randint(0, maze_config.width - 1)
            direction = random.randint(0, 3)

            if direction == 0 and y > 0:  # North
                maze[y][x].north = False
                maze[y-1][x].south = False
                removed = True
            elif direction == 1 and x < maze_config.width - 1:  # East
                maze[y][x].east = False
                maze[y][x+1].west = False
                removed = True
            elif direction == 2 and y < maze_config.height - 1:  # South
                maze[y][x].south = False
                maze[y+1][x].north = False
                removed = True
            elif direction == 3 and x > 0:  # West
                maze[y][x].west = False
                maze[y][x-1].east = False
                removed = True

            attempts += 1

    return maze


def create_maze(maze_config: MazeConfig) -> tuple[
        list[list[Cell]],
        list[list[bool]]
        ]:
    """
    A function to build a maze in the form of a list inside
    a 2D list inside an object in four directions,
    and see which direction is open

    made by aabtah
    """

    # This is regarding the seed and if it included, will buld with seed
    if maze_config.seed is not None:
        random.seed(maze_config.seed)

    # start hear
    maze: list[list[Cell]] = []

    # This is to ensure all elements are in order to clear the path later.
    for i in range(maze_config.height):
        row: list[Cell] = []
        for j in range(maze_config.width):
            row.append(Cell())
        maze.append(row)

    entry_x, entry_y = maze_config.entry
    pattern_42 = make_42_pattern(maze_config)
    need_open = pattern_42
    need_open[entry_y][entry_x] = True  # start up

    stack = [(entry_x, entry_y)]

    while stack:
        x, y = stack[-1]
        not_open = []
        new_y = y - 1
        if new_y >= 0 and not need_open[new_y][x]:
            not_open.append((x, new_y, 0))
        new_x = x + 1
        if new_x < maze_config.width and not need_open[y][new_x]:
            not_open.append((new_x, y, 1))
        new_y = y + 1
        if new_y < maze_config.height and not need_open[new_y][x]:
            not_open.append((x, new_y, 2))
        new_x = x - 1
        if new_x >= 0 and not need_open[y][new_x]:
            not_open.append((new_x, y, 3))

        if not_open:
            new_x, new_y, go_site = random.choice(not_open)
            if go_site == 0:
                maze[y][x].north = False
                maze[new_y][new_x].south = False
            elif go_site == 1:
                maze[y][x].east = False
                maze[new_y][new_x].west = False
            elif go_site == 2:
                maze[y][x].south = False
                maze[new_y][new_x].north = False
            elif go_site == 3:
                maze[y][x].west = False
                maze[new_y][new_x].east = False
            need_open[new_y][new_x] = True
            stack.append((new_x, new_y))
        else:
            stack.pop()

    if not maze_config.perfect:
        maze = Imperfect(maze, maze_config)
    return maze, pattern_42
