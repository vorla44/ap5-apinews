import requests
from send_email import send_email

topic = "tesla"

api_key = "4bb909ddc48448b2b40563d1626f6d12"
url = "https://newsapi.org/v2/everything?"\
    f"q={topic}&"\
    "sortBy=publishedAt&"\
    "apiKey=4bb909ddc48448b2b40563d1626f6d12&"\
    "language=en"

#Make request

request = requests.get(url)

#Get a dictionary with data
content = request.json()

#Access the article titles and description
body = ""
for article in content["articles"][:5]:
    if article["title"] is not None:
        body = "Subject: Today's  news "\
               + "\n" + body + article["title"] + "\n" \
               + article["description"] \
               + "\n" + article['url'] + 2*"\n"

body = body.encode("utf-8")
send_email(message=body)

