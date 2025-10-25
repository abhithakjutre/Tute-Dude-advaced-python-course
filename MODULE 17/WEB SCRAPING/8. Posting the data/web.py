import requests
url = "http://127.0.0.1:8000/post/" # you change this url into your url because my url is required authentication 
payload = {
    "title": "Greetings",
    "body":"Welcome to python. by Abhi-Coder"
}
response = requests.get(url = url , data= payload)
print(response.text)
