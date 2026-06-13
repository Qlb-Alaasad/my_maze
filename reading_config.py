
"""
Where to read the file
"""

from pydantic import BaseModel, Field, model_validator


class CoordinateError(ValueError):
    """
    Error following coordinates
    """
    pass


class Configfile(BaseModel):
    """
    The class for collecting and verifying data
    """
    
    width: int = Field(gt=0)
    height: int = Field(gt=0)
    entry: tuple[int, int]
    exit: tuple[int, int]
    output_file: str
    perfect: bool
    
    @model_validator(mode='after')
    def check_boundaries(self):
        """
        A function for additional 
        verification to ensure that the exit and entry are not equal, 
        and also that the image size is not larger.
        """
        
        x, y = self.entry
        x2, y2 = self.exit
        if not (0 <= x < self.width) or not(0 <= y < self.height):
            raise CoordinateError("The coordinates entered are incorrect")
        if not (0 <= x2 < self.width) or not(0 <= y2 < self.height):
            raise CoordinateError("The coordinates are incorrect")
        if self.exit == self.entry:
            raise CoordinateError("The entry and exit coordinates are equal")


def reading_config(file: str) -> Configfile:
    """
    The specific logic behind converting the data in the file into real data
    """
    
    dicts: dict = {}
    with open(file, "r") as c:
        for line in c:
            l = line.strip()
            if not l or l.startswith("#"):
                continue
            if '=' not in l:
                raise ValueError(f"There is a problem with the formatting of the config.txt file in line {line}")
            key, value = l.split('=', 1)
            dicts[key.strip().lower()] = value.strip()
    required_keys = ["width", "height", "entry", "exit", "output_file", "perfect"]
    for key in required_keys:
        if key not in dicts:
            raise ValueError(f"Missing required configuration key: {key}")

    width1 = int(dicts["width"])
    height1 = int(dicts["height"])
    entry1 = dicts["entry"].split(',')
    exit1 = dicts["exit"].split(',')
    output_file1: str = dicts["output_file"]
    perfect1 = dicts["perfect"].lower() == "true"
    
        
    if len(entry1) != 2 or len(exit1) != 2:
        raise ValueError("error")
    
    entry2 = int(entry1[0]), int(entry1[1])
    exit2 = int(exit1[0]), int(exit1[1])
    
    return Configfile(
    width=width1,
    height=height1,
    entry=entry2,
    exit=exit2,
    output_file=output_file1,
    perfect=perfect1,
    )
    