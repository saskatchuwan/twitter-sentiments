from bs4 import BeautifulSoup

import requests
import sys
sys.path.insert(0, '/Users/kathrynchu/src/twitter-sentiments')
import proxy

import tweet


class TwitterScraper( object ):

  def perform_scrape(self, query_term):
    print('query_term received ' + query_term)
    url = f"https://twitter.com/search?f=tweets&q={query_term}&lang=en"
    headers = proxy.get_headers()
    print(headers)

    response = requests.get(url, headers=headers)
    print("-- STATUS " + str(response.status_code) + " -- " + url)
    if response.status_code == 200:
      self.parse_tweets(response, 'search')


  def parse_tweets(self, response_obj, content_type):
    soup = BeautifulSoup(response_obj.text, 'lxml')

    tweets_list = list()
    tweets = soup.find_all("li", {"data-item-type": "tweet"})

    for bs4_tweet in tweets:
        tweet_text = tweet.Tweet(content_type, bs4_tweet).get_tweet_text()
        tweets_list.append(tweet_text)

    print(str(len(tweets_list)) + " tweets found.")
    print(tweets_list)
    return tweets_list

