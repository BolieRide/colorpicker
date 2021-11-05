"""

"""
import sys

from argparse import ArgumentParser
from .picker import Picker
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

    args = parser.parse_args()
    catalog = Paint.create_catalog('D:\PDM_Class\colorpicker\colorpicker\data\dakka.csv')
    # for k,v in catalog.items():
    #     print(k, v)
    # exit()
    print(args)

    input_picker = Picker(args.input_image)

    if args.output_file:
        output_file = open(args.output_file, "w")
    else:
        output_file = sys.stdout

    start = datetime.now()
    input_picker.find_colors(output_file,propername=False)
    print("Elapsed: ", datetime.now() - start)


if __name__ == '__main__':

    main()