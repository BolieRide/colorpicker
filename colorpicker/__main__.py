"""

"""
import sys

from argparse import ArgumentParser
from .palette import Palette, KPalette, MCPalette
from datetime import datetime
from .paint import Paint

def main() -> None:
    """Learning the argusment parser
    add the path/name of an image
    add a path/name of the output file that will contain the colors from the image

    Note -- there needs to be an index of location on the image to color in the output file

    The Picker calls the module picker with a class called Picker.

    """
    parser = ArgumentParser()

    parser.add_argument("--input-image", "-i", type=str, help="Path to the input image.",default=None )
    parser.add_argument("--output-file", "-o", type=str, help="Path to write output colors",default=None)
    parser.add_argument("--number-of-colors", "-n", type=int, default=16)

    args = parser.parse_args()

    catalog = Paint.create_catalog('D:\PDM_Class\colorpicker\colorpicker\data\dakka.csv')
    # for k,v in catalog.items():
    #     print(k, v)
    # exit()
    print(args)
    # 0. Retrieve minaute paint colors from an image
    # 1. Get an image, either url or via path.
    # 2. Build a palette from source image.
    # 3. Retrieve paint catalog.
    # 4. Locate palette colors within catalog.
    # 5. Print list of colors and matching paints.
    # 6. (Optional) Matches colors on image with legend to specific paints


    palette = KPalette(args.input_image)

    if args.output_file:
        output_file = open(args.output_file, "w")
    else:
        output_file = sys.stdout

    for color in palette.colors(args.number_of_colors):
        print(color)

if __name__ == '__main__':

    main()