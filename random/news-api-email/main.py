import requests
from send_email import send_email

API_KEY = "Enter Your newsapi key here"
url = f"https://newsapi.org/v2/everything?q=tesla&from=2026-02-10&sortBy=publishedAt&apiKey={API_KEY}"


# Make a request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

# Acess the article titles and description
body = ""
for article in content["articles"]:
    if article["title"] is not None:
        body = body + article["title"] + "\n" + article["description"] + 2*"\n"
    
body = body.encode("utf-8")
send_email(message=body)