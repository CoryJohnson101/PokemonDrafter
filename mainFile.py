import random
import tkinter as tk
import urllib.request
from math import sqrt
import pyglet
import easygui
from InfoHolder import *
from PIL import ImageTk, Image


def getEntryInput():
    pokemonNumber = entry.get()
    return pokemonNumber


with open("resources/completepklist.txt", "r") as f:
    lines = f.readlines()
with open("resources/typeList.txt", "r") as g:
    typeLines = g.readlines()
with open("resources/namesformatted.txt", "r") as h:
    fullNames = h.readlines()


def getPokemon(lines, typeLines, pokemonNumber, fullNames):
    pokemon = []
    for x in range(pokemonNumber):
        rand = random.randrange(0, len(lines))
        temp = lines[rand].replace("\n", "")
        temp = temp.strip()
        pokemon.append(temp)
        temp2 = typeLines[rand].replace("\n", "")
        temp2 = temp2.strip()
        pokemon.append(temp2)
        temp3 = fullNames[rand].replace("\n", "")
        temp3 = temp3.strip()
        pokemon.append(temp3)
        fullNames.pop(rand)
        lines.remove(lines[rand])
        typeLines.pop(rand)
    return pokemon


def Hover(button, pokemon, position, image):
    # newImage = image.convert("1", dither=None)

    def on_enter(e):
        button.config(image='', font=('roboto', 22), foreground="white", background="#212121",
                      text=pokemon[position] + "\n" + pokemon[position - 1])

    def on_leave(e):
        button.config(background='#f0f0f0', text="", image=image)

    button.bind('<Enter>', on_enter)
    button.bind('<Leave>', on_leave)


def nextWindow():
    pokemonNumber = getEntryInput()
    window.destroy()
    newNum = int(pokemonNumber)
    pokemon = getPokemon(lines, typeLines, newNum, fullNames)
    nameIndex = 0
    index = 0
    hoverIndex = 2
    imgs = []
    buttons = []
    c = 0
    r = 0
    window2 = tk.Tk()
    window2.geometry("1810x960")
    container = tk.Frame(window2, width=1810, height=860)
    canvas = tk.Canvas(container)
    scrollbar = tk.Scrollbar(container, orient="vertical", command=canvas.yview)
    scrollable_frame = tk.Frame(canvas, width=1810, height=960)

    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(
            scrollregion=canvas.bbox("all")
        )
    )

    def _on_mousewheel(event):
        canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

    canvas.bind_all("<MouseWheel>", _on_mousewheel)

    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")

    canvas.configure(yscrollcommand=scrollbar.set)
    first = True
    for x in range(len(pokemon) // 3):
        imgs.append(ImageTk.PhotoImage(Image.open("resources/pics/" + pokemon[nameIndex] + ".png").resize((310, 311))))
        nameIndex = nameIndex + 3
    first = True
    for x in range(0, len(imgs) + 1):
        if first:
            first = False
            newImg = ImageTk.PhotoImage(Image.open("resources/googlesheet.png").resize((310, 311)))
            signIn = tk.Button(scrollable_frame, compound=tk.CENTER, image=newImg, command=createsheet)
            signIn.grid(row=r, column=c, sticky=(tk.N, tk.S, tk.E, tk.W))
            if c != 5:
                c = c + 1
            else:
                r = r + 1
                c = 0
        else:
            buttons.append(tk.Button(scrollable_frame, compound=tk.CENTER, image=imgs[index]))
            buttons[index].grid(row=r, column=c, sticky=(tk.N, tk.S, tk.E, tk.W))
            Hover(buttons[index], pokemon, hoverIndex, imgs[index])
            if c != 5:
                c = c + 1
            else:
                r = r + 1
                c = 0
            index = index + 1
            hoverIndex = hoverIndex + 3

    container.pack(fill="both", expand=True)
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
