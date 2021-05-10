import pandas as pd
import requests

def News():
  main_url = " https://newsapi.org/v2/top-headlines?country=in&category=health&apiKey=085535b65cac467784c59d52bc9b1c2d"

  # fetching data in json format
  res = requests.get(main_url)
  open_bbc_page = res.json()

  # getting all articles in a string article
  article = open_bbc_page["articles"]

  # empty list which will
  # contain all trending news
  results = []

  for ar in article:
    results.append(ar["title"])

  return results


# Driver Code
if __name__ == '__main__':
  # function call
  News()