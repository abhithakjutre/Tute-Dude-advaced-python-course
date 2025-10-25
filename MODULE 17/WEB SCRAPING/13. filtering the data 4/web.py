import requests
from bs4 import BeautifulSoup


def Extract(url):
    
    response = requests.get(url=url).content
    soup = BeautifulSoup(response,'lxml')
    tag = soup.find("div", {"id": "content"})
    p= tag.find_all("p")
    content =[p.text for p in p]
    print(content)
Extract(url= "http://127.0.0.1:5500/6.%20Content/index.html") # This index file is in the "6. Content" folder

