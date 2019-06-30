from bs4 import BeautifulSoup
import json

import requests
import sys
sys.path.insert(0, '/Users/kathrynchu/src/twitter-sentiments')
import proxy

import tweet


class TwitterScraper( object ):

  def __init__( self, 
                page_url_base="https://twitter.com/search?f=tweets&lang=en&q=", 
                next_url_base="https://twitter.com/i/search/timeline?f=tweets&src=typd&q=", 
                next_url_additional='',
                content_type='search'
              ):
    self.page_url_base = page_url_base
    self.next_url_base = next_url_base
    self.next_url_additional = next_url_additional
    self.content_type = content_type

  def perform_scrape(self, query_term):
    print('query_term received ' + query_term)
    url = self.page_url_base + query_term

    response = self.request(url)
    print("-- STATUS " + str(response.status_code) + " -- " + url)

    tweets_list = list()
    if response.status_code == 200:
      soup = BeautifulSoup(response.text, 'lxml')
      tweets_list.extend(self.parse_tweets(soup, self.content_type))

      tweets_list.extend(self.get_more_tweets(soup, query_term))

    return tweets_list


  def parse_tweets(self, soup, content_type):
    tweets_list = list()
    tweets = soup.find_all("li", {"data-item-type": "tweet"})

    for bs4_tweet in tweets:
        tweet_text = tweet.Tweet(content_type, bs4_tweet).get_tweet_text()
        tweets_list.append(tweet_text)

    print(str(len(tweets_list)) + " tweets found.")
    return tweets_list

  def get_more_tweets(self, soup, query_term):
    next_pointer = soup.find("div", {"class": "stream-container"})["data-min-position"]
    tweets_list = list()

    extra_fetches = 0
    while extra_fetches <= 5:
        next_url = self.next_url_base + query_term + self.next_url_additional + '&max_position=' + next_pointer
  
        print(next_url)
        next_response = None
        try:
            next_response = self.request(next_url)
        except Exception as e:
            # in case there is some issue with request. None encountered so far.
            print(e)
            return tweets_list

        tweets_data = next_response.text
        tweets_obj = json.loads(tweets_data)

        if not tweets_obj["has_more_items"] and not tweets_obj["min_position"]:
            print("\nNo more tweets returned")
            break

        next_pointer = tweets_obj["min_position"]
        html = tweets_obj["items_html"]
        soup = BeautifulSoup(html, 'lxml')
        tweets_list.extend(self.parse_tweets(soup, self.content_type))
        extra_fetches += 1
    return tweets_list

  def request(self, url):
    headers = proxy.get_headers()
    response = requests.get(url, headers=headers)
    return response
