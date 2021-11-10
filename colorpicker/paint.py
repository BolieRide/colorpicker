from .data import paint_data
from pathlib import Path
import csv
from typing import Union


class Paint:
    """

    """
    @classmethod
    def create_catalog(cls, path: Union[Path, str] = None) -> dict:
        path = Path(path or paint_data)
        catalog = {}
        brand = {}
        rows = list(csv.reader(path.open()))
        header = rows[0]
        for row in rows[1:]:
            idx, *names = row
            brand = dict((zip(header[1:], names)))
            catalog.update({idx: brand})
        return catalog



    def __init__(self, color: tuple[int, int, int], name: str, line: str):
        self.color = color
        self.name = name
        self.line = line

    def distance(self, other: tuple[int, int, int]):
        pass