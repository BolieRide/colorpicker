from .data import paint_data
from pathlib import Path
import csv
import math
from typing import Union


class Paint:
    """"""

    @classmethod
    def create_catalog(cls, path: Union[Path, str] = None) -> dict[str, list["Paint"]]:

        path = Path(path or paint_data)
        catalog = {}
        rows = list(csv.reader(path.open()))
        brands = rows[0]

        for row in rows[1:]:
            color_raw, *names = row
            # color_tuple = tuple(color_raw.to_bytes(byteorder="big"))
            color_tuple = int(color_raw, 16).to_bytes(4, byteorder="big")
            color_str = str(int(color_raw, 16))
            for column, name in enumerate(names, 1):
                if name == "-":
                    continue
                paint = cls(color_tuple, name, brands[column])
                catalog.setdefault(color_str, []).append(paint)
                print(catalog)
        return catalog

    @classmethod
    def create_brand_catalog(
        cls, path: Union[Path, str] = None
    ) -> dict[str, list["Paint"]]:

        catalog = cls.create_catalog(path)

        brand_catalog = {}

        for paints in catalog.values():
            for paint in paints:
                brand_catalog.setdefault(paint.brand, []).append(paint)

        return brand_catalog

    # dataclass
    def __init__(self, color: tuple[int, int, int], name: str, brand: str) -> None:
        self.color = color
        self.name = name
        self.brand = brand

    def distance(self, other: tuple[int, int, int]) -> float:
        """Euclidean distance between self and other."""

        # d([x,y,z], [a,b,c]) = sqrt( (x-a)**2 + (y-b)**2 + (z-c)**2)

        return math.sqrt(self.distance_squared(other))

    def distance_squared(self, other: tuple[int, int, int, int]) -> float:
        """Sum of squared-differences between self and other."""

        # sum = 0
        # for a, b in zip(self.color, other):
        #    sum += (a - b) ** 2
        # return sum

        return sum([(a - b) ** 2 for a, b in zip(self.color, other)])
