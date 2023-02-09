#!/usr/bin/env python3

import simplekml
import csv

# Load our previously-created CSV file of libraries
libraries = []
with open('plymouth-libraries.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        libraries.append(row)

# now we have a Python list of dictionaries

# Now, use simplekml to create a KML output file
# as per the simplekml documentation
kml = simplekml.Kml()
for library in libraries:
    # the coordinates need to be numeric, so convert
    # them to floating-point numbers
    lat = float(library["Latitude"])
    lon = float(library["Longitude"])
    # and add a new "point" to the KML file for this library
    kml.newpoint(name=library["LibraryName"], coords=[(lon, lat)])

kml.save("plymouth-libraries.kml")
