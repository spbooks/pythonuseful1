#!/usr/bin/env python3

import xml.etree.ElementTree as ET
import json

# Create a Python list to put our libraries in
libraries = []

# Use ElementTree to read the XML file
tree = ET.parse('somerset-libraries.xml')
root = tree.getroot()

# iterate over all the elements in <Root>, which are the <Row>s, 
# one per library 
for row in root:

    # make a dictionary object of this library
    # we do this by iterating over all the child elements and
    # putting their values in the dictionary
    this_library = {}
    for element in row:
        name = element.tag
        value = element.text
        this_library[name] = value
    
    # and now add the dictionary element to our list
    libraries.append(this_library)

# We have a list of libraries
# Now, let's filter it, by going through it and removing all the
# libraries with postcode BS40 or greater

for library in libraries:
    # get the third and fourth characters of the postcode, as a number
    # note that real postcode parsing is more complex than this!
    postcode = library["Postcode"]
    postcode_number = int(postcode[2:4])
    if postcode_number >= 40:
        libraries.remove(library)

# Finally, serialise the libraries list to a file
# This time, we'll serialise it to JSON
with open("somerset-libraries.json", mode="w") as fp:
    json.dump(libraries, fp, indent=2) # the indent makes the JSON be formatted

