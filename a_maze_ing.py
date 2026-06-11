#!/usr/bin/env python3
from sys import argv, stderr, exit
from typing import IO
from ... import dict_validate


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

    my_dict: dict[str, str] = file_processor(argv[1])
#    print(my_dict)
    dict_validate(my_dict)


if __name__ == "__main__":
    main()
