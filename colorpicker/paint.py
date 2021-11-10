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
        rows = list(csv.reader(path.open()))
        header = rows[0]
        for row in rows[1:]:
            idx, color, *names = row
            for name in names:
                if name == '-':
                    continue
                catalog.setdefault(color, []).append(cls(color, name, idx))
        return catalog



    def __init__(self, color: tuple[int, int, int], name: str, line: str):
        self.color = color
        self.name = name
        self.line = line

    def distance(self, other: tuple[int, int, int]):
        pass