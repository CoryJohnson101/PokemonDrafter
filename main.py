import random
import tkinter as tk
import urllib.request
from PIL import ImageTk, Image


def getEntryInput():
    pokemonNumber = entry.get()
    return pokemonNumber


with open("resources/completepklist.txt", "r") as f:
    lines = f.readlines()
with open("resources/typeList.txt", "r") as g:
    typeLines = g.readlines()
with open("resources/images.txt", "r") as h:
    imageLines = h.readlines()


def getPokemon(lines, typeLines, imageLines, pokemonNumber):
    pokemon = []
    for x in range(pokemonNumber):
        rand = random.randrange(0, len(lines))
        temp = lines[rand].replace("\n", "")
        temp = temp.strip()
        pokemon.append(temp)
        temp2 = typeLines[rand].replace("\n", "")
        pokemon.append(temp2)
        temp3 = imageLines[rand].replace("\n", "")
        pokemon.append(temp3)
        lines.remove(lines[rand])
        typeLines.remove(typeLines[rand])
        imageLines.remove(imageLines[rand])
    return pokemon


def nextWindow():
    pokemonNumber = getEntryInput()
    window.destroy()
    newNum = int(pokemonNumber)
    pokemon = getPokemon(lines, typeLines, imageLines, newNum)
    imageIndex = 2
    nameIndex = 0
    labels = []
    countdown = len(pokemon) // 3
    window2 = tk.Tk()
    window2.geometry("1920x1080")
    r = 0
    c = 0
    greg = 0
    dingus = 0
    window2.columnconfigure(0, weight=1)
    window2.rowconfigure(0, weight=1)
    window2.rowconfigure(1, weight=1)
    for x in range(len(pokemon) // 3):
        urllib.request.urlretrieve(pokemon[imageIndex], "resources/pics/" + pokemon[nameIndex] + ".png")
        img = Image.open("resources/pics/" + pokemon[nameIndex] + ".png")
        sizedImg = img.resize((35, 45))
        i = ImageTk.PhotoImage(sizedImg)
        labels.append(tk.Label(image=i))
        print(pokemon[nameIndex])
        nameIndex = nameIndex + 3
        imageIndex = imageIndex + 3



window = tk.Tk()
entryText = tk.Label(text="How many Pokemon would you like?")
entry = tk.Entry()
entryButton = tk.Button(text="Submit", command=nextWindow)
entryText.pack()
entry.pack()
entryButton.pack()
window.mainloop()
