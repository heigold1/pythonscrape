#!/usr/bin/python3
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pyvirtualdisplay import Display

options = Options()
options.binary_location = '/usr/bin/google-chrome'
options.add_argument('--disable-extensions')    
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--remote-debugging-port=9515') 
options.add_argument('--disable-setuid-sandbox')
options.add_argument('--disable-gpu') 
options.add_argument('--log-path=/var/log/chromedriver')

display = Display(visible=0, size=(800, 800))
display.start()

driver = webdriver.Chrome(executable_path='/usr/local/bin/chromedriver', options=options)  # Optional argument, if not specified will search path.i
# driver.maximize_window() 
driver.get('http://www.google.com/')
time.sleep(5)  # Let the user actually see something!
search_box = driver.find_element_by_name('q')
search_box.send_keys('ChromeDriver')
search_box.submit()
time.sleep(5)  # Let the user actually see something!
driver.quit()
