from .data import paint_data
from pathlib import Path
import csv
from typing import Union


class Paint:
    """

    """
    @classmethod
    def create_catalog(cls, path: Union[Path, str]=None):
        path = Path(path or paint_data)
        for row in csv.reader(path.open()):
            print(row)


    def __init__(self, color: tuple[int, int, int], name: str, line: str):
        self.color = color
        self.name = name
        self.line = line