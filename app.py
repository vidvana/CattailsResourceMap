import tkinter as tk
import plant_species
import saver

import logging
import logging_config

logging_config.config()
loggerSave = logging.getLogger(__name__ +  ".Save")
loggerUpdateScreen = logging.getLogger(__name__ +  ".UpdateScreen")
logging.basicConfig(filename='myapp.log', level=logging.INFO)


class App:

    def update_square(self, col, row):
        x1 = col * self.square_size
        y1 = row * self.square_size
        x2 = x1 + self.square_size
        y2 = y1 + self.square_size
        # SOURCE:  https: // stackoverflow.com / questions / 68027222 / can - you - make - a - functional - invisible - button - in -tkinter
        # I need for squares to react on click (and hover?)
        # , but I can't have it with buttons, bc the buttons can't be invisible
        if (self.active_area_x == col and self.active_area_y == row):
            self.map_canvas.create_rectangle(x1, y1, x2, y2, fill="light gray", outline="gray")
        else:
            self.map_canvas.create_rectangle(x1, y1, x2, y2, fill="white", outline="light gray")
        padding = 8
        space_between_vert = 4
        space_between_hor = 3
        rect_height = 24
        rect_width = 8
        plant_counter = 0
        current_area = self.world.get_area(col, row)
        for plant, quantity in self.world.get_area(col, row).get_plants().items():
            x1_small = x1 + padding + ((plant_counter % 5) * (rect_width + space_between_hor))
            x2_small = x1_small + rect_width
            if plant_counter < 5:
                y1_small = y1 + padding
                y2_small = y1_small + rect_height
            else:
                y1_small = y1 + space_between_vert + padding + rect_height
                y2_small = y1_small + rect_height
            if plant_counter in self.selected_plants:
                if plant_species.harvest_times[plant_counter][self.selected_season] == 1:
                    if quantity == 0:
                        color = '#EEEEEE'
                    if quantity == 1:
                        color = plant_species.colors_light[plant_counter]
                    if quantity == 2:
                        color = plant_species.colors_medium[plant_counter]
                    if quantity >= 3:
                        color = plant_species.colors_dark[plant_counter]
                else:
                    color = '#EEEEEE'
            else:
                color = '#EEEEEE'
            self.map_canvas.create_rectangle(x1_small, y1_small, x2_small, y2_small, fill=color, outline="light gray")
            plant_counter += 1

    def update_screen(self):
        loggerUpdateScreen.info("UpdateScreen() was called")
        for row in range(self.world_rows):
            for col in range(self.world_cols):
                self.update_square(col, row)

    def apply(self):
        selected_indices = self.species_listbox.curselection()
        self.selected_plants = selected_indices
        selected_indices = self.seasons_listbox.curselection()
        self.selected_season = selected_indices[0]
        self.update_screen()

    def submit(self):
        counter2 = 0
        for plant in self.active_area.get_plants():
            self.world.change_area_no_of_plants(self.active_area_x, self.active_area_y, plant,
                                           int(self.current_area_plant_quantities[counter2].get()))
            counter2 += 1
        self.update_screen()
        return

    def save(self):
        counter2 = 0
        for plant in self.active_area.get_plants():
            self.world.change_area_no_of_plants(self.active_area_x, self.active_area_y, plant,
                                           int(self.current_area_plant_quantities[counter2].get()))
            counter2 += 1
        self.update_screen()
        self.saver.save()
        return

    def area_was_chosen(self, event):
        if (event.x >= 0 and event.x <= self.square_size * self.world_cols) and (
                event.y >= 0 and event.y <= self.square_size * self.world_rows) and event.widget == self.map_canvas:
            former_active_area_x = self.active_area_x
            former_active_area_y = self.active_area_y
            self.active_area_x = int(event.x // self.square_size)
            self.active_area_y = int(event.y // self.square_size)
            self.update_square(former_active_area_x, former_active_area_y)
            self.active_area = self.world.get_area(self.active_area_x, self.active_area_y)
            self.active_area_name.config(text=self.active_area.get_name())
            counter = 0
            for plant, quantity in self.active_area.get_plants().items():
                self.current_area_plant_quantities[counter].set(str(quantity))
                counter += 1
            self.update_square(self.active_area_x, self.active_area_y)

    def __init__(self, root, world : 'World'):

        self.root = root
        self.root.title("Cattails Resource Map")

        self.world = world
        self.world_rows, self.world_cols = self.world.get_height(), self.world.get_width()

        self.saver = saver.Saver(self.world)

        self.selected_season = 0
        self.selected_plants = (0 for i in range(10))
        self.active_area_x = 0
        self.active_area_y = 0
        self.active_area = self.world.get_area(self.active_area_x, self.active_area_y)

        self.square_size = 68
        self.line_spacing = 30
        self.space_between = 10 / 2
        self.padding_top = 30

        self.canvas = tk.Canvas(root, width=self.square_size*15, height=self.square_size*10)
        self.canvas.pack()
        self.map_canvas = tk.Canvas(root, width=self.square_size * 10, height=self.square_size * 10)
        self.canvas.create_window(0, 0, anchor="nw", window=self.map_canvas)

        self.active_area_name = tk.Label(root, text=self.active_area.get_name())
        self.active_area_name.place(x=self.square_size*10+self.square_size*2.5,
                           y=self.padding_top, anchor="center")

        plant_labels = [0 for x in range(plant_species.number_of_printable_species)]
        plant_spinboxes = plant_labels.copy()
        self.current_area_plant_quantities = [tk.IntVar(root, value=0) for x in
                                              range(plant_species.number_of_printable_species)]

        for n in range(plant_species.number_of_printable_species):
            plant_labels[n] = tk.Label(root, text=plant_species.species[n])
            plant_labels[n].place(x=self.square_size * 10 + self.square_size * 2.5 - self.space_between,
                                   y=self.padding_top + 40 + n*self.line_spacing, anchor="e")
            # SOURCE: https://forums.raspberrypi.com/viewtopic.php?t=288506
            self.current_area_plant_quantities[n] = tk.StringVar()
            _values = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10')
            plant_spinboxes[n] = tk.Spinbox(self.canvas, textvariable=self.current_area_plant_quantities[n],
                                        values=_values)
            self.current_area_plant_quantities[n].set(0)
            plant_spinboxes[n].place(x=self.square_size * 10 + self.square_size * 2.5 + self.space_between,
                                     y=self.padding_top + 40 + n*self.line_spacing, anchor="w")

        # def print_num(num):
        #     print(num)
        # num2 = 56
        # submit_button = tk.Button(root, text="Submit", command=lambda: print_num(num2))
        # ^ alternative way to do it - to keep things nicely isolated
        # but since
        # a) you can't really get the returned variable of a callback (I suppose?)
        # b) but a callback of my functions HAVE TO change some variables
        # I preferred to keep it a method
        submit_button = tk.Button(root, text="Submit", command=self.submit)
        submit_button.place(x=self.square_size * 10 + self.square_size * 2.5 - 10,
                            y=self.padding_top + 20 + (len(plant_labels) + 1) * self.line_spacing, anchor="e")

        save_button = tk.Button(root, text="Save", command=self.save)
        save_button.place(x=self.square_size * 10 + self.square_size * 2.5 + 10,
                          y=self.padding_top + 20 + (len(plant_labels) + 1) * self.line_spacing, anchor="w")

        seasons = [season for season in plant_species.seasons]
        seasons_var = tk.Variable(value=seasons)
        self.seasons_listbox = tk.Listbox(
            root,
            height=10,
            listvariable=seasons_var,
            exportselection=0,
        )
        self.seasons_listbox.place(x=self.square_size * 10 + self.square_size * 2.5,
                                   y=self.padding_top + 60 + (len(plant_labels) + 1) * self.line_spacing, anchor="ne")
        self.seasons_listbox.select_set(0)

        species = [species for species in plant_species.species]
        species_var = tk.Variable(value=species)
        self.species_listbox = tk.Listbox(
            root,
            height=10,
            listvariable=species_var,
            selectmode="multiple",
            exportselection=0,
        )
        self.species_listbox.place(x=self.square_size * 10 + self.square_size * 2.5,
                                   y=self.padding_top + 60 + (len(plant_labels) + 1) * self.line_spacing, anchor="nw")

        apply_button = tk.Button(root, text="Apply", command=self.apply)
        apply_button.place(x=self.square_size * 10 + self.square_size * 2.5 - 10,
                           y=self.padding_top + 250 + (len(plant_labels) + 1) * self.line_spacing, anchor="center")

        root.bind('<Escape>', lambda e: root.destroy())
        root.bind('<Button-1>', self.area_was_chosen)
        # species_listbox.bind('<<ListboxSelect>>', items_selected2)
        # ^ this isn't working when you have 2 listboxes on one canvas (in one window)
        # since <<ListboxSelect>> event is triggered by either of them, not a specific one

        self.update_screen()

