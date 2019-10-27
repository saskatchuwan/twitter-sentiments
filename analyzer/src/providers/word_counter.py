from collections import Counter

def find_most_common(tokens, count=5):
  word_freq = Counter(tokens)
  common_words = word_freq.most_common(count)
  return common_words