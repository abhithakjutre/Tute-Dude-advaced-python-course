import requests

url = "http://127.0.0.1:5500/WEB%20SCRAPING/3.%20Retrieving%20content%20from%20web/index.html"
user = {
    "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Mobile Safari/537.36"
}
response = requests.get(url = url , headers= user)
print(response.request.headers)
