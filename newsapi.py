
import requests
import secrets

base_url = 'https://newsapi.org/v2/top-headlines'
params = {
    "country": "us",
    "apiKey": secrets.NEWSAPI_KEY,
    "q": "new hampshire"
}

response = requests.get(base_url, params)
result = response.json()
articles = result['articles']
for article in articles:
    print(article['title'], '-', article['source']['name'])