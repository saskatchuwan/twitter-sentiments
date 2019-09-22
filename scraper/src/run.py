import sys

from search_scraper import SearchScraper
from user_scraper import UserScraper

if __name__ == '__main__':
  scraper = SearchScraper() 
  print(scraper.perform_scrape('avocadoes'))

  # scraper = UserScraper() 
  # print(scraper.perform_scrape('Call_Me_Dutch'))