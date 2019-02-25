#!/usr/bin/python

# This script reads a CSV and generates a KML using a name field and a latitute
# longitude string.
# Created by: Devin Miller

# Usage: $ ./scrape-csv-to-kml.py


"""
<?xml version="1.0" encoding="UTF-8"?>
<kml xmlns="http://www.opengis.net/kml/2.2" xmlns:gx="http://www.google.com/kml/ext/2.2" xmlns:kml="http://www.opengis.net/kml/2.2" xmlns:atom="http://www.w3.org/2005/Atom">
<Document>
    <name>Lakes.kml</name>
    <Placemark>
        <name>Lake Name</name>
        <Point>
            <coordinates>75.001,12.001,0</coordinates>
        </Point>
    </Placemark>
</Document>
</kml>
"""

import csv

# ==============================================================================
# ----- Configuration Start -----

# NOTE - make sure these indexes match up and are correct or the script will not
# work as expected
#
# Column with the name of the geospatial source; Column 'A' in Excel
# Example of data in cell 'Cubbon Park'
NAME_INDEX = 0

# Column with the lat, long string; Column 'C' in Excel
# Example of data in cell '77.5907397,12.9763472'
LAT_LONG_INDEX = 2

# The CSV file which will be read
CSV_FILE_INPUT = "input.csv"

# The name of the KML file which will be generated
KML_FILENAME_OUTPUT = "output.kml"

# ----- Configuration End -----
# ==============================================================================


# CONSTANTS - Do not change these...
KML_START = \
"""<?xml version="1.0" encoding="UTF-8"?>
<kml xmlns="http://earth.google.com/kml/2.1">
    <Document>
"""

KML_END = """    </Document>
</kml>"""


def read_csv_file(csv_file_path):
    # Read all the rows of the CSV and place into a list 'record_list'
    record_list = list()
    # Opening with Universal mode because of an issue with the newline characters
    with open(csv_file_path, 'rU+') as f:
        reader = csv.reader(f)
        first_iteration = True
        for record in reader:
            # Skip the first row if it's the header
            if first_iteration:
                first_iteration = False
                continue
            record_list.append(record)
    return record_list


def write_kml_file(record_list):
    f = open(KML_FILENAME_OUTPUT, 'w')  # open for 'w'riting
    f.write(KML_START)
    f.write("<name>{0}</name>".format(KML_FILENAME_OUTPUT))

    # Get the name and lat/long for each row using indexes
    # NOTE - Check if these indexes are correct when using different CSVs

    # Write KML file here
    for record in record_list:
        # print(record[name_index], record[lat_lng_index])

        apartment_name = record[NAME_INDEX]
        apartment_name = apartment_name.replace("&", "&amp;")

        # TODO - write the KML dynamic content here
        f.write("<Placemark>\n")
        f.write("<name>{0}</name>\n".format(apartment_name))
        f.write("<Point>\n")
        f.write("<coordinates>{0},0</coordinates>\n".format(record[LAT_LONG_INDEX]))
        f.write("</Point>\n")
        f.write("</Placemark>")

    f.write(KML_END)
    f.close()  # close the file

    # Prints the output of the KML file to the terminal
    # Disabled for now as it's useful only for debugging
    # f = open(KML_FILENAME_OUTPUT)  # if no mode is specified, 'r'ead mode is assumed by default
    # while True:
    #     line = f.readline()
    #     if len(line) == 0:  # Zero length indicates EOF
    #         break
    #     # print(line, end='')
    #     print(line)
    # f.close()  # close the file


def main():
    record_list = read_csv_file(csv_file_path=CSV_FILE_INPUT)
    # Write the names of apartments with their lat/lng into a KML
    write_kml_file(record_list=record_list)
    print("Done! Wrote the KML file.")


if __name__ == "__main__":
    main()
