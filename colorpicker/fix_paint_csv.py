import pandas as pd
import numpy as np

# Pull in the csv that was pulled from https://github.com/redgrimm/paint-conversion
# Then used b4s to pull data out of the html
df1 = pd.read_csv("d:\PDM_class\colorpicker\colorthingy.csv")

# The html had the distance from the other hex color in the cell.  Strip it out.
df1["Army Painter"] = df1["Army Painter"].map(lambda x: str(x)[:-4])
df1["Vallejo Game"] = df1["Vallejo Game"].map(lambda x: str(x)[:-4])
df1["Vallejo Model"] = df1["Vallejo Model"].map(lambda x: str(x)[:-4])
df1["P3 Formula"] = df1["P3 Formula"].map(lambda x: str(x)[:-4])

# Create an new cell with the hex color.  The hex color is located at the end of the cell.
# It doesn't make sense, because it is 7 characters from the end of the cell.  However, it
# it requires a -10 to get the complete code...
df1["Army Painter Hex"] = df1["Army Painter"].apply(lambda x: str(x)[-10:])
df1["Army Painter"] = df1["Army Painter"].map(lambda x: str(x)[:-10])
df1["P3 Formula Hex"] = df1["P3 Formula"].apply(lambda x: str(x)[-10:])
df1["P3 Formula"] = df1["P3 Formula"].map(lambda x: str(x)[:-10])
df1["Vallejo Model Hex"] = df1["Vallejo Model"].apply(lambda x: str(x)[-10:])
df1["Vallejo Model"] = df1["Vallejo Model"].map(lambda x: str(x)[:-10])
df1["Vallejo Game Hex"] = df1["Vallejo Game"].apply(lambda x: str(x)[-10:])
df1["Vallejo Game"] = df1["Vallejo Game"].map(lambda x: str(x)[:-10])
df1["Citadel Hex"] = df1["Citadel"].apply(lambda x: str(x)[-7:])
df1["Citadel"] = df1["Citadel"].map(lambda x: str(x)[:-7])

df1.to_csv("color_new.csv")
