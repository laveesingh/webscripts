__author__ = 'lavee_singh'

from bs4 import BeautifulSoup
import urllib2, os, ctypes

# This function is force glibc to read /etc/resolv.conf again
libc = ctypes.cdll.LoadLibrary('libc.so.6')
res_init = libc.__res_init

# Where do you want to save the downloaded files
os.chdir(raw_input("Enter the path of the directory where you want to save the files: "))
res_init()

# Give the url of index page, however, you can give the url of any link from the page you want.
url = raw_input("Enter the url : ")
print "Fetching html...."

# Fetch the html to store in htm
htm = urllib2.urlopen(url).read()
print "Creating Soup...."
soup = BeautifulSoup(htm, "lxml")
links = []
print "Finding all the links....",
for link in soup.find_all('a'):
    links.append(link.get('href')) # links will be appended in /html/blah/blah.blah
                                   # And I've to convert the links into http://www.tutorialspoint.com/html/.......

toadd = 'http://www.tutorialspoint.com'
print "Modifying links...."
for i in xrange(len(links)):
    links[i] = toadd + links[i]

#
print links

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
