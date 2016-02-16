#!/usr/bin/python

from selenium import webdriver
import time
browser = webdriver.Chrome()
time.sleep(1)
url = "http://172.16.166.10"

browser.get(url)
time.sleep(3)
uelement = browser.find_element_by_css_selector(".textfield2>input[type='text']")
pelement = browser.find_element_by_css_selector(".textfield2>input[type='password']")
lelement = browser.find_element_by_css_selector(".login2>input[type='image']")

uelement.click()
time.sleep(1)
uelement.send_keys("14bcs027")  # Write your entry number instead of 14bcs027
time.sleep(1)
pelement.click()
time.sleep(1)
pelement.send_keys("L4vee0n1yiAB") # Write your password here instead of mine
time.sleep(1)
lelement.click()
time.sleep(3)

browser.close() # Remove this line, if you don't want browser to get closed after login process.


