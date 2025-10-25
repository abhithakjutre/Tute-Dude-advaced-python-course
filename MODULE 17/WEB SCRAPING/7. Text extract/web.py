import requests
url = "http://127.0.0.1:5500/WEB%20SCRAPING/6.%20Content/index.html"
response = requests.get(url= url)
print(type(response.text))