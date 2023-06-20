import json
import os
import shutil

import PIL.Image
import urllib.request
import requests

images = []
index = 0
index2 = 0
index3 = 0
with open("resources/completepklist.txt", "r") as f:
    lines = f.readlines()

shutil.rmtree('resources/pics')
os.mkdir('resources/pics')
for x in lines:
    temp = lines[index].strip()
    response = requests.get("https://pokeapi.co/api/v2/pokemon/" + temp)
    print(response.status_code)
    data = response.text
    parse_json = json.loads(data)
    urllib.request.urlretrieve(parse_json["sprites"]["other"]["official-artwork"]["front_default"], "resources/pics/" + temp + ".png")
    index = index + 1
print("done")

for x in images:
    f = open("resources/images.txt", "a")
    f.write(images[index2] + "\n")
    f.close()
    index2 = index2 + 1
    print("added" + str(index2))