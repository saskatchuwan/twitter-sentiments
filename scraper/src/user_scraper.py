from bs4 import BeautifulSoup
import json

import requests

from .twitter_scraper import TwitterScraper

class UserScraper( TwitterScraper ):

  def __init__( self, 
                page_url_base="https://twitter.com/", 
                next_url_base="https://twitter.com/i/profiles/show/", 
                next_url_additional="/timeline/tweets?include_available_features=1&include_entities=1&reset_error_state=false",
                content_type='user'
              ):
    self.page_url_base = page_url_base
    self.next_url_base = next_url_base
    self.next_url_additional = next_url_additional
    self.content_type = content_type

  def perform_scrape(self, handle):
    print('handle received ' + handle)
    url = self.page_url_base + handle

    response = TwitterScraper.request(self, url)
    print("-- STATUS " + str(response.status_code) + " -- " + url)

    tweets_list = list()
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'lxml')
        tweets_list.extend(TwitterScraper.parse_tweets(self, soup, self.content_type))

        tweets_list.extend(TwitterScraper.get_more_tweets(self, soup, handle))

    return tweets_list