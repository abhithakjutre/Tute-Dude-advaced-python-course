import requests
from bs4 import BeautifulSoup


def Extract(url):
    
    response = requests.get(url=url).content
    soup = BeautifulSoup(response,'lxml')
    tag1 = soup.find("div", {"id": "content"})
    tag2 = soup.find("h3", {"id": "second_text"})
    print(tag1)
    print("\n \n \n \n")
    print(tag2)


Extract(url= "http://127.0.0.1:5500/6.%20Content/index.html")

