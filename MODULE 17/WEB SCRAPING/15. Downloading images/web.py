import requests

user_query = input("Enter image name: ")
user_agent = { 
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
}
url = f"https://www.google.com/search?q={user_query}+images&sca_esv=c66570702dbaae6e&hl=en&udm=2&biw=1920&bih=911&sxsrf=AE3TifNXV_n6jmgu5U3jhy0d7qvaDOH7aQ%3A1761410167955&ei=d_z8aNeIOsCS4-EPzrrCwAc&ved=0ahUKEwiXoPWa5L-QAxVAyTgGHU6dEHgQ4dUDCBE&uact=5&oq=coding+images&gs_lp=Egtnd3Mtd2l6LWltZyINY29kaW5nIGltYWdlczIFEAAYgAQyBRAAGIAEMgUQABiABDIFEAAYgAQyBRAAGIAEMgUQABiABDIFEAAYgAQyBRAAGIAEMgUQABiABDIFEAAYgARI5OMCUMEMWKPiAnAJeACQAQCYAcUBoAHNEKoBBDAuMTK4AQPIAQD4AQGYAhOgApAOqAIEwgIHECMYJxjJAsICBhAAGAcYHsICCBAAGIAEGLEDwgINEAAYgAQYsQMYQxiKBcICChAAGIAEGEMYigXCAgsQABiABBixAxiDAcICChAjGCcYyQIY6gKYAwKIBgGSBwQ5LjEwoAfyQbIHBDAuMTC4B_QNwgcGMC4xOC4xyAct&sclient=gws-wiz-img"


response = requests.get(url = url, headers=user_agent).content
print(response)