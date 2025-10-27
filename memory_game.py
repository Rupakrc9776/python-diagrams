# memory_game.py
import tkinter as tk
import random, time

root = tk.Tk()
root.title("Memory Game")

symbols = list("AABBCCDDEEFF")
random.shuffle(symbols)
buttons = []
revealed = []

def click(i):
    if len(revealed) < 2 and not buttons[i]['text']:
        buttons[i]['text'] = symbols[i]
        revealed.append(i)
        if len(revealed) == 2:
            root.after(800, check_match)

def check_match():
    i1, i2 = revealed
    if symbols[i1] != symbols[i2]:
        buttons[i1]['text'] = ""
        buttons[i2]['text'] = ""
    revealed.clear()

for i in range(12):
    b = tk.Button(root, text="", width=6, height=3, command=lambda i=i: click(i))
    b.grid(row=i//4, column=i%4)
    buttons.append(b)

root.mainloop()
