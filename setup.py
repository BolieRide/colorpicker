import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Colorpicker_BolieRide",
    version="0.0.1",
    author="BolieRide",
    author_email="BolieRide@gmail.com",
    description="Select colors in an image",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/BolieRide/colorpicker",
    project_urls={
        "Bug Tracker": "https://github.com/BolieRide/colorpicker/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "colorpicker"},
    packages=setuptools.find_packages(where="colorpicker"),
    python_requires=">=3.6",
)