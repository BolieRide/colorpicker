"""Input an image and output the color in English


"""
import sys
from PIL import Image
import webcolors

class Picker:
    def __init__(self, filepath: str) -> None:
        """
        """
        self.path = filepath
        self.image = Image.open(self.path)

    @property
    def color_strings(self):
        try:
            return self._color_strings
        except AttributeError:
            pass
        self._color_strings = []
        for count, rgb in self.image.getcolors(maxcolors=20000000):
            rgb_colors = rgb[:3]
            try:
                color: str = webcolors.rgb_to_name(( rgb_colors))
                self._color_strings.append(color)
            except ValueError as error:
                r,g,b = rgb_colors
                self._color_strings.append(f"#{r:02x}{g:02x}{b:02x}")
        return self._color_strings

    def find_colors(self, output, propername=True) -> None:
        """Output is an open file object.

        @param output:
        @return:
        """

        output = output or sys.stdout
        for color in self.color_strings:
            if propername:
                if color.startswith("#"):
                    continue
            print(color, file=output)

