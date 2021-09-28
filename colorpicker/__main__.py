"""

"""
import sys

from argparse import ArgumentParser
from .picker import Picker


def main() -> None:
    """

    """
    parser = ArgumentParser()

    parser.add_argument("--input-image", "-i", type=str, help="Path to the input image.",default=None )
    parser.add_argument("--output-file", "-o", type=str, help="Path to write output colors",default=None)

    args = parser.parse_args()

    print(args)

    input_picker = Picker(args.input_image)

    if args.output_file:
        output_file = open(args.output_file, "w")
    else:
        output_file = sys.stdout

    input_picker.find_colors(output_file)



if __name__ == '__main__':

    main()