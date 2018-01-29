from bs4 import BeautifulSoup

import praw
import time
import re
import requests
import bs4

path = '.\commented.txt'


def authenticate():
    print('Authenticating...\n')
    reddit = praw.Reddit('subwaybot', user_agent = 'web:subwaybot:v0.1 (by /u/ArtigoQ)')
    print('Authenticated as {}\n'.format(reddit.user.me()))
    return reddit


def run_subwaybot(reddit):

    print("Getting 30 posts...\n")

    subreddit = reddit.subreddit('giftcardexchange')
    for submission in subreddit.new(limit=30):
        match = re.findall("Subway", submission.title)
        if match:
            print('Match found in submission: ' + submission.title)

            file_obj_r = open(path, 'r')

            if submission.id not in file_obj_r.read().splitlines():
                print('Submission is unique, saving for future reference')

                file_obj_r.close()

                file_obj_w = open(path, 'a+')
                file_obj_w.write(submission.id + '\n')
                file_obj_w.close()
            else:
                    print('Already visited link...no reply needed\n')

        time.sleep(10)

    print('Waiting 60 seconds...\n')
    time.sleep(60)


def main():
    reddit = authenticate()
    while True:
        run_subwaybot(reddit)


if __name__ == '__main__':
    main()