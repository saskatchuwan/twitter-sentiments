from flask import Flask
import sys

# sys.path.insert(0, '/Users/kathrynchu/src/twitter-sentiments/scraper/src')
# from search_scraper import SearchScraper
# from user_scraper import UserScraper

# creates a Flask application, named app
app = Flask(__name__)


@app.route("/")
def hello():
    message = "Hello, World"
    return 'Hello, World!'

# if __name__ == '__main__':
#   # scraper = SearchScraper() 
#   # print(scraper.perform_scrape('avocadoes'))

#   scraper = UserScraper() 
#   print(scraper.perform_scrape('Call_Me_Dutch'))

