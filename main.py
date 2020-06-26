#!/usr/bin/env python
# coding: utf-8

# In[1]:


from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Cryptex 0.0")

# ------

mainframe = ttk.Frame(root, padding = "5")
mainframe.grid(row = 0, column = 0)


# ------

entry_state = ['ESVWGRPHGC', 'AEACTIOIIP', 
              'RDANOSIRSR', 'MUPAUDEDTA',
              'APBLTGEDHT', 'RTOEELLUEE', 
              'KRGCASDRAR', 'SNMYUYYSYT']

def insert_s(string_s, insert_s, pos_i=0):
    return string_s[:pos_i] + insert_s + string_s[pos_i:]

last_state = list(entry_state)

for i in range(len(entry_state)):
    ABC = last_state[i]
    for ii in range(len(ABC)):
        ABC = insert_s(ABC, '\n', pos_i = ii*2+1)
    last_state[i] = ABC
    
# -----

map_ncol = len(last_state)
map_nrow = int(len(last_state[0])/2)

mapframe = ttk.Frame(mainframe, padding = 10)
mapframe.grid(row = 1, column = 0, rowspan = map_nrow, columnspan = map_ncol)

ArrowUp = PhotoImage(file = "_files/ArrowUp.png")
ArrowDown = PhotoImage(file = "_files/ArrowDown.png")

def moveUp(x, *args) :
    old_col = list(map(str, str(x.get())))
    new_col = old_col[2:] + old_col[:2]
    replacement = ''
    for i in new_col:
        replacement = replacement + str(i)
    x.set(replacement)

def moveDown(x, *args) :
    old_col = list(map(str, str(x.get())))
    new_col = old_col[-2:] + old_col[:-2]
    replacement = ''
    for i in new_col:
        replacement = replacement + str(i)
    x.set(replacement)
    
def setfunction(position = 0):
    set_x = StringVar()
    def mUp():
        return moveUp(x = set_x)
    def mDown():
        return moveDown(x = set_x)
    set_x.set(last_state[position])
    for j in range(map_ncol):
        ttk.Button(mapframe, image = ArrowUp, command = mUp).grid(row = 0, column = position)
        ttk.Label(mapframe, textvariable = set_x).grid(row = 1, column = position)
        ttk.Button(mapframe, image = ArrowDown, command = mDown).grid(row = 1, column = position, sticky = S, rowspan = 4)

for x in range(len(last_state)):
    setfunction(position = x)

# ------

ttk.Style().theme_use('xpnative')
root.mainloop()

