import requests
from random import choice

#print(response.json()["results"][0]["joke"] + "\n " + response.json()["results"][1]["joke"])
#print(len(response.json()["results"]))

def getjokes(searchword):
    url = "https://icanhazdadjoke.com/search"
    response = requests.get(url, headers={"Accept": "application/json"}, params={"term": f"{searchword}"})
    if response.status_code==200:
        if not len(response.json()["results"]):
            print ("Sorry no jokes")
        elif len(response.json()["results"])==1:
             print(response.json()["results"][0]["joke"])
        else:
            print(choice(response.json()["results"])["joke"])




getjokes("flower")