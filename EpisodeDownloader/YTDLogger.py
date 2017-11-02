from __future__ import print_function
import sys


class YTDLogger(object):
    
    def debug(self, msg):
        pass 

    def warning(self, msg):
        pass

    def error(self, msg):
        print(msg, file=sys.stderr)


def ytd_hook(d):
    if d['status'] == 'finished':
        print('download finished, saving...')
