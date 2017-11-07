import time
import subprocess
import argparse


def notify(title, msg, say=False):
    subprocess.Popen([
        'notify-send',
        title,
        msg
    ])
    if say:
        subprocess.Popen([
            'say',
            title,
            msg
        ])


def run_timer(total_time, interval=1, say=False):
    while total_time > 0:
        notify('attention', '%d minutes are remaining' % total_time, say)
        time.sleep(60)  # temporary
        total_time -= 1
    notify('', 'Your time is over', say)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('minutes', help='no of minutes to run timer for')
    parser.add_argument('-s', '--say', help='if true, say message out loud')
    args = parser.parse_args()
    total_time = args.minutes
    say = True if args.say else False
    print "running the timer"
    run_timer(int(total_time), 1, say)
