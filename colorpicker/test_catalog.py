from pathlib import Path
import csv

path = Path('D:\PDM_Class\colorpicker\colorpicker\data\dakka.csv')
catalog = {}
brand = {}
rows = list(csv.reader(path.open()))
header = rows[0]
# brand.fromkeys(header[1:], None)
print(brand)
for row in rows[1:]:
    idx, *names = row
    brand = dict((zip(header[1:], names)))
    catalog.update({idx: brand})
    # print(catalog)
    # print(idx, ' ', brand)
print(catalog)
