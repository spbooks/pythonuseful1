#!/usr/bin/env python3

import json

# read the contents of the JSON file into
# a Python data structure
with open("libraries.json") as fp:
    library_data = json.load(fp)

# library_data is now a Python dictionary
print(library_data.keys())

# this will print
# dict_keys(['type', 'name', 'crs', 'features'])
# which are indeed the top-level keys from this file

print(library_data["features"][0]["properties"]["LibraryName"])

# this will print
# Central Library
# which is the LibraryName value in properties for the first
# entry in the features list in the JSON file

import csv

# now write the data out as CSV
# to write a CSV file, we need a list of column header names
# these will be the keys of the properties of the first 
# entry in "features", since all libraries have the same keys
header_names = library_data["features"][0]["properties"].keys()

with open("libraries.csv", "w", newline="") as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=header_names)
    writer.writeheader()
    for library in library_data["features"]:
        writer.writerow(library["properties"])
