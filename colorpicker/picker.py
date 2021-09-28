"""a picker

"""
import sys

class Picker:
    def __init__(self, filepath: str) -> None:
        """

        @rtype: object
        """
        self.path = filepath

    def find_colors(self, output) -> None:
        """Output is an open file object.

        @param output:
        @return:
        """
        output = output or sys.stdout

        print(f"find colors {self.path}", file=output)