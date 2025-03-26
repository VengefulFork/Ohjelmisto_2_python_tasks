import requests
import json
from api_key import api_key


def säätila ():
    loop = True
    while loop :
        kaupunki = input("Anna kaupungin nimi = ").capitalize()
        haku = f"http://api.openweathermap.org/geo/1.0/direct?q={kaupunki}&limit={1}&appid={api_key}"
        try :
            vastaus = requests.get(haku)
            if vastaus.status_code==200 :
                json_vastaus = vastaus.json()

                if len(json_vastaus) >= 1:
                    lat_long = (json_vastaus[0]["lat"], json_vastaus[0]["lon"])
                    haku2 = f"https://api.openweathermap.org/data/2.5/weather?lat={lat_long[0]}&lon={lat_long[1]}&appid={api_key}&units=metric"
                    vastaus2 = requests.get(haku2).json()

                    print(
                        f"Kaupungissa : {kaupunki}, lämpötila on {vastaus2["main"]["temp"]} celciusta ja säätila on {vastaus2["weather"][0]["main"]}")
                    loop = False
                else :
                    print("Kokeile uudestaan")
        except requests.exceptions.RequestException as e:
            print("Hakua ei voitu suorittaa.")





    return

säätila()




