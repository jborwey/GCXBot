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

    print("Getting 20 posts...\n")

    subreddit = reddit.subreddit('giftcardexchange')
    for submission in subreddit.new(limit=30):
        match = re.findall("Amazon", submission.title)
        if match:
            print('Match found in submission: ' + submission.title)

        time.sleep(10)


def main():
    reddit = authenticate()
    while True:
        run_subwaybot(reddit)


if __name__ == '__main__':
    main()