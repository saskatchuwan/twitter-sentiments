from bs4 import BeautifulSoup

import requests
import sys
sys.path.insert(0, '/Users/kathrynchu/src/twitter-sentiments')
import proxy

import tweet
from twitter_scraper import TwitterScraper

class UserScraper( TwitterScraper ):

  def perform_scrape(self, handle):
    print('handle received ' + handle)
    url = "https://twitter.com/" + handle
    headers = proxy.get_headers()

    response = requests.get(url, headers=headers)
    print("-- STATUS " + str(response.status_code) + " -- " + url)
    if response.status_code == 200:
        TwitterScraper.parse_tweets(self, response, 'user')