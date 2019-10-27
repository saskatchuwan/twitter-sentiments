import os
from flask import Flask, jsonify

from src.handlers import execute_user_tweet_analysis, execute_search_tweet_analysis

app = Flask(__name__)

@app.route("/", methods=['GET'])
def hello():
    return "This is my twitter analyzer!"

@app.route("/analyze/user/<username>", methods=['GET'])
def user(username):
    results = execute_user_tweet_analysis(username)
    return jsonify(results)

@app.route("/analyze/search/<query>", methods=['GET'])
def search(query):
    results = execute_search_tweet_analysis(query)
    return jsonify(results)

if __name__ == '__main__':
    host = "0.0.0.0"
    port = 5001

    try:
        host = os.environ['ANALYZER_HOSTNAME']
    except KeyError:
        print("Hostname not found in environment. Reverting to default value: " + host)
    
    try:
        port = os.environ['ANALYZER_PORT']
    except KeyError:
        print("Port not found in environment. Reverting to default value: " + str(port))
    
    app.run(host=host, port=int(port), debug=False)