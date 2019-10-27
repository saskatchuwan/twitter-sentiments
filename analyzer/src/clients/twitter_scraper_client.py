import os
import http.client
import json

def get_user_tweets(username):
  client = initialize_client()

  client.request("GET", "/user/" + username)
  response = client.getresponse().read()
  return json.loads(response.decode())

def get_search_tweets(searchterm):
  client = initialize_client()

  client.request("GET", "/search/" + searchterm)
  response = client.getresponse().read()
  return json.loads(response.decode())

def initialize_client():
  scraper_host = "0.0.0.0"
  scraper_port = 5000

  try:
      scraper_host = os.environ['SCRAPER_HOSTNAME']
  except KeyError:
      print("Hostname not found in environment. Reverting to default value: " + scraper_host)
  
  try:
      scraper_port = os.environ['SCRAPER_PORT']
  except KeyError:
      print("Port not found in environment. Reverting to default value: " + str(scraper_port))
    
  connection = http.client.HTTPConnection(scraper_host, scraper_port)

  return connection