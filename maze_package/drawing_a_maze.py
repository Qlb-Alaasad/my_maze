from .dict_validate import MazeConfig
from .create_maze import Cell


class Colors:
    purple: str = '\033[45m'
    red: str = '\033[41m'
    cyan: str = '\033[46m'
    green: str = '\033[42m'
    magenta: str = '\033[43m'
    original: str = '\033[0m'


def drawing_a_maze(
    maze: list[list[Cell]],
    maze_config: MazeConfig,
    pattern_42: list[list[bool]],
    color: str = '\033[47m',
    show_path: bool = False,
    solution_path: list[tuple[int, int]] = None
) -> None:
    """
    Function to draw the maze structure with pathfinding visualization.

    Developed by aabtah.
    """
    if solution_path is None:
        solution_path = []

    if '92' in color:
        path_color = Colors.magenta
    else:
        path_color = Colors.green

    path_set = set(solution_path) if show_path else set()
    x = f"{color}██{Colors.original}"

    for _ in range(maze_config.width * 2 + 1):
        print(x, end="")
    print()

    for i in range(maze_config.height):
        print(x, end="")
        for j in range(maze_config.width):
            if (j, i) == maze_config.entry:
                print(f"{Colors.purple}  {Colors.original}", end="")
            elif (j, i) == maze_config.exit:
                print(f"{Colors.red}  {Colors.original}", end="")
            elif (j, i) in path_set:
                print(f"{path_color}  {Colors.original}", end="")
            elif pattern_42[i][j]:
                print(f"{Colors.cyan}  {Colors.original}", end="")
            else:
                print("  ", end="")

            if maze[i][j].east:
                print(x, end="")
            elif show_path and (j, i) in path_set and (j + 1, i) in path_set:
                print(f"{path_color}  {Colors.original}", end="")
            else:
                print("  ", end="")
        print()

        print(x, end="")
        for j in range(maze_config.width):
            if maze[i][j].south:
                print(x, end="")
            elif show_path and (j, i) in path_set and (j, i + 1) in path_set:
                print(f"{path_color}  {Colors.original}", end="")
            else:
                print("  ", end="")
            print(x, end="")
        print()
