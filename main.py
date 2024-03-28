import tkinter as tk
from tkinter import ttk
import random
import app
import reader

import world
#import area
import plant_species

# TODO: the name of the area after hovering above it
# TODO: each area is separated into 12 squares (3 rows 4 cols)
# TODO: you can specify with checkbox witch plants to show and which not
# TODO: you can edit data with data entry after selecting each field + submit button
# TODO: so you create separate menu with ticks (all of the world) + menu with data entry

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    reader = reader.Reader()
    #world = world.World([])
    world = reader.read()
    root = tk.Tk()
    app = app.App(root, world)
    root.mainloop()



