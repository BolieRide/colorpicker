#!/usr/bin/env python3
"""Produce an image with color patches representative of
colors found in the input image. 

Requires Pillow and SciPy (Numpy is a prereq of SciPy)

> python3 -m pip install scipy
> python kpalette.py -i image.png -o palette.png

"""


from PIL import Image
from scipy.cluster.vq import kmeans
import numpy as np


def color_palette_from_image(
    image: Image, ncolors: int = 16
) -> list[tuple[int, int, int, int]]:
    """Computes a color palette based on color value clusters in the input image.

    The returned color palette is a list of color tuples whose values are:
    red, green, blue and alpha.

    :param image: PIL.Image
    :param ncolors: int defaults to 16
    :returns: list[tuple[int, int, int, int]]
    """

    npixels = image.width * image.height

    # There is a lot going on in this next line, but start from the "inside" and work
    # your way "out":
    #
    # 1. get the colors from the image with a maximum of `npixels`
    #
    # 2. iterate thru the returned values, seperating them into `count` and a tuple
    #    named `color` which is a RGBA value and create a list of those tuples.
    #
    # 3. We feed that list of color tuples to Numpy's array object constructor and
    #    tell Numpy that the values in the array should be interpreted as floats.

    colors = np.array([color for count, color in image.getcolors(npixels)], dtype=float)

    # This looks too simple to work!  We feed our prepared colors to the kmeans
    # function and tell it to cluster around `ncolors`.

    centers, mean_distance = kmeans(colors, ncolors)

    # We want to return something that looks like the input, a list of color tuples,
    # so we will iterate thru `centers`, which is Numpy array of float 4-tuples.

    palette = []
    for color in centers.round().astype(int).tolist():
        palette.append(tuple(color))

    return palette


def image_from_palette(
    palette: list[tuple[int, int, int, int]],
    patch_width: int = 128,
    patch_height: int = 128,
) -> Image:
    """Creates a rectangular PIL.Image with patches for each color color in `palette`.

    Each patch in the image will be (patch_width, patch_height) in dimension,
    and in the order given by `palette`.

    :param palette: list of RGBA color tuples
    :param patch_width: int defaults to 128
    :param patch_height: int defaults to 128
    :return: PIL.Image
    """

    size = (patch_width * len(palette), patch_height)

    image = Image.new("RGBA", size, 0)

    for col, color in enumerate(palette):
        patch = (patch_width * col, 0, patch_width * (col + 1), patch_height)
        image.paste(color, box=patch)

    return image


if __name__ == "__main__":

    from argparse import ArgumentParser

    parser = ArgumentParser()
    parser.add_argument("--input-file", "-i", type=str)
    parser.add_argument("--output-file", "-o", type=str, default="palette.png")
    parser.add_argument("--verbose", "-v", default=False, action="store_true")
    parser.add_argument("--palette-length", "-p", type=int, default=16)
    args = parser.parse_args()

    try:
        if args.verbose:
            print(
                f"Finding a palette of {args.palette_length} colors for {args.input_file}"
            )
        im = Image.open(args.input_file)

        if args.verbose:
            print("Generating palette...")

        palette = color_palette_from_image(im, args.palette_length)

        if args.verbose:
            print(f"Done! Found a palette for {args.input_file}")
            for n, (r, g, b, a) in enumerate(palette):
                print(f"{n:3d} #{r:02x}{g:02x}{b:02x}")

        if args.verbose:
            print("Creating in-memory palette Image..")

        pim = image_from_palette(palette)

        if args.verbose:
            print("Finished creating in-memory Image!")

        if args.verbose:
            print(f"Writing palette to {args.output_file}")

        pim.save(args.output_file)

        if args.verbose:
            print(f"Done! Created palette {args.output_file} for {args.input_file}")

    except Exception as error:
        print(f"Error occurred: {error}")
        exit(1)
