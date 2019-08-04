from bs4 import BeautifulSoup

class Tweet():

  def __init__(self, content_type, bs4_tweet):
    self.bs4_tweet = bs4_tweet
    self.content_type = content_type

  def get_tweet_text(self):
    try:
      if self.content_type == 'search':
        tweet_text_box = self.bs4_tweet.find("p", {"class": "TweetTextSize js-tweet-text tweet-text"})
        images_in_tweet_tag = tweet_text_box.find_all("a", {"class": "twitter-atreply pretty-link js-nav"})

      else:
        tweet_text_box = self.bs4_tweet.find("p", {"class": "TweetTextSize TweetTextSize--normal js-tweet-text tweet-text"})
        images_in_tweet_tag = tweet_text_box.find_all("a", {"class": "twitter-timeline-link u-hidden"})
        
      tweet_text = tweet_text_box.text
      for image_in_tweet_tag in images_in_tweet_tag:
          tweet_text = tweet_text.replace(image_in_tweet_tag.text, '')

      return tweet_text

    except Exception as e:
        return None

