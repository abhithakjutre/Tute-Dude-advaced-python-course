import urllib.request, urllib.parse, urllib.error
url = urllib.request.urlopen("http://127.0.0.1:5500/WEB%20SCRAPING/3.%20Retrieving%20content%20from%20web/index.html")

for line in url:
    print(line.decode().strip())