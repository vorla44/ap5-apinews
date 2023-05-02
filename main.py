import requests
from send_email import send_email

api_key = "4bb909ddc48448b2b40563d1626f6d12"

url = "https://newsapi.org/v2/everything?q=tesla&\
from=2023-04-02&sortBy=publishedAt&apiKey=4bb909ddc48448b2b40563d1626f6d12"

#Make request
request = requests.get(url)

#Get a dictionary with data
content = request.json()

#Access the article titles and description
body = ""
for article in content["articles"]:
    if article["title"] is not None:
        body = body + article["title"] + "\n" + article["description"] + 2*"\n"

body = body.encode("utf-8")
send_email(message = body)

