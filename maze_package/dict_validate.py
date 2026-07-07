#!/usr/bin/env python3
from sys import stderr
try:
    from pydantic import (
        BaseModel, Field, field_validator, model_validator, ValidationError
        )
except Exception as error:
    print(error, file=stderr)
    exit(1)

from typing import Any, Optional


class ConfigError(Exception):
    """Custom exception raised when maze validation fails."""
    pass


class MazeConfig(BaseModel):
    """
    This class represents the maze configuration using Pydantic.
    All fields are validated strictly according to 42 requirements.

    made by mabu-are
    """
    width: int = Field(gt=1)  # must be greater than 1
    height: int = Field(gt=1)  # must be greater than 1
    entry: tuple[int, int]
    exit: tuple[int, int]
    output_file: str = Field(min_length=1)  # cannot be empty string
    perfect: bool = Field(default=True)
    seed: Optional[int] = Field(default=None)

    @field_validator('entry', 'exit', mode='before')
    @classmethod
    def parse_coordinates(cls, value: Any) -> tuple[int, int]:
        """
        Parses 'x,y' string into a tuple of ints before
        Pydantic validates types.

        made by mabu-are
        """
        if isinstance(value, str):
            parts = value.split(',')
            if len(parts) != 2:
                raise ValueError("coordinates must be in 'x,y' format!!")
            try:
                return (int(parts[0].strip()), int(parts[1].strip()))
            except ValueError:
                raise ValueError("coordinates must contain valid integers!!")
        raise TypeError(f"Except a str value ({value})")

    @field_validator('output_file', mode='after')
    @classmethod
    def validate_filename(cls, value: str) -> str:
        """
        Ensures the filename doesn't just contain empty spaces.

        made by mabu-are
        """
        if not value.strip():
            raise ValueError(
                    "output_file name cannot be empty or whitespaces!!"
                    )
        return value.strip()

    @model_validator(mode='after')
    def validate_maze_logic(self) -> 'MazeConfig':
        """
        Cross-field validation to check boundaries and entry != exit.

        made by mabu-are
        """
        entry_x, entry_y = self.entry
        exit_x, exit_y = self.exit

        # 1- check entry bounds
        if not (0 <= entry_x < self.width and 0 <= entry_y < self.height):
            raise ValueError(
                    f"entry point {self.entry} is out of maze bounds!!"
                    )

        # 2- check exit bounds
        if not (0 <= exit_x < self.width and 0 <= exit_y < self.height):
            raise ValueError(
                    f"exit point {self.exit} is out of maze bounds!!"
                    )

        # 3- check if entry and exit are the same
        if self.entry == self.exit:
            raise ValueError("entry and exit points must be different!!")

        return self


def dict_validate(my_dict: dict[str, Any]) -> MazeConfig:
    """
    Converts all keys to lowercase and passes them to MazeConfig.
    Raises ConfigError instead of killing the program.

    made by mabu-are

    btw:
    the validation errors are wrapped into ConfigError to be handled in main
    """
    try:
        clean_dict = {key.lower(): value for key, value in my_dict.items()}
        maze_instance = MazeConfig(**clean_dict)
        return maze_instance
    except ValidationError as error:
        # We catch Pydantic's ValidationError and raise our custom ConfigError
        raise ConfigError(str(error))
    except Exception as general_error:
        raise ConfigError(f"Unexpected validation error: {general_error}")
