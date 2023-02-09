#!/usr/bin/env python3

# we may need modules installed for this
# pip install requests
# pip install beautifulsoup4

import requests
from bs4 import BeautifulSoup

# Use the Python requests module to fetch the web page
# Note that here we specify a particular ID, in case the HTML changes
# between when this code was written and when you're using it
response = requests.get("https://en.wikipedia.org/w/index.php?title=List_of_tallest_buildings&oldid=1136407614&useskin=vector")
# and extract its HTML
html = response.content

# Now, use BeautifulSoup to parse that HTML so we can
# extract data from it
soup = BeautifulSoup(html, "html.parser")

# The relevant table, of the tallest buildings in the world by
# height to pinnacle,  is the fifth <table> element on the page.
# If the Wikipedia HTML had an ID attribute on that table,
# we could use that to find it directly, but it doesn't.
# So we'll use that we know that it's the fifth table
# to find it, with the .select() function, which takes
# a CSS selector similar to JavaScript's querySelectorAll()
tallest_table = soup.select("table")[4]

# Make ourselves a list to store buildings in
tallest_buildings = []

# Get the title for each column, by reading the text of
# each <th> in the first row of this table
# Note that the "Height" column is two columns, m and ft,
# so we handle this differently.
column_titles = []
first_row = tallest_table.select("tr")[0]
for th in first_row.select("th"):
    column_title = th.text.strip() # .strip() removes carriage returns
    if column_title == "Height":
        # add two columns
        column_titles.append(column_title + " (m)")
        column_titles.append(column_title + " (ft)")
    else:
        # add this column title to the list
        column_titles.append(column_title) 

# Now, for each row (building) in the table after 
# the first (header) row, get the data and make a dictionary 
# for this building using the column headers we already have
for tr in tallest_table.select("tr")[1:]:
    building = {}
    tds = tr.select("td")
    # combine the header list and the data list from this row with zip()
    named_data = zip(column_titles, tds)
    for title, td in named_data:
        building[title] = td.text.strip()
    # and store this building in the list
    tallest_buildings.append(building)

import re
for building in tallest_buildings:
    # get the digits from "Height (m)" the most basic way
    height_m_digits = ""
    for character in building["Height (m)"]:
        if character.isdigit() or character == ".":
            height_m_digits += character
    building["Height (m)"] = float(height_m_digits)

    # get the digits from "Height (ft)" a slightly better way
    # using a list comprehension
    height_ft_digits = [
        character for character in building["Height (ft)"]
        if character.isdigit() or character == "."]
    height_ft_digits = "".join(height_ft_digits)
    building["Height (ft)"] = float(height_ft_digits)

    # get the digits from "Floors" using regular expressions
    floors_digits = re.findall(r"[\d.]", building["Floors"])
    building["Floors"] = int("".join(floors_digits))

    # and remove the Rank column, since Excel's row numbers do that
    del building["Rank"]

import xlsxwriter

workbook = xlsxwriter.Workbook('tallest_buildings.xlsx')
worksheet = workbook.add_worksheet()

# Add a bold red format to use to highlight cells
bold = workbook.add_format({
    'bold': True, 'font_color': 'red'
})

# Add a number format for cells with heights.
heights = workbook.add_format({'num_format': '#,##0.00'})

# Write the column titles out, by using the dictionary keys
# from the first building.
column_titles = tallest_buildings[0].keys()
row_number = 0 # we write the column titles in row 0

# Use the enumerate() function to iterate the list while
# getting the index position for each item
# enumerate([a, b, c, ...]) -> [(0, a), (1, b), (2, c), ...]

for column_number, title in enumerate(column_titles):
    worksheet.write(row_number, column_number, title, bold)

# Start from the first cell below the headers.
row_number = 1

# Iterate over the buildings and write them out row by row,
for building in tallest_buildings:
    for column_number, title in enumerate(column_titles):
        worksheet.write(row_number, column_number, building[title], heights)
    row_number += 1

# And make all the columns wide enough to fit the data in them
# Note that this is a new function as of January 2023
worksheet.autofit()

# Save the workbook and exit
workbook.close()