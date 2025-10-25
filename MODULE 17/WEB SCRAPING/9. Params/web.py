import requests
url = "http://127.0.0.1:8000/post/" # you change this url into your url because my url is required authentication 
params = {
    "offset": "10"
}

response = requests.get(url = url , params = params)
print(response.text)
