#!/usr/bin/ env python
import Tkinter as tk

root = tk.Tk()

top_fr = tk.Frame(root)
top_fr.pack()
intro = tk.Label(top_fr, text="Nobody Explodes Companion", font="Times 22 bold")
intro.pack(side='left')
bt_killit = tk.Button(
    top_fr, 
    text="Make It Stop", 
    fg="red", 
    bg="black", 
    font="Helvetica 12 bold",
    command=root.destroy)
bt_killit.pack(side='right')

bottom_fr = tk.Frame(root)
bottom_fr.pack(side='bottom')
bt_wires = tk.Button(bottom_fr, text="Wires", font="Helvetica 16", width=10)
bt_wires.pack(side='right')
bt_symbols = tk.Button(bottom_fr, text="Symbols", font="Helvetica 16", width=10)
bt_symbols.pack(side='right')


root.mainloop()