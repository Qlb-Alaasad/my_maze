from typing import Optional
from .dict_validate import MazeConfig
from .create_maze import Cell


class Colors:
    purple: str = '\033[45m'
    red: str = '\033[41m'
    cyan: str = '\033[46m'
    magenta: str = '\033[43m'
    original: str = '\033[0m'
    colors = [
        '\033[42m',
        '\033[44m',
        '\033[47m',
        '\033[100m',
        ]
    def discoloration(self):
        while True:
            for color in self.colors:
                yield color

def drawing_a_maze(
    maze: list[list[Cell]],
    maze_config: MazeConfig,
    pattern_42: list[list[bool]],
    color: str,
    show_path: bool = False,
    solution_path: Optional[list[tuple[int, int]]] = None
) -> None:
    """
    Function to draw the maze structure with pathfinding visualization.

    Developed by aabtah.
    """
    
    for _ in range(maze_config.width * 2 + 1):
        print(f"{color}  {Colors.original}", end="")
    print()

    for i in range(maze_config.height):
        print(f"{color}  {Colors.original}", end="")
        for j in range(maze_config.width):
            if (j, i) == maze_config.entry:
                print(f"{Colors.cyan}  {Colors.original}", end="")
            elif (j, i) == maze_config.exit:
                print(f"{Colors.red}  {Colors.original}", end="")
            elif show_path == True and solution_path and (j, i) in solution_path:
                print(f"{Colors.magenta}  {Colors.original}", end="")
            elif pattern_42[i][j]:
                print(f"{Colors.purple}  {Colors.original}", end="")

            else:
                print(f"  ", end="")
                
            if maze[i][j].east:
                print(f"{color}  {Colors.original}", end="")
            elif show_path == True and solution_path and (j, i) in solution_path and (j + 1, i) in solution_path:
                print(f"{Colors.magenta}  {Colors.original}", end="")
            else:
                print("  ", end="")
        print()
        print(f"{color}  {Colors.original}", end="")
        for j in range(maze_config.width):
            if maze[i][j].south:
                print(f"{color}  {Colors.original}", end="")
            elif show_path == True and solution_path and (j, i) in solution_path and (j, i + 1) in solution_path:
                print(f"{Colors.magenta}  {Colors.original}", end="")
            else:
                print("  ", end="")
            print(f"{color}  {Colors.original}", end="")
        print()
            

    