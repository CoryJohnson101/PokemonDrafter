import tkinter as tk


def getEntryInput():
    pokemonNumber = entry.get()
    return pokemonNumber


def nextWindow():
    pokemonNumber = getEntryInput()
    print(pokemonNumber)
    window.destroy()
    window2 = tk.Tk()
    window2.mainloop()


window = tk.Tk()
entryText = tk.Label(text="How many Pokemon would you like?")
entry = tk.Entry()
entryButton = tk.Button(text="Submit", command=nextWindow)
entryText.pack()
entry.pack()
entryButton.pack()
window.mainloop()
