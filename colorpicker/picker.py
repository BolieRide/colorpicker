"""Input an image and output the color in English


"""
import sys

class Picker:
    def __init__(self, filepath: str) -> None:
        """
        """
        self.path = filepath

    def find_colors(self, output) -> None:
        """Output is an open file object.

        @param output:
        @return:
        """
        output = output or sys.stdout

        print(f"find colors {self.path}", file=output)