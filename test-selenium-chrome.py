#!/usr/bin/python3

from pyvirtualdisplay import Display
from selenium import webdriver

display = Display(visible=0, size=(800, 600))
display.start()
driver = webdriver.Chrome()
driver.get('https://www.streetinsider.com/stock_lookup.php?LookUp=Get+Quote&q=TNXP')
#driver.get('https://finance.yahoo.com/quote/TNXP?p=TNXP&.tsrc=fin-srch')
#driver.get('http://christopher.su')

print(driver.page_source)


