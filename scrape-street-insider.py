#!/usr/bin/python3

from lxml import html
import requests
from time import sleep
import json
import argparse
from random import randint
import urllib3
import sys 
import re 
import random 


urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def parse_finance_page(symbol):

  headers = {
          "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
          "Accept-Encoding":"gzip, deflate",
          "Accept-Language":"en-GB,en;q=0.9,en-US;q=0.8,ml;q=0.7",
          "Connection":"keep-alive",
          "Host":"www.streetinsider.com",
          "Referer":"https://www.streetinsider.com",

          "Upgrade-Insecure-Requests":"1",
          "User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.36"
    } 


#  print("Content-type: text/html\n\n")

  for retries in range(1):
    try:    

      url = "https://www.streetinsider.com/stock_lookup.php?LookUp=Get+Quote&q=" + symbol

      response = requests.get(url, headers = headers, verify=False)

      if response.status_code!=200:
        raise ValueError("Invalid Response Received From Webserver")


#      randomFloat = randint(1,2) + random.random()
#      print("randomFloat is " + str(randomFloat)) 
#      sys.exit() 

      sleep(randint(1,3) + random.random())

      parser = html.fromstring(response.text)

      responseText = response.text

#      print(responseText) 

      responseText = re.sub(r"\$jq\('#blocker'\).fadeIn\(500\);", "console.log('nothing')", responseText)  

      print(responseText) 


    except Exception as e:
      print("Failed to process the request, Exception:%s"%(e))

symbol = sys.argv[1] 

scraped_data = parse_finance_page(symbol)



