import requests
import re
import os

user_query = input("Enter image name: ")

user_agent = { 
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
}

url = f"https://www.google.com/search?tbm=isch&q={user_query}"
response = requests.get(url, headers=user_agent).text

# Extract image URLs directly from HTML
pattern = r'"(https://[^"]*?\.(?:jpg|jpeg|png|gif))"'
images = re.findall(pattern, response)
print(f"Total Images: {len(images)}")
no_of_images = int(input("Number of images to be downloaded: "))


if images: 
    if  not os.path.exists(user_query): 
        os.mkdir(user_query)
        os.chdir(user_query)

    else: 
        os.chdir(user_query)
    for image in images[ 1:no_of_images+1]:
        image_url = image
        response = requests.get(url=image_url).content
        image_name = image_url.split("/")[-1]
        
        with open(image_name, "wb") as file: 
            file.write(response)

    


