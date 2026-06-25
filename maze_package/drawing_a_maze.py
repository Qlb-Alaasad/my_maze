# type: ignore
from .make42_pattern import make_42_pattern


def drawing_a_maze(maze, maze_config) -> None:
    pattern_42 = make_42_pattern(maze_config)
    RED_BG = "\033[41m"
    RESET = "\033[0m"

    for i in range(maze_config.height):
        print("+", end="")
        for j in range(maze_config.width):
            if maze[i][j].north:
                print("---", end="")

            else:
                print("   ", end="")

            print("+", end="")

        print()
        print("|", end="")
        for j in range(maze_config.width):

            bg = RED_BG if pattern_42[i][j] else ""
            reset_color = RESET if pattern_42[i][j] else ""

            if (j, i) == maze_config.entry:
                print(f"{bg} E {reset_color}", end="")
            elif (j, i) == maze_config.exit:
                print(f"{bg} X {reset_color}", end="")
            else:
                print(f"{bg}   {reset_color}", end="")

            if maze[i][j].east:
                print("|", end="")
            else:
                print(" ", end="")
        print()

    print("+", end="")
    for i in range(maze_config.width):
        if maze[maze_config.height-1][i].south:
            print("---", end="")
        else:
            print("   ", end="")
        print("+", end="")
    print()
