from __future__ import print_function
import bs4
import argparse
import os
import requests
import threading
import time
import youtube_dl
import urllib

from YTDLogger import YTDLogger, ytd_hook



def fetch_videos_links(url):
    print('fetching html data...')
    html_content = requests.get(url).content
    print('done!')
    soup = bs4.BeautifulSoup(html_content, 'html.parser')
    videos_links = []
    print('fetching videos links from webpage')
    for anchor in soup.findAll('a'):
        # if anchor.get('href') in 'mp4mkvavi':  # need more formats
        if any((s in anchor.get('href')) for s in ['mp4', 'mkv', 'avi']):
            videos_links.append(anchor.get('href'))
    print('returning %d videos links' % len(videos_links))
    return videos_links


def download_videos(ydl, videos):
    for tv_cnt in xrange(100000):
        if not os.path.isdir('tv_series%d' % tv_cnt):
            os.mkdir('tv_series%d' % tv_cnt)
            os.chdir('tv_series%d' % tv_cnt)
            break

    for video in videos:
        print('creating new thread for new video...')
        time.sleep(5)
        threading.Thread(
            target=download_video,
            kwargs={
                'video_url': video,
                'ydl': ydl
            }
        ).start()
    os.chdir('..')

def download_video(ydl, video_url):
    global args
    if not video_url.startswith('http'):
        video_url = args.url + ('' if args.url.endswith('/') else '/') + urllib.unquote(video_url)
    ydl.download([video_url])
    print('active threads: %d', threading.active_count())


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('url', help='url of page that contains tv series videos')
    args = parser.parse_args()
    # ydl = youtube_dl.YoutubeDL({
        # 'logger': YTDLogger,
        # 'progress_hooks': [ytd_hook]
    # })
    ydl = youtube_dl.YoutubeDL()
    videos_links = fetch_videos_links(args.url)
    download_videos(ydl, videos_links)
