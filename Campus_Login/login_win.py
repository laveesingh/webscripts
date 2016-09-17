#!C:\Python\python.exe

from selenium import webdriver
import time
from pyvirtualdisplay import Display

#display = Display(visible=0, size=(800, 500))
#display.start()

browser = webdriver.Chrome("C:\Python27\Scripts\chromedriver.exe")
time.sleep(1)
url = "http://172.16.166.10"

browser.get(url)
time.sleep(3)
uelement = browser.find_element_by_css_selector(".textfield2>input[type='text']")
pelement = browser.find_element_by_css_selector(".textfield2>input[type='password']")
lelement = browser.find_element_by_css_selector(".login2>input[type='image']")

uelement.click()
time.sleep(1)
uelement.send_keys("")  # Write your entry number instead of 14bcs027
time.sleep(1)
pelement.click()
time.sleep(1)
pelement.send_keys("") # Write your password here instead of mine
time.sleep(1)

#iex ((new-object net.webclient).DownloadString('https://chocolatey.org/install.ps1')); choco install -y python python-pip wget unzip; pip install pyvirtualdisplay selenium; wget -nc http://chromedriver.storage.googleapis.com/2.9/chromedriver_win32.zip; unzip ~\Downloads\chromedriver.zip; mv ~\Downloads\chromedriver.exe C:\Python27\Scripts

lelement.click()
time.sleep(3)

browser.close() # Remove this line, if you don't want browser to get closed after login process.

#display.stop()
