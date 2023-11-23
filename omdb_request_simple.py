# this is a simple request to the omdb api to investigate the json file
# Martin Vogel - martin.vogel@hslu.ch

from requests import get
# key for the omdb requests
API_KEY = "a6700fc4"

# change here the title to search
movietitle = "wizard of oz"

# request on the API -> json as a return
api_results = get(f"http://www.omdbapi.com/?apikey={API_KEY}&s={movietitle}", timeout=30)
json = api_results.json()
# observe the json content! Do you find the picture for the movie poster?
print("->json:", json)

# listing the "Search" list:
anzahlfilme=0
if json["Response"] == "True":
    for found_element in json["Search"]:
        print(found_element)
        anzahlfilme += 1

else:
    print("no movie found")
print("Es wurden "+ str(anzahlfilme) + " filme gefunden")