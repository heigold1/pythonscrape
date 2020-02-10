#!/usr/bin/python3

import requests
import dateutil.parser

response = requests.head('https://www.sec.gov/Archives/edgar/data/1505952/000150595219000041/earningsrelease8-kfy20q2.htm')
last_modified = response.headers.get('Last-Modified')
print("last_modified is *" + str(last_modified) + "*")
if last_modified:
    last_modified = dateutil.parser.parse(last_modified)
    print("last_modified is *" + str(last_modified) + "*")


