#!/usr/bin/ env python
import Tkinter as tk

root = tk.Tk()

# top_fr = tk.Frame(root)
# top_fr.pack(side='top')
intro = tk.Label(
    text="Nobody Explodes Companion", 
    font="Times 22 bold", 
    justify='left').grid(row=0, column=0)
# intro.pack(side='left')
bt_killit = tk.Button( 
    text="Make It Stop", 
    fg="red", 
    font="Helvetica 12 bold",
    command=root.destroy)
bt_killit.grid(row=0, column=2)

# rightside_fr = tk.Frame(root)
# rightside_fr.pack(side='bottom')
# bt_wires = tk.Button(rightside_fr, text="Wires", width=10)
# bt_wires.pack(side='right')
# bt_symbols = tk.Button(rightside_fr, text="Symbols", width=10)
# bt_symbols.pack(side='right')


root.mainloop()