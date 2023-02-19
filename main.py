from tkinter import Tk
from move import Move

master = Tk()
move = Move(master)

master.bind("<KeyPress-Left>", lambda e: move.left(e))
master.bind("<KeyPress-Right>", lambda e: move.right(e))
master.bind("<KeyPress-Up>", lambda e: move.up(e))
master.bind("<KeyPress-Down>", lambda e: move.down(e))

master.bind("<KeyPress-a>", lambda e: move.left(e))
master.bind("<KeyPress-d>", lambda e: move.right(e))
master.bind("<KeyPress-w>", lambda e: move.up(e))
master.bind("<KeyPress-s>", lambda e: move.down(e))


master.mainloop()




