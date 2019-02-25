#!/usr/bin/python

# Prerequisites: requests, beautifulsoup4
#   $ pip install requests
#	$ pip install beautifulsoup4


import requests
from bs4 import BeautifulSoup


# request web page content
page = requests.get('https://www.w3schools.com/html/html_tables.asp')

contents = page.content

# Some other BS4 examples 
# from https://gist.github.com/bradmontgomery/1872970
# data = {}
# for a in samples:
#     title = a.string.strip()
#     data[title] = a.attrs['href']


# parse web page for content
soup = BeautifulSoup(contents, 'html.parser')

# Print all the table cells (data) in the "Customers" table
table = soup.find(lambda tag: tag.name=='table' and tag.has_attr('id') and tag['id']=="customers") 
for item in table.find_all('td'):
    print item


