"""Here is my docstring."""
from pathlib import Path
from typing import Union, List, Tuple
from PIL import Image
from scipy.cluster.vq import kmeans
import numpy as np


class Palette:
    def __init__(self, image_path: Union[str, Path]) -> None:
            self.path = Path(image_path)

    @property
    def image(self) -> Image:
        #lazy accessor  & cached accessor
        try:
            return self._image
        except AttributeError:
            pass

        self._image = Image.open(self.path, "r")
        return self._image

    def colors(self, ncolors: int=None) -> List[Tuple[int, int, int, int]]:

        colors = self.image.getcolors(maxcolors=self.image.width*self.image.height)
        sorted(colors, key=lambda item: item[0], reverse=True)
        if ncolors is None:
            return [color for count, color in colors]
        return [color for count, color in colors][:ncolors]


class KPalette(Palette):
    def colors(self, ncolors: int=16) -> List[Tuple[int, int, int, int]]:
        colors = np.array(super().colors(), dtype=float)
        centers, mean_distance = kmeans(colors,ncolors)
        return [tuple(color) for color in centers.round().astype(int).tolist()]


class MCPalette(Palette):
    def colors(self, ncolors: int=None) -> List[Tuple[int, int, int, int]]:
        pass


class MagicPalette(Palette):
    def colors(self, ncolors: int=None) -> List[Tuple[int, int, int, int]]:
        pass