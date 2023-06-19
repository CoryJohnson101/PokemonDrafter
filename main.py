import random
import tkinter as tk
import urllib.request
from math import sqrt

from PIL import ImageTk, Image


def getEntryInput():
    pokemonNumber = entry.get()
    return pokemonNumber


with open("resources/completepklist.txt", "r") as f:
    lines = f.readlines()
with open("resources/typeList.txt", "r") as g:
    typeLines = g.readlines()


def getPokemon(lines, typeLines, pokemonNumber):
    pokemon = []
    for x in range(pokemonNumber):
        rand = random.randrange(0, len(lines))
        temp = lines[rand].replace("\n", "")
        temp = temp.strip()
        pokemon.append(temp)
        temp2 = typeLines[rand].replace("\n", "")
        pokemon.append(temp2)
        lines.remove(lines[rand])
        typeLines.remove(typeLines[rand])
    return pokemon


def nextWindow():
    pokemonNumber = getEntryInput()
    window.destroy()
    newNum = int(pokemonNumber)
    pokemon = getPokemon(lines, typeLines, newNum)
    nameIndex = 0
    index = 0
    imgs = []
    c = 0
    r = 0
    window2 = tk.Tk()
    window2.geometry("1920x1080")
    container = tk.Frame(window2, width=1920, height=1080)
    canvas = tk.Canvas(container)
    scrollbar = tk.Scrollbar(container, orient="vertical", command=canvas.yview())
    scrollable_frame = tk.Frame(canvas, width=1920, height=1080)

    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(
            scrollregion=canvas.bbox("all")
        )
    )

    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")

    canvas.configure(yscrollcommand=scrollbar.set)

    for x in range(len(pokemon) // 2):
        imgs.append(ImageTk.PhotoImage(Image.open("resources/pics/" + pokemon[nameIndex] + ".png").resize((311,311))))
        nameIndex = nameIndex + 2
    for x in imgs:
        tk.Button(scrollable_frame, image=imgs[index]).grid(row=r, column=c, sticky=(tk.N, tk.S, tk.E, tk.W))
        if c != 5:
            c = c + 1
        else:
            r = r + 1
            c = 0
        index = index + 1

    container.pack()
    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")
    window2.mainloop()



window = tk.Tk()
entryText = tk.Label(text="How many Pokemon would you like?")
entry = tk.Entry()
entryButton = tk.Button(text="Submit", command=nextWindow)
entryText.pack()
entry.pack()
entryButton.pack()
window.mainloop()
