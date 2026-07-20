from .solve_maze import solve_maze


def output_file(maze_config: dict[str, str], maze: list[list]):
    """
    Export the generated maze structure and its solution path to a file.

    Parameters:
    maze_config: Configuration dictionary containing entry/exit coordinates.
    maze: 2D list of Cell objects representing the maze layout.

    Developed by aabtah.
    """
    with open("maze.txt", "w") as f:
        # Convert Cell directions to hexadecimal representation
        for i in maze:
            for j in i:
                x = 0
                if j.north:
                    x += 1
                if j.east:
                    x += 2
                if j.south:
                    x += 4
                if j.west:
                    x += 8
                f.write(f"{x:X}")
            f.write("\n")

        # Write entry and exit points
        f.write(f"\n{maze_config.entry[0]},{maze_config.entry[1]}\n")
        f.write(f"{maze_config.exit[0]},{maze_config.exit[1]}\n")

        # Solve the maze and record the path directions
        solution = solve_maze(maze, maze_config)
        for i in range(len(solution) - 1):
            x, y = solution[i]
            x_new, y_new = solution[i + 1]
            if x_new == x and y_new == y + 1:
                f.write("N")
            elif x_new == x and y_new == y - 1:
                f.write("S")
            elif x_new == x + 1 and y_new == y:
                f.write("E")
            elif x_new == x - 1 and y_new == y:
                f.write("W")
