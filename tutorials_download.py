__author__ = 'lavee_singh'

from bs4 import BeautifulSoup
import urllib2
import os
import ctypes

def Clear(links):
    i = 0
    while i < len(links):
        if '/html' not in links[i] and ('.htm' not in links[i] or '.pdf' not in links[i]):
            del links[i]
        else: i += 1
    return

libc = ctypes.cdll.LoadLibrary('libc.so.6')
res_init = libc.__res_init # This function is force glibc to read /etc/resolv.conf again

os.chdir(raw_input("Enter the path of the directory where you want to save the files: "))
res_init()
url = raw_input("Enter the url : ")
print "Fetching html...."
htm = urllib2.urlopen(url).read()
print "Creating Soup...."
soup = BeautifulSoup(htm, "lxml")
links = []
print "Finding all the links....",
for link in soup.find_all('a'):
    links.append(link.get('href')) # links will be appended in /html/blah/blah.blah
                                   # And I've to convert the links into http://www.tutorialspoint.com/html/.......
Clear(links) # To Eliminate extra links from the list
toadd = 'http://www.tutorialspoint.com'
print "Modifying links...."
for i in xrange(len(links)):
    links[i] = toadd + links[i]

print "Starting the traversal of all the links...."
for i in xrange(len(links)):
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
                if link2.get('href') is not None and '.pdf' in link2.get('href'):
                    pdf = toadd + link2.get('href')
                    command = "wget " + pdf
                    print "Downloading ....",pdf
                    os.system(command)

        except urllib2.URLError: print "Skipped"

    else:
        print "It's not a proper link"
