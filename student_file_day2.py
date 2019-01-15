############################
#     Writing to CSV       #
############################

import csv
from bs4 import BeautifulSoup
import requests

csvPath = './output.csv'  # The '.' indicates the directory in which the Python file is running
header = ['Country', 'Capital', 'Population', 'Area (sq-km)']

# Create a CSV file and write the headers to it
with open(csvPath, "w", newline="") as csv_file:  # Opens / creates the file
    writer = csv.writer(csv_file, delimiter=',')  # Converts the file to a Python CSV "object"
    writer.writerow(header)  # Writes a list of strings to the CSV file, using the delimiter

sampleData = ['Meowistan', 'Felixburg', '3,800,000', '1,385,382']

# Often we'll have to clean the data we add to a CSV file. For instance, we don't want commas in our numbers.
for x in range(0, len(sampleData)):
    sampleData[x] = sampleData[x].replace(',', '')

# Open the CSV file we just created and append some data to it
with open(csvPath, "a", newline="") as csv_file:  # The 'a' parameter shows that we want to add data, not overwrite it
    writer = csv.writer(csv_file, delimiter=',')
    writer.writerow(sampleData)

############################
#       Web Scraping       #
############################

url = 'http://example.webscraping.com/places/default/view/United-States-240'
page = requests.get(url)
soup = BeautifulSoup(page.text, "html.parser")

# print(soup.prettify())
rawData = soup.body.findAll(class_='w2p_fw')
for x in rawData:
    print(x.text)

outputData = [rawData[4].text, rawData[5].text, rawData[2].text, rawData[1].text]
for x in range(0, len(outputData)):
    outputData[x] = outputData[x].replace(',', '').replace('square kilometres', '').strip()

with open(csvPath, "a", newline="") as csv_file:
    writer = csv.writer(csv_file, delimiter=',')
    writer.writerow(outputData)
