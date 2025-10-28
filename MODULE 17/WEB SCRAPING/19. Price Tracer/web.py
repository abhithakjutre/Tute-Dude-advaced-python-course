import requests
from bs4 import BeautifulSoup

class PriceTracer: 
    def __init__(self, url):
        self.url = url
        self.user_agent = {"User-Agent" : "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Mobile Safari/537.36"}
        self.response =  requests.get(url=self.url, headers=self.user_agent).text
        self.soup = BeautifulSoup(self.response, "lxml")
        
    def product_title(self):
        title = self.soup.find("span", {"id": "productTitle"}) # I don't understand, why this not working. I think the Amazon website blocks simple scraping attempts.
        if title:
            return title.text.strip()
        else:
            return "Title tag not found"
        
    def product_price(self): 
        title = self.soup.find("span", {"class" : "a-price-whole"})
        if title is not None: 
            return f"Price: {title.text.strip()}"
        else: 
            return "Tag not Found"


url = "https://www.amazon.in/MSI-i5-13420H-Windows-GeForce-B13UC-1805IN/dp/B0CV9J1QSM/ref=sr_1_3?crid=1QUB7IVCYFU1G&dib=eyJ2IjoiMSJ9.qZIh1ii6-azVZo4_dNgF6P9eLJhb9AGwx7v5Hvn2B3Y6z0se3_tMiuXuecWkztP5SrfMJ80t-mxufeDNkBewCv2ma9k4bdZntcJRmOir02lKfqzpM9YE7yguP30-1TbgnCyQ1NsADrQUf4aPSIqZqRVZiK-P8Tk9INZ7iIMowbY0GuYvlAmfAACGtNP2k_YdvfhG8YsP3ikRlK_Moc7tGjj0NkAIeSew9BOGOGSvA2c.td5j73OnB0MwGIZkFKcKkbHJZO3xLvp0geHv7_44DAQ&dib_tag=se&keywords=laptop%2Bmsi&qid=1761492773&sprefix=laptop%2Bmsi%2Caps%2C263&sr=8-3&th=1"
device = PriceTracer(url=url)
print(device.product_title())
print(device.product_price())