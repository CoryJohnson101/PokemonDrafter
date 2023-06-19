import json
import PIL.Image
import urllib.request
import requests

images = []
index = 0
index2 = 0
index3 = 0
with open("resources/completepklist.txt", "r") as f:
    lines = f.readlines()

for x in lines:
    lines[index3] = x
    print(lines[index3])
    index3 = index3 + 1
for x in lines:
    response = requests.get("https://pokeapi.co/api/v2/pokemon/" + lines[index])
    data = response.text
    parse_json = json.loads(data)
    images.append(parse_json['sprites']['other']['official-artwork']['front_default'])
    print(parse_json['sprites']['other']['official-artwork']['front_default'])
    index = index + 1

for x in images:
    f = open("resources/images.txt", "a")
    f.write(images[index2] + "\n")
    f.close()
    index2 = index2 + 1
    print("added" + str(index2))