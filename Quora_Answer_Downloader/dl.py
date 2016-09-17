
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from pyvirtualdisplay import Display 
import pdfkit
import os
import re
import subprocess as sp

url = raw_input("Please enter the url of the webpage: ");
display = Display(visible=0, size=(1024, 768))
display.start()
browser = webdriver.Chrome()

sp.call(["notify-send", "Attention", "Opening the browser, and getting the webpage."])

browser.get(url)
time.sleep(3)
body = browser.find_element_by_tag_name("body")
t = 25

print "Loading all the answers...."
sp.call(["notify-send", "Attention", "Lazy loading of answers will take a minute or two, please be patient. File will be saved as answer.pdf in current directory."])
while t > 0:
	body.send_keys(Keys.END)
	time.sleep(3)
	t -= 1
print "All the answers loaded."
print "Getting the html source."
html_source = browser.page_source
print "HTML fetched."
print "now creating pdf file..."

pat = ".*www.quora.com/(.*)"
fname = re.findall(pat, url)[0]
fname = fname + '.pdf'

pdfkit.from_string(html_source, fname)
print "File will be saved as " + fname + " in current directory."
print "File created."
browser.close()
display.stop()
os.system("xdg-open "+fname)