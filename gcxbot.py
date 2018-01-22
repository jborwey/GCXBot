import praw
import requests
from lxml import html

path = '.\commented.txt'
REDIRECT_URI = 'http://localhost:65010/reddit_callback'
url = 'https://www.reddit.com/r/giftcardexchange/'


def authenticate():
    print('Authenticating...\n')
    reddit = praw.Reddit('explainbot', user_agent='web:subway-bot (by /u/ArtigoQ)')
    print('Authenticated as {}\n'.format(reddit.user.me()))
    return reddit


def run_subwaybot(reddit):


def get_parsed_page(url):
    """return the content of the site page on the url in
    a parsed lxml format that is easy to query."""

    response = requests.get(url)
    parsed_page = html.fromstring(response.content)
    return parsed_page


parsed_page = get_parsed_page(url)

# Print the subreddits post titles
parsed_page.xpath('//p/a/text()')  # ['Data, what now?'].


post_urls = parsed_page.xpath('//p/a/@href')


for post_url in post_urls:
    print('Post url:', post_url)


    parsed_post_page = get_parsed_page(post_url)
    paragraph_title_xpath = '//p[@class="title"]/a/text()'
    paragraph_titles = parsed_post_page.xpath(paragraph_title_xpath)
    paragraph_titles = map(lambda x: ' \n ' + x, paragraph_titles)
    print(''.join(paragraph_titles) + '\n')


def main():
    reddit = authenticate()
    while True:
        run_subwaybot(reddit)


if __name__ == '__main__':
    main()