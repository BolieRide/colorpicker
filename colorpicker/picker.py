"""Input an image and output the color in English


"""
import sys
from PIL import Image
import webcolors
import requests
from bs4 import BeautifulSoup
import html2text
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

class Picker:
    def __init__(self, filepath: str) -> None:
        """
        """
        self.path = filepath
        self.image = Image.open(self.path)
        self.baseurl = "https://encycolorpedia.com"

    @property
    def color_names(self):
        try:
            return self._color_names
        except AttributeError:
            pass

        color_names = []
        for color in self.color_strings:
            if color.startswith("#"):
                color_names.append(self.get_color_name(color))
            else:
                color_names.append(color)

        self._color_names = list(set(color_names))
        return self._color_names

    def get_color_name(self, color):
        color = color[1:]
        response = requests.get(f"{self.baseurl}/{color}", verify=False)
        try:
            response.raise_for_status()
            pass
        except Exception as error:
            print(f"Error occurred {error}")
            raise
        soup = BeautifulSoup(response.text, 'html.parser')
        chunk = str(soup.find(id='information'))
        color = html2text.html2text(chunk)
        start = ".svg)"
        end = "*."
        idx1 = color.index(start)
        idx2 = color.index(end)
        phrase = color[idx1 + 31: idx2].replace("\n", " ").replace("*", "")
        return phrase.split()[-1]

    @property
    def reduce_img(self):
        try:
            return self._reduce_img
        except AttributeError:
            pass

        self._reduce_img = self.image.reduce(64)

        l = self._reduce_img.getcolors(maxcolors=20000000)
        print(len(l),"colors in reduced image")

        return self._reduce_img


    @property
    def color_strings(self):
        try:
            return self._color_strings
        except AttributeError:
            pass
        self._color_strings = []
        for count, rgb in self.reduce_img.getcolors(maxcolors=2000000):
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
        for color in self.color_names:

        # print(color, file=output)
            print(color)

