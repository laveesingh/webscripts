from __future__ import print_function
import bs4
import re
import argparse
import os
import urllib

# Map %20 to space
# Name can be extracted as prefix of season specification
# Make URL or search terms interchangeable

parser = argparse.ArgumentParser()
parser.add_argument('-f', '--folder', help="keep the files in the folder specified")
parser.add_argument('-n', '--name', help="name of the tv series, to name files particularly")
parser.add_argument('-s', '--start-index', help="Number of video to start from", type=int)
parser.add_argument('-e', '--end-index', help="Number of video to stop at", type=int)
parser.add_argument('-r', '--rate-limit', help="Maximum internet bandwidth to be used in KiloBytes", type=int)
parser.add_argument('-nt', '--number-of-threads',  help="In case of slow server and a fast internet connection, more threads will result in efficient usage of bandwidth", type=int)
parser.add_argument('-v', '--video-extension', help="Most of servers serve videos as .mkv files, if it's different please specify")
parser.add_argument('url', help="URL of the page that contains video links")
arguments = parser.parse_args()

URL = arguments.url
folder_name = None
series_name = None
season_number = None
no_of_threads = None
bandwidth = None
start_index = None
end_index = None
extension = arguments.video_extension if arguments.video_extension else 'mkv'

# Setting series name and season number
if not arguments.name:
    pat = r"/(?P<name>[\w\-\.]+)/?(s(?P<no>[0-9])+|season[\-\.]?(?P<nu>[0-9]+))"
    match = re.search(pat, URL.lower().replace('%20', '-'))
    if match.group('name'):
        series_name = match.group('name')
    else:
        series_name = raw_input("You have to enter the tv series name: ")
    if match.group('no'):
        season_numbner = match.group('no')
    elif match.group('nu'):
        season_numbner = match.group('nu')
    else:
        season_number = input("You have to enter the season number: ")
else: series_name = arguments.name

# Setting folder name
if not arguments.folder :
    folder_name = series_name + str(season_number).zfill(2)
    folder_name = os.getcwd() + '/' + folder_name
else:
    folder_name = arguments.folder
    if folder_name.startswith('/') or folder_name.startswith('~'):
        None
    else:
        folder_name = os.getcwd() + '/' + folder_name
if os.path.exists(folder_name):
    print ("Directory already present")
else:
        os.mkdir(folder_name)
previous_directory = os.getcwd()
os.chdir(folder_name)


# Bandwidth management
no_of_threads = arguments.number_of_threads if arguments.number_of_threads else 5
bandwidth /= 5

# Fetch the page source
html = urllib.urlopen(URL).read()
soup = bs4.BeautifulSoup(html, 'html.parser')
links = []
for anchor in soup.findAll('a'):
    if any([s in anchor.get('href') for s in ['mp4', 'mkv', 'avi']]):
