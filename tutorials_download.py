__author__ = 'lavee_singh'

from bs4 import BeautifulSoup
import urllib2
import os
import ctypes
import sys

# This function is force glibc to read /etc/resolv.conf again
libc = ctypes.cdll.LoadLibrary('libc.so.6')
res_init = libc.__res_init

# Where do you want to save the downloaded files
directory = raw_input("Where do you want to save files: ")
if directory.startswith('/'):
    os.chdir(directory)
else:
    os.chdir(os.path.join(os.getcwd(), directory))
res_init()


url = raw_input("""You're here to download the tutorials.
    Enter what you want to download: """)
black = ['php']
if url in black:
    print "Sorry tutorial for your choice is not available."
    sys.exit(1)

base = "http://tutorialspoint.com/"
url = base + url
print "Fetching html...."

# Fetch the html to store in htm
htm = urllib2.urlopen(url).read()
print "Creating Soup...."
soup = BeautifulSoup(htm, "lxml")
links = []
print "Finding all the links....",
for link in soup.find_all('a'):
    links.append(link.get('href'))
    # links will be appended in /html/blah/blah
    # And I've to convert the links into
    # http://www.tutorialspoint.com/html/.......

toadd = 'http://www.tutorialspoint.com'
print "Modifying links...."
for i in xrange(len(links)):
    links[i] = toadd + links[i]

print "Starting the traversal of all the links...."
for i in xrange(len(links)):
    try:
        if '.pdf' in links[i]:
            command = "wget " + links[i]
            print "Downloading ...."
            os.system(command)
        elif '.htm' == links[i][-4:]:
            try:
                htm2 = urllib2.urlopen(links[i])
                htm2 = htm2.read()
                soup2 = BeautifulSoup(htm2, "lxml")
                for link2 in soup2.find_all('a'):
                    if link2.get('href')is not None and'.pdf'in link2.get('href'):
                        pdf = toadd + link2.get('href')
                        command = "wget " + pdf
                        print "Downloading ....", pdf
                        os.system(command)

            except urllib2.URLError:
                print "Skipped"

        else:
            print "It's not a proper link"
    except KeyboardInterrupt:
        print "User manually stopped downloading."
        break
