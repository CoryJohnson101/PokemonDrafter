import tkinter as tk


def getEntryInput():
    pokemonNumber = entry.get()
    return pokemonNumber


window = tk.Tk()
entryText = tk.Label(text="How many Pokemon would you like?")
entry = tk.Entry()
entryButton = tk.Button(text="Submit", command=getEntryInput)
entryText.pack()
entry.pack()
entryButton.pack()
window.mainloop()
