#!/usr/bin/env python3
from sys import argv, stderr, exit
# from typing import IO
import random


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
        try:
            from maze_package import (
                    dict_validate, ConfigError,  create_maze, drawing_a_maze
                    )
            # هذا عشان موضوع الالوان في الكود بتقدر تضيف الالوان الي بدك إياها
            colors = [
        '\033[92m', # هذا اخضر 
        '\033[94m', # ازرق 
        '\033[93m', # اصفر 
        '\033[95m', # زهري لون البنات عشان لو بنت عملت ريفيو 
        ]
            my_dict: dict[str, str] = file_processor(argv[1])

            maze_config = dict_validate(my_dict)
            x = 0
            drawing_a_maze(create_maze(maze_config), maze_config, colors[x])

            
            while True:
                input_variable = int(input("""
A-Maze-ing
1. Re-generate a new maze
2. Show/Hide path from entry to exit
3. Rotate maze colors
4. Quit
Choice? (1-4):"""))
                if input_variable == 1:
                    my_dict: dict[str, str] = file_processor(argv[1])
                    maze_config = dict_validate(my_dict)
                    drawing_a_maze(create_maze(maze_config), maze_config,colors[x])
                elif input_variable == 2:
                    pass
                elif input_variable == 3:
                    if x == len(colors) - 1:
                        x = 0
                    x += 1
                    drawing_a_maze(create_maze(maze_config), maze_config,colors[x])


                elif input_variable == 4:
                    exit(0)
                else:
                    print("Invalid choice, please enter 1-4.")

        except ConfigError as error:
            print(f"Configuration Error:\n{error}", file=stderr)
            exit(1)

    except KeyboardInterrupt:
        print("\nAn unauthorized character has been pressed on the keyboard.")
        exi
    except Exception as error:
        print(f"Unexpected validation error: {error}", file=stderr)
        exit(1)

 
if __name__ == "__main__":
    main()
