from clients.twitter_scraper_client import get_user_tweets, get_search_tweets
from .analyzer import analyze

def execute_user_tweet_analysis(username):
  user_tweets = get_user_tweets(username)['result']
  analysis = analyze(user_tweets)

  return analysis

def execute_search_tweet_analysis(queryterm):
  search_tweets = get_search_tweets(queryterm)['result']
  analysis = analyze(search_tweets)

  return analysis