import requests

query = "AI"
api = "d17c5ae759b24f0f8f6cc56b38135135"

url = f"https://newsapi.org/v2/top-headlines?country=us&q={query}&apiKey={api}"

r = requests.get(url)

data = r.json()
articles = data.get("articles", [])
for idx, a in enumerate(articles):
    print(f"{idx+1})Title:{a.get("title")}\nURL:{a.get("url")}")
    print("\n*************************************\n")
