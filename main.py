import requests

api_key = "4bb909ddc48448b2b40563d1626f6d12"

url = "https://newsapi.org/v2/everything?q=tesla&\
from=2023-04-02&sortBy=publishedAt&apiKey=4bb909ddc48448b2b40563d1626f6d12"

#Make request
request = requests.get(url)

#Get a dictionary with data
content = request.json()

#Access the article titles and description
for article in content["articles"]:
    print(article["title"])
    print(article["description"])
