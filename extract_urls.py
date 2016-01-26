#!/usr/bin/python

# This script takes the url of the playlist and returns a dictionary
# that has values as the urls of the videos in that playlist and keys as the
# indices of those videos.
#
# Remember this script returns codes that are embedable.


from pprint import pprint
import re
import urllib
from bs4 import BeautifulSoup
urlplay = raw_input("Enter the url of the playlist: ")
print "extracting...."
if 'watch' in urlplay and 'list=' in urlplay:
    pattern = ('watch.*?&')
    search = re.search(pattern, urlplay)
    start = search.start()
    end = search.end()
    tor = urlplay[start:end]
    new = 'playlist?'
    urlplay = urlplay.replace(tor, new)

data = urllib.urlopen(urlplay)
html = data.read()
soup = BeautifulSoup(html)

a = set()
for s in soup.findAll('a'):
    if s.get('href') and s.get('href').startswith('/watch'):
        a.add(s.get('href'))

print "Total " + str(len(a)) + " videos found in the playlist."


choice = raw_input("""What do you want?
    1. Simple Videos urls
    2. Embedable videos urls
    Enter your choice and hit enter,
    Or simply hit enter for default(Simple urls): """)

choice = choice if choice else 1

choice = int(choice)
print "Your choice is", choice
if choice == 1:
    print "Extracting simple videos urls..."
    pattern = "(/watch\?v=.*?)&"
    base = "https://www.youtube.com"
    links = {}
    for s in a:
        trail = re.findall(pattern, s)[0]
        index = re.findall('index=([0-9]*)', s)
        if not index:
            continue
        index = int(index[0])
        links[index] = base + trail
    for s in links:
        print links[s]


if choice == 2:
    print "Extracting embedable videos urls..."
    pattern = "/watch\?v=(.*?)&"
    base = "https://www.youtube.com/embed/"
    links = {}
    for s in a:
        Hash = re.findall(pattern, s)[0]
        index = re.findall('index=([0-9]*)', s)
        if not index:
            continue
        index = int(index[0])
        links[index] = base + Hash
    pprint(links)
