#!/usr/bin/pythoption:'ascii' codec can't encode character '\xa9' in position 134670 lxml import html
import requests
from time import sleep
import json
import argparse
from random import randint
import urllib3
import sys 
import re 
import random 

from itertools import cycle
import traceback


urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def get_proxies():
    url = 'https://free-proxy-list.net/'
    response = requests.get(url)
    parser = fromstring(response.text)
    proxies = set()
    for i in parser.xpath('//tbody/tr')[:10]:
        if i.xpath('.//td[7][contains(text(),"yes")]'):
            #Grabbing IP and corresponding PORT
            proxy = ":".join([i.xpath('.//td[1]/text()')[0], i.xpath('.//td[2]/text()')[0]])
            proxies.add(proxy)
    return proxies


def parse_finance_page(symbol):

  headers = {
          "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
          "Accept-Encoding":"gzip, deflate",
          "Accept-Language":"en-GB,en;q=0.9,en-US;q=0.8,ml;q=0.7",
          "Connection":"keep-alive",
          "Host":"www.streetinsider.com",
          "Referer":"https://www.streetinsider.com",
#          "Host":"finance.yahoo.com",
#          "Referer":"https://finance.yahoo.com",



          "Upgrade-Insecure-Requests":"1",
          "User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.36"
    } 


  for retries in range(1):
    try:    

      url = "https://www.streetinsider.com/stock_lookup.php?LookUp=Get+Quote&q=" + symbol
#      url = "https://finance.yahoo.com/quote/" + symbol + "?p=" + symbol

      response = requests.get(url, headers = headers, verify=False) 

      if response.status_code!=200:
        raise ValueError("Invalid Response Received From Webserver")



      sleep(randint(1,3) + random.random())

      responseText = response.text

      responseText = re.sub(r"\$jq\('#blocker'\).fadeIn\(500\);", "console.log('nothing')", responseText)  

      responseText = responseText.encode('ascii') 

      print(responseText) 


    except Exception as e:
      print("Failed to process the request, Exception:%s"%(e))

symbol = sys.argv[1] 

scraped_data = parse_finance_page(symbol)



