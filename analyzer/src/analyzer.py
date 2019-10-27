import spacy
nlp = spacy.load('en_core_web_sm')

from providers.data_preprocessor import preprocess_all_tokens
from providers.word_counter import find_most_common

def analyze(tweets): #tweets = array of strings
  tokens = preprocess_all_tokens(tweets)

  common_words = find_most_common(tokens, 8)
  # generate sentiment analysis

  result = {
    "most_common_words": common_words
  }

  return result