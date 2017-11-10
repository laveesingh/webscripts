import os
import requests
import argparse
from bs4 import BeautifulSoup as Soup
import pdfkit

HOST = "https://www.tutorialspoint.com"

def fetch_links(soup):
    uls = soup.findAll('ul', attrs={'class': 'nav nav-list primary left-menu'})
    print "Found %d uls" % len(uls)
    links = []
    for ul in uls:
        if 'tutorial' in ul.find('li').text.lower():
            for li in ul.findAll('li'):
                if li.find('a'):
                    links.append(li.find('a').get('href'))
    return links

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('url', help='url of the tutorial')
    args = parser.parse_args()
    url = args.url
    html_data = requests.get(url).content
    soup = Soup(html_data, 'html.parser')
    links = fetch_links(soup)
    for link in links:
        filename = link.split('/')[-1].split('.')[0] + '.pdf'
        print 'saving: %s....' % filename
        if os.path.isfile('archive/%s' % filename):
            continue
        pdfkit.from_url(HOST+link, 'archive/'+filename)
