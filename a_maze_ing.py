#!/usr/bin/env python3
from sys import argv, stderr, exit
from importlib.util import find_spec


if find_spec("pydantic") is not None:
    ...
else:
    print("you did not install the pydintic yet", file=stderr)
    exit(1)


def file_processor(file_name: str) -> dict[str, str]:
    """
    This function is take the file that pass from main
    and read from it and return the encoded as a dict

    made by mabu-are

    the project end hear if:
    1- error in open or read
    2- if the Requirement fewer than 5

    btw:
    we still dos not check if the arg validate yet
    """
    try:
        result = {}
        with open(file_name, 'r') as file:
            for line in file:
                if not line.strip():  # if the line is empty will skip it
                    continue
                if line.strip().startswith('#'):
                    continue

                key, value = line.strip().split('=', 1)
                result[key.strip()] = value.strip()

        if len(result) >= 5:  # 5 is the less arg must bee in the file
            return result
        else:
            raise Exception(
                f"the arg in {file_name} is less than the Requirement!!"
                "\n please check your file and try again"
            )

    except Exception as error:
        print(error, file=stderr)
        exit(1)


def main() -> None:
    """
    The main is the function that start the whole project with

    made by mabu-are

    this function make check that you run the code with the correct
    way then start calling the other function
    """

    if len(argv) != 2:
        print("Error: expect 1 valid file exist", file=stderr)
        print(f"Usage: python {argv[0]} <config_file>", file=stderr)
        exit(1)

    try:
        from maze_package import (
            dict_validate, ConfigError, create_maze,
            drawing_a_maze, solve_maze, output_file,
        )

        # الالوان
        colors = [
            '\033[92m',  # اخضر
            '\033[94m',  # ازرق
            '\033[93m',  # اصفر
            '\033[95m',  # زهري
        ]
        my_dict: dict[str, str] = file_processor(argv[1])

        maze_config = dict_validate(my_dict)
        change_colors = 0  # Absher Hai changed the name
        maze, pattern_42 = create_maze(maze_config)
        solution_path = solve_maze(maze, maze_config)
        show_path = False
        drawing_a_maze(
                maze, maze_config, pattern_42, colors[change_colors],
                show_path, solution_path
                )
        output_file(maze_config, maze)

        while True:
            input_variable = int(input(
                "\nA-Maze-ing\n1. Re-generate a new maze\n"
                "2. Show/Hide path from entry to exit\n"
                "3. Rotate maze colors\n4. Quit\nChoice? (1-4):"
            ))

            if input_variable == 1:
                my_dict = file_processor(argv[1])
                maze_config = dict_validate(my_dict)
                maze, pattern_42 = create_maze(maze_config)
                print(pattern_42)
                solution_path = solve_maze(maze, maze_config)
                show_path = False
                drawing_a_maze(maze, maze_config,
                               pattern_42, colors[change_colors])
                output_file(maze_config, maze)
            elif input_variable == 2:
                show_path = not show_path
                drawing_a_maze(
                        maze, maze_config, pattern_42, colors[change_colors],
                        show_path, solution_path
                        )
            elif input_variable == 3:
                if change_colors >= len(colors) - 1:
                    change_colors = 0
                else:
                    change_colors += 1
                path_to_draw = solution_path if show_path else None
                drawing_a_maze(
                    maze, maze_config, pattern_42, colors[change_colors],
                    show_path, path_to_draw
                )
            elif input_variable == 4:
                exit(0)
            else:
                print("Invalid choice, please enter 1-4.")

    except ConfigError as error:
        print(f"Configuration Error:\n{error}", file=stderr)
        exit(1)

    except KeyboardInterrupt:
        print("\nAn unauthorized character has been pressed.")
        exit(1)
    except Exception as error:
        print(f"Unexpected validation error: {error}", file=stderr)


if __name__ == "__main__":
    main()
