import requests

url = "http://127.0.0.1:5500/WEB%20SCRAPING/3.%20Retrieving%20content%20from%20web/index.html"
response = requests.get(url = url)
print(response.request.headers)
