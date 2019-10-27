import spacy

nlp = spacy.load('en_core_web_sm')

def preprocess_all_tokens(tweets):
  all_tokens = []

  for tweet in tweets:
    doc = nlp(tweet)
    tokens = filter_tokens(doc)
    all_tokens.extend(tokens)

  return all_tokens

#private methods
def filter_tokens(doc):
  complete_filtered_tokens = [preprocess_token(token) for token in doc if is_token_allowed(token)]
  return complete_filtered_tokens

def is_token_allowed(token):
  if (not token or not token.string.strip() or token.is_stop or token.is_punct or token.is_space):
    return False
  return True

def preprocess_token(token):
  return token.lemma_.strip().lower()
