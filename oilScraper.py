import urllib.request
from html_table_parser import HTMLTableParser
import pandas as pd

target = 'https://reports.shell.com/sustainability-report/2022/our-performance-data/greenhouse-gas-and-energy-data.html'

# get website content
req = urllib.request.Request(url=target)
f = urllib.request.urlopen(req)
xhtml = f.read().decode('utf-8')

# instantiate the parser and feed it
p = HTMLTableParser()
p.feed(xhtml)

with open('ESGOilData.csv', 'w') as f:
    for i, row in enumerate(p.tables):
        f.write(",".join(p.tables[0][i]))
    f.flush()

df = pd.read_csv('ESGOilData.csv')

print(df.to_string())

    
#" ".join(row)
#output to .csv file
#read in using pandas
#matplotlib graphs
