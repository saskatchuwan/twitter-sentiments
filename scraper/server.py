from flask import Flask, jsonify

from src.search_scraper import SearchScraper
from src.user_scraper import UserScraper

app = Flask(__name__)

@app.route("/", methods=['GET'])
def hello():
    return "This is my twitter scraper!"

@app.route("/user/<username>", methods=['GET'])
def user(username):
    scraper = UserScraper() 
    results = scraper.perform_scrape(username)
    return jsonify(result=results)

@app.route("/search/<query>", methods=['GET'])
def search(query):
    scraper = SearchScraper() 
    results = scraper.perform_scrape(query)
    return jsonify(result=results)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int("5000"), debug=False)