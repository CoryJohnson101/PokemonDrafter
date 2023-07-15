import json
import os
import shutil

import PIL.Image
import urllib.request
import requests

with open("resources/completepklist.txt", "r") as f:
    lines = f.readlines()


def UpdateImageList():
    images = []
    index = 0
    index2 = 0
    shutil.rmtree('resources/pics')
    os.mkdir('resources/pics')
    for x in lines:
        temp = lines[index].strip()
        response = requests.get("https://pokeapi.co/api/v2/pokemon/" + temp)
        data = response.text
        parse_json = json.loads(data)
        urllib.request.urlretrieve(parse_json["sprites"]["other"]["official-artwork"]["front_default"],
                                   "resources/pics/" + temp + ".png")
        print(index)
        index = index + 1
    print("done")


#this is probably trash
    for x in images:
        f = open("resources/images.txt", "a")
        f.write(images[index2] + "\n")
        f.close()
        index2 = index2 + 1
        print("added" + str(index2))

# UpdateImageList()
def UpdateSpriteList():
    images = []
    index = 0
    index2 = 0
    shutil.rmtree('resources/sprites')
    os.mkdir('resources/sprites')
    for x in lines:
        try:
            temp = lines[index].strip()
            response = requests.get("https://pokeapi.co/api/v2/pokemon/" + temp)
            data = response.text
            parse_json = json.loads(data)
            urllib.request.urlretrieve(parse_json["sprites"]["front_default"], "resources/sprites/" + temp + ".png")
            print(index)
            index = index + 1
        except TypeError as e:
            temp = "dedenne"
            response = requests.get("https://pokeapi.co/api/v2/pokemon/" + temp)
            data = response.text
            parse_json = json.loads(data)
            urllib.request.urlretrieve(parse_json["sprites"]["front_default"], "resources/sprites/" + temp + ".png")
    print("done part 2")

    for x in images:
        f = open("resources/images.txt", "a")
        f.write(images[index2] + "\n")
        f.close()
        index2 = index2 + 1
        print("added" + str(index2))

UpdateSpriteList()
# def UpdatePokemonList():