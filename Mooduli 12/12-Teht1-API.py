import requests
import json

pyyntö = "https://api.chucknorris.io/jokes/random"
vastaus = requests.get(pyyntö).json()

print(f"Chuck Norris vitsi : {vastaus["value"]}")